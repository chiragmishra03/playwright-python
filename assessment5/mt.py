from playwright.sync_api import Playwright, expect
from assessment5.COAPI import ApiUtils


FAKE_ORDER_RESPONSE = {
    "data": [],
    "message": "No Orders"
}


def intercept_empty_orders(route):
    route.fulfill(json=FAKE_ORDER_RESPONSE)


def login(page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("Shubhamlambha.1996@gmail.com")
    page.locator("#userPassword").fill("Shubh123")
    page.locator("#login").click()


def test_createOrder(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
        intercept_empty_orders
    )

    login(page)

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="HELP").click()

    expect(
        page.locator("div.mt-4.ng-star-inserted")
    ).to_have_text(
        "You have No Orders to show at this time. Please Visit Back Us"
    )
