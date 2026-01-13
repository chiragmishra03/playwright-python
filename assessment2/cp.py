from playwright.sync_api import Page, expect

def login(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("checkbox").click()
    page.get_by_role("button").click()

def add_product_to_cart(page: Page, product_name: str):
    card = page.locator("app-card").filter(has_text=product_name)
    card.get_by_role("button").click()

def test_checkoutPage(page: Page):
    login(page)

    phone1 = "iphone X"
    phone2 = "Samsung Note 8"

    add_product_to_cart(page, phone1)
    add_product_to_cart(page, phone2)

    page.get_by_text(" Checkout ( 2 )").click()

    items = page.locator(".media-body")
    names = page.locator(".media-heading")

    expect(items).to_have_count(2)
    expect(names.nth(0)).to_have_text(phone1)
    expect(names.nth(2)).to_have_text(phone2)

    page.get_by_text("Checkout").click()

    page.locator("#country").type("India")
    page.wait_for_selector(".suggestions", state="visible")
    page.locator(".suggestions").click()

    page.get_by_label("I agree with the terms & Conditions").click()
    page.get_by_role("button", name="Purchase").click()
