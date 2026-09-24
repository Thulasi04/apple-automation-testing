import pytest
from playwright.sync_api import Page

from pages.apple_page import ApplePage
from pages.search_page import SearchPage
from helpers import helper_for_pages as hp


@pytest.mark.search
def test_open_search_bar(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_search()

    search.search_product("AppleCare+ for Apple TV")
    search.open_related_product()

    heading = search.get_product_heading()

    hp.assert_page(heading, "AppleCare+ for Apple TV")


@pytest.mark.search
def test_search_valid_product(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_search()

    search.search_product("MacBook Pro")

    hp.assert_contains(page.url, "search")


@pytest.mark.search
def test_search_quick_links_visibility(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_search()

    quick_links_visible = search.is_quick_links_visible()

    hp.assert_page(quick_links_visible, True)


@pytest.mark.search
def test_search_clear_input(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_search()

    search.enter_search_text("iPhone")
    search.clear_search()

    search_value = search.get_search_value()

    hp.assert_page(search_value, "")


@pytest.mark.search
def test_search_invalid_product(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_search()

    search.search_product("xyznonexistentproduct999")

    hp.assert_contains(page.url, "search")


@pytest.mark.search
def test_search_suggestions_appear(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_search()

    search_box = page.locator(
        'input[placeholder="Search apple.com"]'
    )

    search_box.fill("Watch")

    suggestions_visible = search.is_suggestions_visible()

    hp.assert_page(suggestions_visible, True)


@pytest.mark.search
def test_open_shopping_bag_dropdown(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_shopping_bag()

    heading = search.get_bag_heading()

    hp.assert_page(heading, "Your Bag is empty.")


@pytest.mark.search
def test_open_sign_in(page: Page):
    apple = ApplePage(page)
    search = SearchPage(page)

    apple.open_website()
    search.open_shopping_bag()

    sign_in_text = search.get_sign_in_text()

    hp.assert_page(sign_in_text, "Sign in")