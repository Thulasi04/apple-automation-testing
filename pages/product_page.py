from playwright.sync_api import Page

from locators import product_locators as locate

class ProductPage:

    def __init__(self, page: Page):
        self.page = page

    def open_store(self):
        self.page.goto("https://www.apple.com/in/shop/")

    def is_store_header_visible(self):
        store_header = self.page.locator(
            locate.STORE_HEADER
        ).first

        store_header.wait_for(state="visible")

        return store_header.is_visible()

    def open_mac(self):
        self.page.locator(locate.MAC_LINK).first.click()

    def open_iphone(self):
        self.page.locator(locate.IPHONE_LINK).first.click()

    def open_ipad(self):
        self.page.locator(locate.IPAD_LINK).first.click()

    def open_watch(self):
        self.page.locator(locate.WATCH_LINK).first.click()

    def click_add_to_bag(self):
        self.page.locator(locate.ADD_TO_BAG_BUTTON).click()

    def click_proceed(self):
        self.page.locator(locate.PROCEED_BUTTON).click()

    def open_shopping_bag(self):
        self.page.locator(locate.SHOPPING_BAG_BUTTON).click()

    def click_review_bag(self):
        self.page.locator(locate.REVIEW_BAG_LINK).click()