import pytest
from playwright.sync_api import Page
from pages.apple_page import ApplePage
from pages.support_page import SupportPage
from helpers import helper_for_pages as hp


@pytest.mark.support
def test_navigate_to_apple_support(page: Page):
    support = SupportPage(page)

    support.open_support_website()

    heading_text = support.get_header_text()

    hp.assert_page(heading_text, "Apple Support")


@pytest.mark.support
def test_support_search_box_visibility(page: Page):
    support = SupportPage(page)

    support.open_support_website()

    search_button_visible = support.is_search_button_visible()

    hp.assert_page(search_button_visible, True)

    support.click_search_button()

    search_box_visible = support.is_search_box_visible()

    hp.assert_page(search_box_visible, True)


@pytest.mark.support
def test_navigate_to_iphone_repair_service(page: Page):
    support = SupportPage(page)

    support.open_iphone_repair_page()

    body_visible = support.is_body_visible()

    hp.assert_page(body_visible, True)

    url = page.url

    hp.assert_contains(url, "iphone")
    hp.assert_contains(url, "repair")


@pytest.mark.support
def test_navigate_to_apple_service_repair(page: Page):
    support = SupportPage(page)

    support.open_service_repair_page()

    body_visible = support.is_body_visible()

    hp.assert_page(body_visible, True)

    url = page.url

    hp.assert_contains(url, "support.apple.com")


@pytest.mark.support
def test_navigate_to_apple_support_contact(page: Page):
    support = SupportPage(page)

    support.open_contact_page()

    body_visible = support.is_body_visible()

    hp.assert_page(body_visible, True)

    url = page.url

    hp.assert_contains(url, "support.apple.com")