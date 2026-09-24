from playwright.sync_api import Page

from locators import airpods_locators as locate


class AirPodsPage:

    def __init__(self, page: Page):
        self.page = page

    def open_airpods(self):
        self.page.goto("https://www.apple.com/in/airpods/")

        self.page.wait_for_load_state("domcontentloaded")

    def get_header_text(self):
        heading = self.page.locator(locate.AIRPODS_HEADER).first

        heading.wait_for(state="visible")

        return heading.text_content().strip()

    def is_airpods_page_opened(self):
        return "/in/airpods/" in self.page.url

    def click_buy_button(self):
        buy_button = self.page.get_by_role(
            "link",
            name="Buy"
        ).first

        buy_button.wait_for(state="visible")

        buy_button.click()

        self.page.wait_for_load_state("domcontentloaded")

    def open_airpods_accessories(self):
        self.page.goto(
            "https://www.apple.com/in/shop/airpods/accessories"
        )

        self.page.wait_for_load_state("domcontentloaded")

    def is_price_visible(self):
        price = self.page.get_by_text(
            "₹",
            exact=False
        ).first

        price.wait_for(state="visible")

        return price.is_visible()

    def take_screenshot(self):
        heading = self.page.locator(
            locate.AIRPODS_HEADER
        ).first

        heading.wait_for(state="visible")

        self.page.screenshot(
            path="airpods_product_page.png",
            full_page=True
        )

    def is_header_visible(self):
        heading = self.page.locator(
            locate.AIRPODS_HEADER
        ).first

        return heading.is_visible()