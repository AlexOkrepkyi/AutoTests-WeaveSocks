import time

import pytest

from src.api.user_service_api import UserServiceApi
from src.ui.locators import IndexPageLocators, CataloguePageLocators, DetailsPageLocators
from src.ui.pages.basket_page import BasketPage
from src.ui.pages.catalogue_page import CataloguePage
from src.ui.pages.details_page import DetailsPage
from src.ui.pages.index_page import IndexPage


@pytest.mark.E2E
def test_e2e_user_can_add_figueroa_socks_to_basket(driver, fake_user):

    # create user
    UserServiceApi().create_user(fake_user)

    # login user
    link = IndexPageLocators.BASE_LINK
    page_login = IndexPage(driver, link)
    page_login.open()
    page_login.open_login_window()
    page_login.should_be_login_form()
    page_login.login_registered_user(fake_user["username"], fake_user["password"])
    page_login.go_to_catalogue()

    # switch to catalogue page
    page_catalogue = CataloguePage(driver, url=driver.current_url)
    page_catalogue.select_9_products_per_page()
    page_catalogue.verify_all_9_products_are_present()
    page_catalogue.go_to_figueroa_socks()

    # switch to details page
    page_details = DetailsPage(driver, url=driver.current_url)
    page_details.add_item_to_cart()
    page_details.go_to_basket()

    # switch to basket page
    page_basket = BasketPage(driver, url=driver.current_url)
    page_basket.verify_quantity_is_one()
    page_basket.proceed_to_checkout()
    page_basket.verify_is_present_alert_message_order_not_placed()
