from playwright.sync_api import Page, expect

def test_example_domain_page(page: Page):
    page.goto("https://example.com/")

    title = page.title()
    heading = page.locator("h1")
    description = page.get_by_text(
        "This domain is for use in documentation examples without needing permission."
    )

    expect(title).to_be("Example Domain")
    expect(heading).to_have_text("Example Domain")
    expect(description).to_contain_text(
        "documentation examples without needing permission"
    )
    expect(page).not_to_have_title("Wrong Title")
