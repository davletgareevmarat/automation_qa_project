import time

import pytest
import random

from pages.elements_page import (
    TextBoxPage,
    CheckBoxPage,
    RadioButtonPage,
    WebTablePage,
    ButtonsPage,
)


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "Input data does not match output data"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox(25)
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_checked_checkboxes()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        @pytest.mark.xfail(raises=AssertionError)
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(
                driver, "https://demoqa.com/radio-button"
            )
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("no")
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "'Yes' have not been selected"
            assert (
                output_impressive == "Impressive"
            ), "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_persons = web_table_page.add_new_person(random.randint(1, 4))
            table_result = web_table_page.check_new_added_person()

            for person in new_persons:
                assert person in table_result, '"New person does not created correctly"'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0][random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            time.sleep(5)
            table_result = web_table_page.check_search_person()
            time.sleep(5)
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0][random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0][random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.remove_footer()

            count = web_table_page.select_up_to_some_rows()
            assert count == [
                5,
                10,
                20,
                25,
                50,
                100,
            ], "The number of rows in the table has not been changed or has changed incorrectly"

    class TestButtonsPage:
        def test_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            click_text = button_page.click_on_button()
            assert (
                click_text == "You have done a dynamic click"
            ), "The dynamic click button was not pressed"

        def test_double_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.double_click_on_button()
            double_click_text = button_page.click_on_different_button("double")
            assert (
                double_click_text == "You have done a double click"
            ), "The double click button was not pressed"

        def test_right_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.right_click_on_button()
            right_click_text = button_page.click_on_different_button("right")
            assert (
                right_click_text == "You have done a right click"
            ), "The right click button was not pressed"
