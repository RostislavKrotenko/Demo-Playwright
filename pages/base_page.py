class BasePage():
    def __init__(self, page):
        self.page = page
        self.page.goto("http://uitestingplayground.com")

    def navigate(self, page_name):
        self.page.get_by_role("link", name=page_name).click()
    
    def input_text(self, text):
        self.page.get_by_role("textbox", name=text).fill(text)
    
    def click_button(self, button_name):
        self.page.get_by_role("button", name=button_name).click()
    