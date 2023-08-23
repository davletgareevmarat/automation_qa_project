import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            print(input_data)
            print(output_data)
            assert input_data == output_data, "Input data does not match output data"
