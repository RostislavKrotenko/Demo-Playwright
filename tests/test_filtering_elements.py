from playwright.sync_api import Page, expect

def test_filtering_elements(page: Page):
    page.goto("http://uitestingplayground.com")
    page.get_by_role("link", name="Alert").click()

    # finding parent element by presence of specific text inside
    page.locator('div', has_text='Playground').get_by_role('button', name="Alert").click()

    # finding parent element by presence of specific locator inside
    page.locator('div', has=page.locator('#alertButton')).get_by_role('button', name='Alert').click()

    # same as previous one
    page.locator('div').filter(has_text='Alert').get_by_role('button', name='Alert').click()