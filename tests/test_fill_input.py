from playwright.sync_api import Page, expect

def test_fill_input(page: Page):
    page.goto("http://uitestingplayground.com")
    page.get_by_role("link", name="Text Input").click()

    new_button_name = "NewButton"
    button = page.get_by_role("button")

    page.get_by_role("textbox", name="Set New Button Name").fill(new_button_name)
    button.click()

    expect(button).to_contain_text(new_button_name)
    