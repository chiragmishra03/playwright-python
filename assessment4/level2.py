from playwright.sync_api import Page, expect


def perform_click(action, element):
    if action == "double":
        element.dblclick()
    elif action == "right":
        element.click(button="right")
    else:
        element.click()


def test_mouseNinja(page: Page):
    page.goto("https://demoqa.com/buttons", wait_until="domcontentloaded")

    actions = {
        "double": (
            page.get_by_text("Double Click Me"),
            "You have done a double click"
        ),
        "right": (
            page.get_by_text("Right Click Me"),
            "You have done a right click"
        ),
        "single": (
            page.get_by_text("Click Me", exact=True),
            "You have done a dynamic click"
        ),
    }

    for action, (button, result_text) in actions.items():
        perform_click(action, button)
        expect(page.get_by_text(result_text)).to_be_visible()
