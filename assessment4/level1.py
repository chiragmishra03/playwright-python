from playwright.sync_api import Page, expect


def handle_dialog(page: Page, action: str, text: str | None = None):
    def _handler(dialog):
        if action == "accept":
            dialog.accept(text) if text else dialog.accept()
        elif action == "dismiss":
            dialog.dismiss()

    page.once("dialog", _handler)


def test_dialogTrainer(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    handle_dialog(page, "accept")
    page.get_by_text("Click for JS Alert").click()
    expect(page.get_by_text("You successfully clicked an alert")).to_be_visible()

    handle_dialog(page, "dismiss")
    page.get_by_text("Click for JS Confirm").click()
    expect(page.get_by_text("You clicked: Cancel")).to_be_visible()

    handle_dialog(page, "accept", "Playwright Hero")
    page.get_by_text("Click for JS Prompt").click()
    expect(page.get_by_text("You entered: Playwright Hero")).to_be_visible()
