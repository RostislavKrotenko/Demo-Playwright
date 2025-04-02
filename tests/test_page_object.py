from pages.input_page import InputPage

def test_page_object(page):
    input_page = InputPage(page)
    input_page.navigate()
    input_page.input_text("Set New Button Name")
    input_page.click_button("Button That Should Change it's Name Based on Input Value")

    

    

