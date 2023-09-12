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


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "#frame1")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, "p")


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "#showSmallModal")
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeSmallModal")
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, ".modal-body")
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, "#example-modal-sizes-title-sm")

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "#showLargeModal")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "#closeLargeModal")
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, ".modal-body")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, "#example-modal-sizes-title-lg")

    CLOSE_BUTTON = (By.CSS_SELECTOR, ".close")
