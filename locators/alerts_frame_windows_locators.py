from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")
    TITLE_NEW = (By.CSS_SELECTOR, "#sampleHeading")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "#alertButton")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, "#timerAlertButton")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "#confirmButton")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "#confirmResult")
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "#promtButton")
    PROMPT_RESULT = (By.CSS_SELECTOR, "#promptResult")


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "#frame1")
    SECOND_FRAME = (By.CSS_SELECTOR, "#frame2")
    TITLE_FRAME = (By.CSS_SELECTOR, "#sampleHeading")
