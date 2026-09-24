from playwright.sync_api import Page

from locators import iphone_locators as locate


class IPhonePage:

    def __init__(self, page: Page):
        self.page = page

    def open_iphone_section(self):
        self.page.goto("https://www.apple.com/in/")

        iphone_link = self.page.locator(
            locate.IPHONE_LINK
        ).first

        iphone_link.wait_for(state="visible")

        iphone_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def get_header_text(self):
        heading = self.page.locator(
            locate.IPHONE_HEADER
        ).first

        heading.wait_for(state="visible")

        return heading.text_content().strip()

    def open_iphone_17(self):
        iphone_17_link = self.page.locator(
            locate.IPHONE_17_LINK
        ).nth(1)

        iphone_17_link.wait_for(state="visible")

        iphone_17_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def open_iphone_air(self):
        iphone_air_link = self.page.locator(
            locate.IPHONE_AIR_LINK
        ).nth(1)

        iphone_air_link.wait_for(state="visible")

        iphone_air_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def is_buy_button_visible(self):
        buy_button = self.page.get_by_text(
            "Buy",
            exact=True
        ).first

        buy_button.wait_for(state="visible")

        return buy_button.is_visible()

    def open_iphone_buy_page(self):
        buy_link = self.page.locator(
            locate.IPHONE_17_BUY_LINK
        ).first

        buy_link.wait_for(state="visible")

        buy_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def open_iphone_17_buy_page(self):
        buy_link = self.page.locator(
            'a[href="/in/shop/goto/buy_iphone/iphone_17"]'
        ).first

        buy_link.wait_for(state="visible")
        buy_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def is_color_option_visible(self):
        color_option = self.page.locator(
            locate.COLOR_OPTION
        ).first

        color_option.wait_for(state="visible")

        return color_option.is_visible()

    def is_storage_option_visible(self):
        storage_option = self.page.locator(
            locate.STORAGE_OPTION
        ).first

        storage_option.wait_for(state="visible")

        return storage_option.is_visible()