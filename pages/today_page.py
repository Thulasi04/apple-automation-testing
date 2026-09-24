from playwright.sync_api import Page

from locators import today_locators as locate


class TodayPage:

    def __init__(self, page: Page):
        self.page = page

    def open_today_at_apple(self):
        self.page.goto("https://www.apple.com/in/")

        today_link = self.page.locator(
            locate.TODAY_AT_APPLE_LINK
        ).first

        today_link.wait_for(state="visible")

        today_link.click()

        self.page.wait_for_load_state("networkidle")

    def get_header_text(self):
        heading = self.page.locator(
            locate.TODAY_HEADER
        ).first

        heading.wait_for(state="visible")

        return heading.text_content().strip()

    def is_session_visible(self):
        session_card = self.page.locator(
            locate.SESSION_CARD
        ).first

        session_card.scroll_into_view_if_needed()

        return session_card.is_visible()

    def is_store_link_visible(self):
        store_link = self.page.locator(
            locate.STORE_LINK
        ).first

        store_link.scroll_into_view_if_needed()

        return store_link.is_visible()

    def open_session_details(self):
        session_link = self.page.locator(
            locate.SESSION_CARD
        ).first

        session_link.scroll_into_view_if_needed()

        session_link.click(force=True)

        self.page.wait_for_load_state("networkidle")

    def is_header_visible(self):
        heading = self.page.locator(
            locate.TODAY_HEADER
        ).first

        return heading.is_visible()

    def open_genius_bar(self):
        self.page.goto("https://www.apple.com/in/")

        genius_bar_link = self.page.locator(
            locate.GENIUS_BAR_LINK
        ).first

        genius_bar_link.wait_for(state="visible")

        genius_bar_link.click()

        self.page.wait_for_load_state("networkidle")

    def is_event_visible(self):
        event_card = self.page.locator(
            locate.EVENT_CARD
        ).first

        event_card.scroll_into_view_if_needed()

        return event_card.is_visible()

    def open_bkc_store(self):
        self.page.goto("https://www.apple.com/in/")

        store_link = self.page.locator(
            locate.STORE_LINK
        ).first

        store_link.wait_for(state="visible")

        store_link.click()

        self.page.wait_for_load_state("networkidle")

        self.page.goto(
            "https://www.apple.com/in/retail/bkc/"
        )

        self.page.wait_for_load_state("domcontentloaded")

    def take_bkc_screenshot(self):
        self.page.screenshot(
            path="apple_bkc.png",
            full_page=True
        )