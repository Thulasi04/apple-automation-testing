from playwright.sync_api import Page

from locators import support_locators as locate


class SupportPage:

    def __init__(self, page: Page):
        self.page = page

    def open_support_website(self):
        self.page.goto("https://support.apple.com/en-in")

        self.page.wait_for_load_state("domcontentloaded")

    def get_header_text(self):
        heading = self.page.locator(
            locate.SUPPORT_HEADER
        ).first

        heading.wait_for(state="visible")

        return heading.text_content().strip()

    def is_search_button_visible(self):
        search_button = self.page.get_by_role(
            "button",
            name="Search"
        )

        return search_button.is_visible()

    def click_search_button(self):
        search_button = self.page.get_by_role(
            "button",
            name="Search"
        )

        search_button.wait_for(state="visible")

        search_button.click()

    def is_search_box_visible(self):
        search_box = self.page.locator(
            locate.SEARCH_BOX
        ).first

        search_box.wait_for(state="visible")

        return search_box.is_visible()

    def open_iphone_repair_page(self):
        self.page.goto(
            "https://support.apple.com/en-in/iphone/repair"
        )

        self.page.wait_for_load_state("domcontentloaded")

    def open_service_repair_page(self):
        self.page.goto(
            "https://support.apple.com/en-in/repair"
        )

        self.page.wait_for_load_state("domcontentloaded")

    def open_contact_page(self):
        self.page.goto(
            "https://support.apple.com/en-in/contact"
        )

        self.page.wait_for_load_state("domcontentloaded")

    def is_body_visible(self):
        body = self.page.locator(locate.BODY)

        return body.is_visible()

    def search_support(self, search_text):
        search_box = self.page.locator(
            locate.SEARCH_BOX
        ).first

        search_box.fill(search_text)

        search_box.press("Enter")

    def is_support_category_visible(self):
        support_category = self.page.locator(
            locate.SUPPORT_CATEGORY
        ).first

        return support_category.is_visible()