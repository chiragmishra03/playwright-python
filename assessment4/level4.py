from playwright.sync_api import Page, expect


def clear_and_type(page: Page, element, text: str):
    element.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    page.keyboard.type(text)


def test_frameBreaker(page: Page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    editor = page.frame_locator("#mce_0_ifr").locator("body")

    clear_and_type(page, editor, "I rule the frames")

    expect(editor).to_have_text("I rule the frames")
