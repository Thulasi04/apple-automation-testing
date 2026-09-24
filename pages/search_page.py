from playwright.sync_api import Page

from locators import search_locators as locate


class SearchPage:

    def __init__(self, page: Page):
        self.page = page

    def open_search(self):
        search_button = self.page.locator(locate.SEARCH_BUTTON)
        search_button.wait_for(state="visible")
        search_button.click()

    def search_product(self, product_name):
        search_box = self.page.locator(locate.SEARCH_BOX)
        search_box.wait_for(state="visible")
        search_box.fill(product_name)
        search_box.press("Enter")
        self.page.wait_for_load_state("domcontentloaded")

    def enter_search_text(self, product_name):
        search_box = self.page.locator(locate.SEARCH_BOX)
        search_box.wait_for(state="visible")
        search_box.fill(product_name)

    def clear_search(self):
        clear_button = self.page.locator(locate.CLEAR_SEARCH_BUTTON)
        clear_button.wait_for(state="visible")
        clear_button.click()

    def get_search_value(self):
        search_box = self.page.locator(locate.SEARCH_BOX)
        return search_box.input_value()

    def is_quick_links_visible(self):
        quick_links = self.page.locator(locate.QUICK_LINKS).first
        quick_links.wait_for(state="visible")
        return quick_links.is_visible()

    def is_suggestions_visible(self):
        suggestions = self.page.locator(locate.SUGGESTIONS_PANEL).first
        suggestions.wait_for(state="visible")
        return suggestions.is_visible()

    def open_related_product(self):
        related_link = self.page.locator(locate.RELATED_LINK).first
        related_link.wait_for(state="visible")
        related_link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def get_product_heading(self):
        heading = self.page.locator(locate.PRODUCT_HEADING)
        heading.wait_for(state="visible")
        return heading.text_content().strip()

    def open_shopping_bag(self):
        bag_link = self.page.locator(locate.BAG_LINK)
        bag_link.wait_for(state="visible")
        bag_link.click()

    def get_bag_heading(self):
        heading = self.page.locator(locate.BAG_HEADING)
        heading.wait_for(state="visible")
        return heading.text_content().strip()

    def get_sign_in_text(self):
        sign_in = self.page.locator(locate.SIGN_IN_TEXT).nth(3)
        sign_in.wait_for(state="visible")
        return sign_in.text_content().strip()