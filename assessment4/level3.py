from playwright.sync_api import Page, expect


def type_and_tab(page: Page, text: str | None = None):
    if text:
        page.keyboard.type(text)
    page.keyboard.press("Tab")


def test_keyboardWizard(page: Page):
    page.goto("https://www.selenium.dev/selenium/web/web-form.html")

    page.get_by_label("Text input").click()
    page.keyboard.type("johndoe@gmail.com")
    expect(page.locator("#my-text-id")).to_have_value("johndoe@gmail.com")

    type_and_tab(page, "Password")
    type_and_tab(page, "Hello World!!!")

    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")

    for _ in range(8):
        page.keyboard.press("Tab")

    page.keyboard.press("Enter")
    expect(page.get_by_text("Received!")).to_be_visible()
