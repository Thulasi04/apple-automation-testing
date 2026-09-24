import pytest
from playwright.sync_api import Page

from pages.iphone_page import IPhonePage
from helpers import helper_for_pages as hp


@pytest.mark.iphone
def test_open_iphone_section(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()

    heading_text = iphone.get_header_text()

    hp.assert_contains(heading_text, "iPhone")


@pytest.mark.iphone
def test_open_iphone_17(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()
    iphone.open_iphone_17()

    url = page.url

    hp.assert_contains(url, "iphone-17")


@pytest.mark.iphone
def test_open_iphone_air(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()
    iphone.open_iphone_air()

    url = page.url

    hp.assert_contains(url, "iphone-air")


@pytest.mark.iphone
def test_iphone_buy_button_visibility(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()
    iphone.open_iphone_17()

    buy_button_visible = iphone.is_buy_button_visible()

    hp.assert_page(buy_button_visible, True)


@pytest.mark.iphone
def test_open_iphone_buy_page(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()
    iphone.open_iphone_buy_page()

    url = page.url

    hp.assert_contains(url, "shop/buy-iphone")


@pytest.mark.iphone
def test_iphone_color_selection(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()
    iphone.open_iphone_17_buy_page()

    color_option_visible = iphone.is_color_option_visible()

    hp.assert_page(color_option_visible, True)


@pytest.mark.iphone
def test_iphone_storage_options(page: Page):
    iphone = IPhonePage(page)

    iphone.open_iphone_section()
    iphone.open_iphone_buy_page()

    storage_option_visible = iphone.is_storage_option_visible()

    hp.assert_page(storage_option_visible, True)