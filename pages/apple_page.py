from playwright.sync_api import Page

from locators import apple_locators as locate


class ApplePage:

    def __init__(self, page: Page):
        self.page = page

    def open_website(self):
        self.page.goto("https://www.apple.com/in/")
        self.page.wait_for_load_state("domcontentloaded")

    def get_title(self):
        return self.page.title()

    def open_store(self):
        store_link = self.page.locator(locate.STORE_LINK).first
        store_link.wait_for(state="visible")
        store_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_mac(self):
        mac_link = self.page.locator(locate.MAC_LINK).first
        mac_link.wait_for(state="visible")
        mac_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_ipad(self):
        ipad_link = self.page.locator(locate.IPAD_LINK).nth(1)
        ipad_link.wait_for(state="visible")
        ipad_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_iphone(self):
        iphone_link = self.page.locator(locate.IPHONE_LINK).first
        iphone_link.wait_for(state="visible")
        iphone_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_watch(self):
        watch_link = self.page.locator(locate.WATCH_LINK).first
        watch_link.wait_for(state="visible")
        watch_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_airpods(self):
        airpods_link = self.page.locator(locate.AIRPODS_LINK).first
        airpods_link.wait_for(state="visible")
        airpods_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_shopping_bag(self):
        bag_link = self.page.locator(locate.BAG_LINK)
        bag_link.wait_for(state="visible")
        bag_link.click()

    def get_bag_heading(self):
        return self.page.locator(locate.BAG_HEADING).text_content()

    def get_sign_in_text(self):
        return self.page.locator(locate.SIGN_IN_TEXT).nth(3).text_content()