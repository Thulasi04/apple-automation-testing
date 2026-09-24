import pytest
from playwright.sync_api import Page

from pages.today_page import TodayPage
from helpers import helper_for_pages as hp


@pytest.mark.today
def test_navigate_to_today_at_apple(page: Page):
    today = TodayPage(page)

    today.open_today_at_apple()

    heading_text = today.get_header_text()

    hp.assert_page(heading_text, "Today at Apple")


@pytest.mark.today
def test_filter_today_sessions(page: Page):
    today = TodayPage(page)

    today.open_today_at_apple()

    session_visible = today.is_session_visible()

    hp.assert_page(session_visible, True)


@pytest.mark.today
def test_select_store_from_today(page: Page):
    today = TodayPage(page)

    today.open_today_at_apple()

    store_visible = today.is_store_link_visible()

    hp.assert_page(store_visible, True)


@pytest.mark.today
def test_open_today_session_details(page: Page):
    today = TodayPage(page)

    today.open_today_at_apple()

    today.open_session_details()

    heading_visible = today.is_header_visible()

    hp.assert_page(heading_visible, True)


@pytest.mark.today
def test_navigate_to_genius_bar(page: Page):
    today = TodayPage(page)

    today.open_genius_bar()

    heading_text = today.get_header_text()

    hp.assert_page(heading_text, "Genius Bar")


@pytest.mark.today
def test_explore_today_schedule(page: Page):
    today = TodayPage(page)

    today.open_today_at_apple()

    event_visible = today.is_event_visible()

    hp.assert_page(event_visible, True)


@pytest.mark.today
def test_navigate_to_apple_bkc_store(page: Page):
    today = TodayPage(page)

    today.open_bkc_store()

    heading_text = today.get_header_text()

    hp.assert_page(heading_text, "Apple BKC")
    today.take_bkc_screenshot()