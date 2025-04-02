from playwright.sync_api import Page, expect
import re

def test_should_fail(page: Page):
    page.goto("http://uitestingplayground.com")

    page.get_by_role('link', name='Sample App').click()

    label = page.locator('#loginstatus')
    expect(label).to_contain_text('logged out')

    page.fill('[name="UserName"]', 'Rostyslav')
    page.fill('[name="Password"]', '12345678')
    page.get_by_role('button', name='Log In').click()

    expect(label).to_contain_text('fdasdfas')
