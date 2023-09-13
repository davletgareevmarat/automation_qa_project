from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, "#section1Heading")
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, "#section1Content p")
    SECTION_SECOND = (By.CSS_SELECTOR, "#section2Heading")
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, "#section2Content p")
    SECTION_THIRD = (By.CSS_SELECTOR, "#section3Heading")
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, "#section3Content p")


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "#autoCompleteMultipleInput")
    MULTI_VALUE = (
        By.CSS_SELECTOR,
        'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]',
    )
    MULTI_VALUE_REMOVE = (
        By.CSS_SELECTOR,
        'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path',
    )
    SINGLE_VALUE = (
        By.CSS_SELECTOR,
        'div[class="auto-complete__single-value css-1uccc91-singleValue"]',
    )
    SINGLE_INPUT = (By.CSS_SELECTOR, "#autoCompleteSingleInput")


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "#startStopButton")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
