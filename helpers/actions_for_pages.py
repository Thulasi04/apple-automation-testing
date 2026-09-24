from playwright.sync_api import Page

def click_action(page: Page, selector):
    page.locator(selector).click()

def type_action(page: Page, selector, value):
    page.locator(selector).fill(value)

def get_text_action(page: Page, selector):
    return page.locator(selector).text_content()

def get_title_action(page: Page):
    return page.title()