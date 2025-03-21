from playwright.sync_api import Page, expect

def test_auto_waiting(page: Page):
    # page.context.tracing.start(screenshots=True, snapshots=True)

    page.goto("http://uitestingplayground.com")

    page.get_by_role("link", name="Auto Wait").click()
    page.get_by_role("button", name="Apply 3s").click()
    page.get_by_role("button", name="Button").click()

    # page.context.tracing.stop(path='trace.zip')