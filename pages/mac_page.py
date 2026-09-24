from playwright.sync_api import Page

from locators import mac_locators as locate


class MacPage:

    def __init__(self, page: Page):
        self.page = page

    def open_mac_section(self):
        self.page.goto("https://www.apple.com/in/")

        mac_link = self.page.locator(
            locate.MAC_LINK
        ).first

        mac_link.wait_for(state="visible")
        mac_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def get_header_text(self):
        heading = self.page.locator(
            locate.MAC_HEADER
        ).first

        heading.wait_for(state="visible")

        return heading.text_content().strip()

    def open_macbook_air(self):
        macbook_air_link = self.page.locator(
            f'{locate.MACBOOK_AIR_LINK}:visible'
        ).first

        macbook_air_link.wait_for(state="visible")
        macbook_air_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def open_macbook_pro(self):
        macbook_pro_link = self.page.locator(
            f'{locate.MACBOOK_PRO_LINK}:visible'
        ).first

        macbook_pro_link.wait_for(state="visible")
        macbook_pro_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def is_buy_button_visible(self):
        buy_button = self.page.get_by_text(
            "Buy",
            exact=True
        ).first

        buy_button.wait_for(state="visible")

        return buy_button.is_visible()

    def open_macbook_air_buy_page(self):
        buy_link = self.page.locator(
            f'{locate.MACBOOK_AIR_BUY_LINK}:visible'
        ).first

        buy_link.wait_for(state="visible")
        buy_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def is_color_visible(self):
        color_option = self.page.get_by_text(
            "Sky Blue",
            exact=True
        ).first

        color_option.wait_for(state="visible")

        return color_option.is_visible()

    def open_macbook_air_product(self):
        macbook_air_link = self.page.locator(
            f'{locate.MACBOOK_AIR_LINK}:visible'
        ).nth(1)

        macbook_air_link.wait_for(state="visible")
        macbook_air_link.click()

        self.page.wait_for_load_state("domcontentloaded")

    def is_body_visible(self):
        body = self.page.locator(locate.BODY)

        body.wait_for(state="visible")

        return body.is_visible()