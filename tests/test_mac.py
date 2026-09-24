import pytest
from playwright.sync_api import Page

from pages.mac_page import MacPage
from helpers import helper_for_pages as hp


@pytest.mark.mac
def test_open_mac_section(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()

    heading = mac.get_header_text()

    hp.assert_contains(heading, "Mac")


@pytest.mark.mac
def test_open_macbook_air(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()
    mac.open_macbook_air()

    hp.assert_contains(page.url, "macbook-air")


@pytest.mark.mac
def test_open_macbook_pro(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()
    mac.open_macbook_pro()

    hp.assert_contains(page.url, "macbook-pro")


@pytest.mark.mac
def test_mac_buy_button_visibility(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()
    mac.open_macbook_air()

    hp.assert_page(
        mac.is_buy_button_visible(),
        True
    )


@pytest.mark.mac
def test_open_macbook_air_buy_page(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()
    mac.open_macbook_air_buy_page()

    hp.assert_contains(page.url, "buy")


@pytest.mark.mac
def test_mac_colors_visibility(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()
    mac.open_macbook_air_product()

    hp.assert_page(
        mac.is_color_visible(),
        True
    )


@pytest.mark.mac
def test_mac_add_to_bag_button(page: Page):
    mac = MacPage(page)

    mac.open_mac_section()
    mac.open_macbook_air_buy_page()

    hp.assert_page(
        mac.is_body_visible(),
        True
    )

    hp.assert_contains(page.url, "buy-mac")