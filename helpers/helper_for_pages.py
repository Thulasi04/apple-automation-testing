from playwright.sync_api import Page

def open_website(page: Page):
    page.goto("https://www.apple.com/in/")

def assert_page(actual, expected):
    assert actual == expected

def assert_contains(actual, expected):
    assert expected.lower() in actual.lower()