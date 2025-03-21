from playwright.sync_api import Page, expect

def test_should_fail(page: Page):
    page.goto("http://uitestingplayground.com")

    page.get_by_role('link', name='Dynamic IDs').click()