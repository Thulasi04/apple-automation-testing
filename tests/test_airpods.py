import pytest
from playwright.sync_api import Page
from pages.airpods_page import AirPodsPage
from helpers import helper_for_pages as hp


@pytest.mark.airpods
def test_navigate_to_airpods_page(page: Page):
    airpods = AirPodsPage(page)

    airpods.open_airpods()

    airpods_page_opened = airpods.is_airpods_page_opened()

    hp.assert_page(airpods_page_opened, True)


@pytest.mark.airpods
def test_verify_airpods_product_heading(page: Page):
    airpods = AirPodsPage(page)

    airpods.open_airpods()

    heading_text = airpods.get_header_text()

    hp.assert_contains(heading_text, "AirPods")


@pytest.mark.airpods
def test_open_airpods_buying_page(page: Page):
    airpods = AirPodsPage(page)

    airpods.open_airpods()

    airpods.click_buy_button()

    url = page.url

    hp.assert_contains(url, "shop")


@pytest.mark.airpods
def test_verify_airpods_price_visibility(page: Page):
    airpods = AirPodsPage(page)

    airpods.open_airpods_accessories()

    price_visible = airpods.is_price_visible()

    hp.assert_page(price_visible, True)


@pytest.mark.airpods
def test_take_airpods_screenshot(page: Page):
    airpods = AirPodsPage(page)

    airpods.open_airpods()

    airpods.take_screenshot()

    heading_visible = airpods.is_header_visible()

    hp.assert_page(heading_visible, True)