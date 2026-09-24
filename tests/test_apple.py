import pytest
from playwright.sync_api import Page

from pages.apple_page import ApplePage
from helpers import helper_for_pages as hp


@pytest.mark.navigation
def test_open_apple_india(page: Page):
    apple = ApplePage(page)

    apple.open_website()

    title = apple.get_title()

    hp.assert_page(title, "Apple (India)")


@pytest.mark.navigation
def test_open_store(page: Page):
    apple = ApplePage(page)

    apple.open_website()
    apple.open_store()

    hp.assert_contains(page.url, "/store")


@pytest.mark.navigation
def test_open_mac(page: Page):
    apple = ApplePage(page)

    apple.open_website()
    apple.open_mac()

    hp.assert_contains(page.url, "mac")


@pytest.mark.navigation
def test_open_ipad(page: Page):
    apple = ApplePage(page)

    apple.open_website()
    apple.open_ipad()

    hp.assert_contains(page.url, "ipad")


@pytest.mark.navigation
def test_open_iphone(page: Page):
    apple = ApplePage(page)

    apple.open_website()
    apple.open_iphone()

    hp.assert_contains(page.url, "iphone")


@pytest.mark.navigation
def test_open_watch(page: Page):
    apple = ApplePage(page)

    apple.open_website()
    apple.open_watch()

    hp.assert_contains(page.url, "watch")


@pytest.mark.navigation
def test_open_airpods(page: Page):
    apple = ApplePage(page)

    apple.open_website()
    apple.open_airpods()

    hp.assert_contains(page.url, "airpods")