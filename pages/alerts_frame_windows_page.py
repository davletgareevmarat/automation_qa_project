import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened(self, open_value):
        value = {
            "tab": self.locators.NEW_TAB_BUTTON,
            "window": self.locators.NEW_WINDOW_BUTTON,
        }
        self.element_is_visible(value[open_value]).click()
        time.sleep(10)
        self.switch_to_window(1)
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

