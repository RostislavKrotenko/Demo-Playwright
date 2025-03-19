import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://uitestingplayground.com")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("UI Test Automation"))

def test_get_started_link(page: Page):
    page.goto("http://uitestingplayground.com")

    # Click the link.
    page.get_by_role("link", name="Dynamic ID").click()

    # Expects page to have a heading with the name of Dynamic ID.
    expect(page.get_by_role("heading", name="Dynamic ID")).to_be_visible()

def test_auto_waiting(page: Page):
    # page.context.tracing.start(screenshots=True, snapshots=True)

    page.goto("http://uitestingplayground.com")

    page.get_by_role("link", name="Auto Wait").click()
    page.get_by_role("button", name="Apply 10s").click()
    page.get_by_role("button", name="Button").click()

    # page.context.tracing.stop(path='trace.zip')

def test_child_elements_location(page: Page):
    page.goto("http://uitestingplayground.com")
    page.get_by_role("link", name="Alert").click()

    # more common syntax
    page.locator('.container #alertButton').click()

    # chaining locators
    page.locator('.container').locator('#alertButton').click()
    
    # mixed type of finding locators
    page.locator('.container').get_by_role('button', name='Alert').click()

def test_filtering_elements(page: Page):
    page.goto("http://uitestingplayground.com")
    page.get_by_role("link", name="Alert").click()

    # finding parent element by presence of specific text inside
    page.locator('div', has_text='Playground').get_by_role('button', name="Alert").click()

    # finding parent element by presence of specific locator inside
    page.locator('div', has=page.locator('#alertButton')).get_by_role('button', name='Alert').click()

    # same as previous one
    page.locator('div').filter(has_text='Alert').get_by_role('button', name='Alert').click()