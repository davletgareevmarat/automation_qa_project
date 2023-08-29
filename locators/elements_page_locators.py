from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT = (By.CSS_SELECTOR, "#submit")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, ".rct-title")
    CHECKED_ITEMS = (By.CSS_SELECTOR, ".rct-icon-check")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, ".text-success")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (
        By.CSS_SELECTOR,
        'label[class^="custom-control"][for="yesRadio"]',
    )
    IMPRESSIVE_RADIOBUTTON = (
        By.CSS_SELECTOR,
        'label[class^="custom-control"][for="impressiveRadio"]',
    )
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


class ButtonsPageLocators:
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    # result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, "#doubleClickMessage")
    SUCCESS_RIGHT = (By.CSS_SELECTOR, "#rightClickMessage")
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, "#dynamicClickMessage")


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "#simpleLink")
    BAD_REQUEST = (By.CSS_SELECTOR, "#bad-request")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "#uploadFile")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "#uploadedFilePath")

    DOWNLOAD_FILE = (By.CSS_SELECTOR, "#downloadButton")


class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "#colorChange")
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "#visibleAfter")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "#enableAfter")
