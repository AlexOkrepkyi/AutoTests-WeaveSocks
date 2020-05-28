import os
from selenium.webdriver.common.by import By


class BasePageLocators:

    # locators
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#numItemsInCart")


class IndexPageLocators:

    # locators
    BASE_LINK = os.environ["BASE_URL"]
    CATALOGUE = (By.CSS_SELECTOR, ".dropdown-toggle")
    FOOTER_PAGES_LI = (By.CSS_SELECTOR, ".col-md-3:nth-child(1) > ul:nth-child(2) > li")
    LOGO = (By.CSS_SELECTOR, ".hidden-xs")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[onclick='return login()']")
    LOGIN_FORM = (By.CSS_SELECTOR, "div[style='display: block; padding-right: 15px;']")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "#login a")
    LOGIN_MESSAGE = (By.CSS_SELECTOR, "#login-message .alert")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#username-modal")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password-modal")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "#register a")
    TAB_CATALOGUE = (By.CSS_SELECTOR, "#tabCatalogue.dropdown")

    # text
    FOOTER_PAGES_LEN = 2
    INVALID_LOGIN_CREDENTIALS_TEXT = "Invalid login credentials."
    LOGIN_SUCCESSFUL_TEXT = "Login successful."

    # size
    LOGO_SIZE = {"height": 50, "width": 248}


class CataloguePageLocators:

    # locators
    ADD_TO_CART = (By.CSS_SELECTOR, "p a.btn.btn-primary")
    PRODUCTS_NUMBER_9 = (By.CSS_SELECTOR, "#products-number :nth-child(4)")
    SOCKS_FIGUEROA = (By.LINK_TEXT, "Figueroa")
    SOCKS_FIGUEROA_PRICE_CATALOGUE_PAGE = (By.CSS_SELECTOR, ".col-md-4:nth-child(5) .price")

    # numbers
    EXPECTED_PRODUCTS_QUANTITY = 9


class DetailsPageLocators:

    # locators
    ADD_TO_CART = (By.CSS_SELECTOR, "#buttonCart")
    SOCKS_FIGUEROA_PRICE_DETAILS_PAGE = (By.CSS_SELECTOR, "#price")


class BasketPageLocators:

    # locators
    ORDER_BUTTON = (By.CSS_SELECTOR, "#orderButton")
    QUANTITY_FIELD = (By.CSS_SELECTOR, "input[type='number']")

    # text
    ALERT_MESSAGE_COULD_NOT_SEND_ORDER = "Could not place order. Missing shipping or payment information."
