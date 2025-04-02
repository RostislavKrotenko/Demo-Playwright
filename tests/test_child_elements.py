from playwright.sync_api import Page, expect

def test_child_elements_location(page: Page):
    page.goto("http://uitestingplayground.com")
    page.get_by_role("link", name="Alert").click()

    # more common syntax
    page.locator('.container #alertButton').click()

    # chaining locators
    page.locator('.container').locator('#alertButton').click()
    
    # mixed type of finding locators
    page.locator('.container').get_by_role('button', name='Alert').click()