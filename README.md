# Playwright Python Pytest Apple Website Automation Framework

This project is a Python-based UI automation framework built with Playwright and pytest for testing the Apple India website. It follows a Page Object Model (POM) approach to organize test logic, page actions, locators, and reusable helper functions.

The framework is designed to validate Apple website navigation, product pages, search functionality, support pages, and other common end-to-end user actions through automated UI tests.

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM)
- CSS Selectors / XPath
- Apple India Website

## Project Structure

```text
apple-automation-testing/
├── helpers/
│   ├── __init__.py
│   ├── actions_for_pages.py
│   └── helper_for_pages.py
│
├── locators/
│   ├── airpods_locators.py
│   ├── apple_locators.py
│   ├── iphone_locators.py
│   ├── mac_locators.py
│   ├── product_locators.py
│   ├── search_locators.py
│   ├── support_locators.py
│   └── today_locators.py
│
├── pages/
│   ├── airpods_page.py
│   ├── apple_page.py
│   ├── iphone_page.py
│   ├── mac_page.py
│   ├── product_page.py
│   ├── search_page.py
│   ├── support_page.py
│   └── today_page.py
│
├── tests/
│   ├── test_airpods.py
│   ├── test_apple.py
│   ├── test_iphone.py
│   ├── test_mac.py
│   ├── test_product.py
│   ├── test_search.py
│   ├── test_support.py
│   └── test_today.py
│
├── airpods_product_page.png
├── apple_bkc.png
└── README.md
