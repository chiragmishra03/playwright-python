from playwright.sync_api import Playwright, expect
from assessment5.COAPI import ApiUtils


def login(page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()


def test_createOrder(playwright: Playwright):
    api_utils = ApiUtils()
    order_id = api_utils.createOrder(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login(page)

    page.get_by_role("button", name="ORDERS").click()
    order_row = page.locator("tr").filter(has_text=order_id)

    expect(order_row).to_be_visible()
    page.wait_for_timeout(2000)
