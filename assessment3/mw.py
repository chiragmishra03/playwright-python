import time
from playwright.sync_api import Page, expect


def open_and_validate_popup(page: Page, link_text: str, expected_title: str, expected_url: str):
    with page.expect_popup() as popup:
        page.get_by_role("link", name=link_text).click()

    popup_page = popup.value
    popup_page.bring_to_front()

    expect(popup_page).to_have_title(expected_title)
    expect(popup_page).to_have_url(expected_url)

    return popup_page


def test_multipleWindows(playwright):
    browser = playwright.chromium.launch(headless=False)

    context1 = browser.new_context()
    page = context1.new_page()

    page.goto("https://www.hdfc.bank.in/")
    expect(page).to_have_title("Personal Banking & Netbanking Services | HDFC Bank")
    expect(page).to_have_url("https://www.hdfc.bank.in/")

    open_and_validate_popup(
        page,
        "Personal Loan",
        "Get Instant Personal Loan Online Starting 9.99% | HDFC Bank",
        "https://www.hdfc.bank.in/personal-loan?icid=website_organic_footer_coreproducts:link:personalloan"
    )

    open_and_validate_popup(
        page,
        "Car Loan",
        "Car Loan Online - Apply New Car Loan & Get up to 100% Funding | HDFC Bank",
        "https://www.hdfc.bank.in/car-loan?icid=website_organic_footer_coreproducts:link:carloan"
    )

    open_and_validate_popup(
        page,
        "Business Loan",
        "Apply for Business Loan Online at Lowest Interest Rate | HDFC Bank",
        "https://www.hdfc.bank.in/business-loan?icid=website_organic_footer_coreproducts:link:businessloan"
    )

    open_and_validate_popup(
        page,
        "Gold Loan",
        "Gold Loan - Apply Loan Against Gold Online in India | HDFC Bank",
        "https://www.hdfc.bank.in/gold-loan?icid=website_organic_footer_coreproducts:link:goldloan"
    )

    # Print titles of all pages in first context
    for p in context1.pages:
        print(p.title())

    # Open a new browser window (new context)
    context2 = browser.new_context()
    new_page = context2.new_page()
    new_page.goto("https://www.google.com/")
    time.sleep(2)
    new_page.close()

    page.close()
    browser.close()
