from playwright.sync_api import Page, expect

def test_auto_waiting(page: Page):
    # page.context.tracing.start(screenshots=True, snapshots=True)

    page.goto("http://uitestingplayground.com")

    page.get_by_role("link", name="Auto Wait").click()
    page.get_by_role("button", name="Apply 10s").click()
    page.get_by_role("button", name="Button").click()

    # page.context.tracing.stop(path='trace.zip')

def test_page_loading(page: Page):
    page.goto("http://uitestingplayground.com")

    page.get_by_role("link", name="Load Delay").click()
    expect(page.get_by_role("button")).to_contain_text("Button Appearing After Delay")
