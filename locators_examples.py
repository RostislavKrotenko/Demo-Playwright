from playwright.sync_api import Page

def test_locators(page: Page):
    
    tag = page.locator('div')

    id = page.locator('#new-id')

    class_ui = page.locator('.some-class')

    attribute = page.locator('[placeholder="MyButton"]')

    # without whitespaces
    combined = page.locator('div[placeholder="MyButton"][class="some-class"]')

    # NOT RECOMMENDED 
    xpath = page.locator('//*[@id="some-id"]')

    partial_text = page.locator(':text("Some text")')

    exact_text = page.locator(':text-is("Some text you want to find")')



