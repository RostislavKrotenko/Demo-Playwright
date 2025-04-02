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
