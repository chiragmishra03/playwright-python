from playwright.sync_api import Playwright, expect
from assessment5.COAPI import ApiUtils


def inject_token(page, token: str):
    page.add_init_script(
        f"localStorage.setItem('token', '{token}')"
    )


def test_networkIntercept(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = ApiUtils()
    token = api_utils.getToken(playwright)

    inject_token(page, token)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()

    expect(page.get_by_text("Your Orders")).to_be_visible()
