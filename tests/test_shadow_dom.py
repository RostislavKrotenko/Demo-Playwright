from playwright.sync_api import Page, expect

def test_shadow_dom(page: Page):
    page.goto("http://uitestingplayground.com")

    page.get_by_role("link", name="Shadow DOM").click()
    page.locator("#buttonGenerate").click()
    page.locator("#buttonCopy").click()

    print(page.query_selector("#buttonCopy"))