import time

import allure
import pytest
import random

from pages.elements_page import (
    TextBoxPage,
    CheckBoxPage,
    RadioButtonPage,
    WebTablePage,
    ButtonsPage,
    LinksPage,
    UploadAndDownloadPage,
    DynamicPropertiesPage,
)


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "Input data does not match output data"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox(25)
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_checked_checkboxes()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check RadioButton")
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

    @allure.feature("WebTable")
    class TestWebTable:
        @allure.title("Сheck to add a person to the table")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_persons = web_table_page.add_new_person(random.randint(1, 4))
            table_result = web_table_page.check_new_added_person()

            for person in new_persons:
                assert person in table_result, '"New person does not created correctly"'

        @allure.title("Check human search in table")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0][random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            time.sleep(5)
            table_result = web_table_page.check_search_person()
            time.sleep(5)
            assert key_word in table_result, "the person was not found in the table"

        @allure.title("Checking to update the persons info in the table")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0][random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        @allure.title("Checking to remove a person from the table")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[0][random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        @allure.title("Check the change in the number of rows in the table")
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

    @allure.feature("Buttons page")
    class TestButtonsPage:
        @allure.title("Checking left click on the buttons")
        def test_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            click_text = button_page.click_on_button()
            assert (
                click_text == "You have done a dynamic click"
            ), "The dynamic click button was not pressed"

        @allure.title("Checking double click on the buttons")
        def test_double_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.double_click_on_button()
            double_click_text = button_page.double_click_on_button()
            assert (
                double_click_text == "You have done a double click"
            ), "The double click button was not pressed"

        @allure.title("Checking right click on the buttons")
        def test_right_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            button_page.right_click_on_button()
            right_click_text = button_page.right_click_on_button()
            assert (
                right_click_text == "You have done a right click"
            ), "The right click button was not pressed"

    class TestLinksPage:
        @allure.title("Checking the link")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        @allure.title("Checking the broken link")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_broken_link(
                "https://demoqa.com/bad-request"
            )
            assert response_code == 400, "the link works or the status code != 400"

    @allure.feature("Upload and Download page")
    class TestUploadAndDownload:
        @allure.title("Check upload file")
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(
                driver, "https://demoqa.com/upload-download"
            )
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "the file has not been uploaded"

        @allure.title("Check download file")
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(
                driver, "https://demoqa.com/upload-download"
            )
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "the file has not been downloaded"

    @allure.feature("Dynamic properties page")
    class TestDynamicPropertiesPage:
        @allure.title("Check dynamic properties")
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, "https://demoqa.com/dynamic-properties"
            )
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, "colors have not been changed"

        @allure.title("Check appear button")
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, "https://demoqa.com/dynamic-properties"
            )
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, "button did not appear after 5 second"

        @allure.title("Check enable button")
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, "https://demoqa.com/dynamic-properties"
            )
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "button did not enable after 5 second"
