from playwright.sync_api import Page
from pages.product_page import ProductPage
from helpers import helper_for_pages as hp
import pytest

@pytest.mark.product
def test_open_store_page(page: Page):
    product = ProductPage(page)
    product.open_store()
    store_header_visible = product.is_store_header_visible()
    hp.assert_page(store_header_visible, True)

@pytest.mark.product
def test_open_mac_from_store(page: Page):
    product = ProductPage(page)
    product.open_store()
    product.open_mac()
    url = page.url
    hp.assert_contains(url, "mac")

@pytest.mark.product
def test_open_iphone_from_store(page: Page):
    product = ProductPage(page)
    product.open_store()
    product.open_iphone()
    url = page.url
    hp.assert_contains(url, "iphone")

@pytest.mark.product
def test_open_ipad_from_store(page: Page):
    product = ProductPage(page)
    product.open_store()
    product.open_ipad()
    url = page.url
    hp.assert_contains(url, "ipad")

@pytest.mark.product
def test_open_watch_from_store(page: Page):
    product = ProductPage(page)
    product.open_store()
    product.open_watch()
    url = page.url
    hp.assert_contains(url, "watch")