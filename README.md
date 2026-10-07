# Apple Automation Testing

A web automation testing project for the **Apple India website** using **Python, Playwright, and Pytest**.

The project follows the **Page Object Model (POM)** approach to keep test cases, page interactions, locators, and reusable actions organized separately.

## Technologies Used

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* CSS Selectors
* XPath
* Git & GitHub

## Project Structure

```text
apple-automation-testing/
│
├── tests/
│   ├── test_apple.py
│   ├── test_airpods.py
│   ├── test_iphone.py
│   ├── test_mac.py
│   ├── test_product.py
│   ├── test_search.py
│   ├── test_support.py
│   └── test_today.py
│
├── pages/
│   ├── apple_page.py
│   ├── airpods_page.py
│   ├── iphone_page.py
│   ├── mac_page.py
│   ├── product_page.py
│   ├── search_page.py
│   ├── support_page.py
│   └── today_page.py
│
├── locators/
│   ├── apple_locators.py
│   ├── airpods_locators.py
│   ├── iphone_locators.py
│   ├── mac_locators.py
│   ├── product_locators.py
│   ├── search_locators.py
│   ├── support_locators.py
│   └── today_locators.py
│
├── helpers/
│   ├── helper_for_pages.py
│   └── actions_for_pages.py
│
├── apple_bkc.png
├── airpods_product_page.png
└── README.md
```

## Project Architecture

The project is organized using the **Page Object Model** design pattern.

### Tests

The `tests` folder contains the automated test cases.

Examples:

* `test_apple.py` – Apple website navigation tests
* `test_airpods.py` – AirPods product tests
* `test_iphone.py` – iPhone tests
* `test_mac.py` – Mac tests
* `test_product.py` – Apple Store product tests
* `test_search.py` – Search functionality tests
* `test_support.py` – Apple Support tests
* `test_today.py` – Today at Apple tests

### Pages

The `pages` folder contains page classes and reusable page-level actions.

Examples:

```text
apple_page.py
airpods_page.py
iphone_page.py
mac_page.py
product_page.py
search_page.py
support_page.py
today_page.py
```

This keeps the actual browser interactions separate from the test cases.

### Locators

The `locators` folder contains the selectors used to identify elements on each page.

Examples:

```text
apple_locators.py
airpods_locators.py
iphone_locators.py
mac_locators.py
product_locators.py
search_locators.py
support_locators.py
today_locators.py
```

The project uses selectors such as:

* CSS selectors
* XPath
* ID selectors
* Attribute selectors
* Text-based selectors
* Placeholder selectors

### Helpers

The `helpers` folder contains reusable functions used across the page classes.

```text
helper_for_pages.py
actions_for_pages.py
```

This helps reduce duplicate code and makes common browser actions reusable.

## Test Coverage

### Apple Navigation

* Open Apple India homepage
* Open Apple Store
* Navigate to Mac
* Navigate to iPad
* Navigate to iPhone
* Navigate to Apple Watch
* Navigate to AirPods

### Mac

* Open Mac section
* Open MacBook Air
* Open MacBook Pro
* Verify Buy button visibility
* Open MacBook Air buying page
* Verify Mac color options
* Verify Add to Bag button

### iPhone

* Open iPhone section
* Open iPhone 17
* Open iPhone Air
* Verify Buy button visibility
* Open iPhone buying page
* Verify color options
* Verify storage options

### AirPods

* Open AirPods page
* Verify AirPods product heading
* Open AirPods buying page
* Verify price visibility
* Capture AirPods screenshot

### Apple Store Products

* Open Store page
* Open Mac from Store
* Open iPhone from Store
* Open iPad from Store
* Open Apple Watch from Store

### Search

* Open search bar
* Search for a valid product
* Verify search results
* Verify quick links
* Clear search input
* Search for an invalid product
* Verify search suggestions
* Open shopping bag
* Open sign-in

### Apple Support

* Navigate to Apple Support
* Verify support search box
* Navigate to iPhone repair service
* Navigate to Apple Service and Repair
* Navigate to Apple Support contact

### Today at Apple

* Navigate to Today at Apple
* Filter Today sessions
* Select a store
* Open session details
* Navigate to Genius Bar
* Explore Today schedule
* Navigate to Apple BKC

## Running the Tests

Activate your virtual environment before running the tests.

### Run all tests

```bash
pytest
```

### Run tests with detailed output

```bash
pytest -v
```

### Run tests with the browser visible

```bash
pytest -v --headed
```

### Run a specific test file

```bash
pytest tests/test_airpods.py -v --headed
```

### Run a specific test

```bash
pytest tests/test_airpods.py::test_navigate_to_airpods_page -v --headed
```

## Screenshots

Playwright screenshots are used to capture important pages during test execution.

Example:

```python
page.screenshot(path="airpods_product_page.png", full_page=True)
```

Current project screenshots include:

```text
airpods_product_page.png
apple_bkc.png
```

## Page Object Model Example

A typical test uses a page class instead of placing all browser interactions directly inside the test.

```python
def test_open_mac(page):
    mac_page = MacPage(page)
    mac_page.open_mac()
```

The corresponding page class contains the actual interaction:

```python
class MacPage:

    def __init__(self, page):
        self.page = page

    def open_mac(self):
        self.page.goto("https://www.apple.com/in/mac/")
```

Locators can be maintained separately in the `locators` folder.

This structure makes the automation framework easier to maintain when website elements or selectors change.

## Test Execution

The tests are executed using Pytest with Playwright.

Example:

```bash
pytest -v --headed
```

Pytest reports:

* Passed tests
* Failed tests
* Errors
* Test execution time

## Author

**Thulasi**

B.Tech – Artificial Intelligence & Data Science

## Repository

GitHub Repository:

https://github.com/Thulasi04/apple-automation-testing
