from playwright.sync_api import Page


class TestAppleNavigation:

    def test_navigate_to_apple_india(self, page: Page):
        page.goto("https://www.apple.com/in/")
        assert page.title() == "Apple (India)"

    def test_navigate_to_store(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('//a[@data-analytics-title="store"]').first.click()
        heading = page.locator('//h1[text()="Store"]').text_content()
        assert heading == "Store"

    def test_navigate_to_mac(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        heading = page.locator('//span[text()="Mac"]').nth(1).text_content()
        assert heading == "Mac"

    def test_navigate_to_ipad(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('//a[@data-analytics-title="ipad"]').nth(1).click()
        heading = page.locator('//h1//span[text()="iPad"]').text_content()
        assert heading == "iPad"

    def test_navigate_to_iphone(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('//span[text()="iPhone"]').click()
        heading = page.locator('//h1[text()="iPhone"]').text_content()
        assert heading == "iPhone"

    def test_navigate_to_watch(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('//a[@data-analytics-title="watch"]').first.click()
        heading = page.locator('h1[class*="PageHeader_title"]').text_content()
        assert heading == "Apple Watch"

    def test_navigate_to_airpods(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[href="/in/airpods/"]').first.click()
        assert page.url == "https://www.apple.com/in/airpods/"


class TestSearch:

    def test_open_search_bar(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-search"]').click()
        search_box = page.locator('input[placeholder="Search apple.com"]')
        search_box.fill("AppleCare+ for Apple TV")
        search_box.press("Enter")
        page.locator('a[data-relatedlink]').click()
        heading = page.locator('h1[class="rf-pdp-title"]').text_content()
        assert heading == "AppleCare+ for Apple TV"

    def test_search_valid_product(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-search"]').click()
        search_box = page.locator('input[placeholder="Search apple.com"]')
        search_box.fill("MacBook Pro")
        search_box.press("Enter")
        page.wait_for_load_state("domcontentloaded")
        assert "search" in page.url

    def test_search_quick_links_visibility(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-search"]').click()
        quick_link = page.locator('h2[class="globalnav-searchresults-header"]').first
        assert quick_link.text_content() == "Quick Links"

    def test_search_clear_input(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-search"]').click()
        search_box = page.locator('input[placeholder="Search apple.com"]')
        search_box.fill("iPhone")
        page.locator('button[class="globalnav-searchfield-reset"]').click()
        assert search_box.input_value() == ""

    def test_search_invalid_product(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-search"]').click()
        search_box = page.locator('input[placeholder="Search apple.com"]')
        search_box.fill("xyznonexistentproduct999")
        page.keyboard.press("Enter")
        page.wait_for_load_state("networkidle")
        assert "search" in page.url

    def test_search_suggestions_appear(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-search"]').click()
        search_box = page.locator('input[placeholder="Search apple.com"]')
        search_box.fill("Watch")
        suggestions_panel = page.locator('div[class="globalnav-searchresults-container"]').first
        assert suggestions_panel.is_visible()

    def test_open_shopping_bag_dropdown(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-bag"]').click()
        heading = page.locator('h2[class="globalnav-flyout-item ac-gn-bagview-header"]').text_content()
        assert heading == "Your Bag is empty."

    def test_open_sign_in(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[id="globalnav-menubutton-link-bag"]').click()
        sign_in = page.locator('span[class="ac-gn-bagview-nav-text"]').nth(3).text_content()
        assert sign_in == "Sign in"


class TestProductShopping:

    def test_navigate_to_mac_buy_page(self, page: Page):
        page.goto("https://www.apple.com/in/shop/buy-mac")
        heading = page.locator("h1").first.text_content()
        assert heading == "Shop Mac"

    def test_check_iphone_tech_specs(self, page: Page):
        page.goto("https://www.apple.com/in/iphone/")
        page.locator('a[href*="/specs/"]').first.click()
        assert "specs" in page.url

    def test_check_applecare_info_page(self, page: Page):
        page.goto("https://www.apple.com/in/support/products/")
        heading = page.locator("h1").first.text_content()
        assert "AppleCare" in heading

    def test_check_store_free_delivery_banner(self, page: Page):
        page.goto("https://www.apple.com/in/store")
        banner = page.locator("text=/Free delivery|Free shipping/i").first
        assert banner.is_visible()

    def test_navigate_to_accessories_section(self, page: Page):
        page.goto("https://www.apple.com/in/shop/goto/buy_accessories")
        heading = page.locator("h1").first.text_content()
        assert "Accessories" in heading


class TestTodayAtApple:

    def test_navigate_to_today_at_apple(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[href*="/today/"]').first.click()
        page.wait_for_load_state("networkidle")
        heading = page.locator("h1").first.text_content().strip()
        assert heading == "Today at Apple"

    def test_filter_today_sessions(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[href*="/today/"]').first.click()
        page.wait_for_load_state("networkidle")
        session_card = page.locator('a[href*="/today/event/"], a[href*="event"]').first
        session_card.scroll_into_view_if_needed()
        assert session_card.is_visible()

    def test_select_store_from_today(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[href*="/today/"]').first.click()
        page.wait_for_load_state("networkidle")
        store_link = page.locator('footer a[href*="/retail/"]').first
        store_link.scroll_into_view_if_needed()
        assert store_link.is_visible()

    def test_open_today_session_details(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[href*="/today/"]').first.click()
        page.wait_for_load_state("networkidle")
        session_link = page.locator('a[href*="/today/event/"], a[href*="event"]').first
        session_link.scroll_into_view_if_needed()
        session_link.click(force=True)
        page.wait_for_load_state("networkidle")
        assert page.locator("h1").first.is_visible()

    def test_navigate_to_genius_bar(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('footer a[href*="geniusbar"]').first.click()
        page.wait_for_load_state("networkidle")
        heading = page.locator("h1").first.text_content().strip()
        assert heading == "Genius Bar"

    def test_explore_today_schedule(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[href*="/today/"]').first.click()
        page.wait_for_load_state("networkidle")
        event_card = page.locator('a[href*="event"]').first
        assert event_card.is_visible()

    def test_navigate_to_apple_bkc_store(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('footer a[href*="/retail/"]').first.click()
        page.wait_for_load_state("networkidle")
        page.goto("https://www.apple.com/in/retail/bkc/")
        heading = page.locator("h1").first.text_content().strip()
        page.screenshot(path="apple_bkc.png")
        assert heading == "Apple BKC"


class TestAppleSupport:

    def test_navigate_to_apple_support(self, page: Page):
        page.goto("https://support.apple.com/en-in")
        heading = page.locator("h1").first
        assert heading.is_visible()
        assert heading.text_content().strip() == "Apple Support"

    def test_support_search_box_visibility(self, page: Page):
        page.goto("https://support.apple.com/en-in")
        search_button = page.get_by_role("button", name="Search")
        assert search_button.is_visible()
        search_button.click()
        search_box = page.locator('div[id="as-search-text-box"]').first
        assert search_box.is_visible()

    def test_navigate_to_iphone_repair_service(self, page: Page):
        page.goto("https://support.apple.com/en-in/iphone/repair")
        assert page.locator("body").is_visible()
        assert "iphone" in page.url
        assert "repair" in page.url

    def test_navigate_to_apple_service_repair(self, page: Page):
        page.goto("https://support.apple.com/en-in/repair")
        assert page.locator("body").is_visible()
        assert "support.apple.com" in page.url

    def test_navigate_to_apple_support_contact(self, page: Page):
        page.goto("https://support.apple.com/en-in/contact")
        assert page.locator("body").is_visible()
        assert "support.apple.com" in page.url


class TestMac:

    def test_open_mac_section(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        heading = page.locator("h1").first.text_content()
        assert "Mac" in heading

    def test_open_macbook_air(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.locator('a[data-analytics-title*="macbook air"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        assert "macbook-air" in page.url

    def test_open_macbook_pro(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.locator('a[data-analytics-title*="macbook pro"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        assert "macbook-pro" in page.url

    def test_mac_buy_button_visibility(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.locator('a[data-analytics-title*="macbook air"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        buy_button = page.get_by_text("Buy", exact=True).first
        assert buy_button.is_visible()

    def test_open_macbook_air_buy_page(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.locator('a[data-analytics-title*="buy - macbook air"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        assert "buy" in page.url

    def test_mac_colors_visibility(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.locator('a[data-analytics-title*="macbook air"]').nth(1).click()
        page.wait_for_load_state("domcontentloaded")
        color_option = page.get_by_text("Sky Blue", exact=True).first
        assert color_option.is_visible()

    def test_mac_add_to_bag_button(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="mac"]').first.click()
        page.locator('a[data-analytics-title*="buy - macbook air"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        assert page.locator("body").is_visible()
        assert "buy-mac" in page.url


class TestIPhone:

    def test_open_iphone_section(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        heading = page.locator("h1").first.text_content()
        assert "iPhone" in heading

    def test_open_iphone_17(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.locator('a[data-analytics-title="iphone 17"]').nth(1).click()
        page.wait_for_load_state("domcontentloaded")
        assert "iphone-17" in page.url

    def test_open_iphone_air(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.locator('a[data-analytics-title*="iphone air"]').nth(1).click()
        page.wait_for_load_state("domcontentloaded")
        assert "iphone-air" in page.url

    def test_iphone_buy_button_visibility(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.locator('a[data-analytics-title="iphone 17"]').nth(1).click()
        page.wait_for_load_state("domcontentloaded")
        buy_button = page.get_by_text("Buy", exact=True).first
        assert buy_button.is_visible()

    def test_open_iphone_buy_page(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.locator('a[data-analytics-title*="buy - iphone 17"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        assert "shop/buy-iphone" in page.url

    def test_iphone_color_selection(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.locator('a[data-analytics-title="iphone 17"]').nth(1).click()
        page.locator('a[href="/in/shop/goto/buy_iphone/iphone_17"]').nth(3).click()
        page.wait_for_load_state("domcontentloaded")
        color_option = page.locator('img[class="colornav-swatch"]').first
        assert color_option.is_visible()

    def test_iphone_storage_options(self, page: Page):
        page.goto("https://www.apple.com/in/")
        page.locator('a[data-globalnav-item-name="iphone"]').first.click()
        page.locator('a[data-analytics-title*="buy - iphone 17"]').first.click()
        page.wait_for_load_state("domcontentloaded")
        storage_option = page.locator('input[type="radio"]').first
        assert storage_option.is_visible()


class TestAirPods:

    def test_navigate_to_airpods_page(self, page: Page):
        page.goto("https://www.apple.com/in/airpods/")
        airpods_link = page.locator('a[href="/in/airpods/"]').first
        airpods_link.wait_for(state="visible")
        airpods_link.click()
        page.wait_for_load_state("domcontentloaded")
        assert "/in/airpods/" in page.url

    def test_verify_airpods_product_heading(self, page: Page):
        page.goto("https://www.apple.com/in/airpods/")
        page.wait_for_load_state("domcontentloaded")
        heading = page.locator("h1").first
        heading.wait_for(state="visible")
        assert "AirPods" in heading.text_content().strip()

    def test_open_airpods_buying_page(self, page: Page):
        page.goto("https://www.apple.com/in/airpods/")
        page.wait_for_load_state("domcontentloaded")
        buy_button = page.get_by_role("link", name="Buy").first
        buy_button.wait_for(state="visible")
        buy_button.click()
        page.wait_for_load_state("domcontentloaded")
        assert "shop" in page.url

    def test_verify_airpods_price_visibility(self, page: Page):
        page.goto("https://www.apple.com/in/shop/airpods/accessories")
        page.wait_for_load_state("domcontentloaded")
        price = page.get_by_text("₹", exact=False).first
        price.wait_for(state="visible")
        assert price.is_visible()

    def test_take_airpods_screenshot(self, page: Page):
        page.goto("https://www.apple.com/in/airpods/")
        page.wait_for_load_state("domcontentloaded")
        heading = page.locator("h1").first
        heading.wait_for(state="visible")
        page.screenshot(path="airpods_product_page.png", full_page=True)
        assert heading.is_visible()