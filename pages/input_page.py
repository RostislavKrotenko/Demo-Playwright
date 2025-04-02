from pages.base_page import BasePage

class InputPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def navigate(self):
        super().navigate("Text Input")