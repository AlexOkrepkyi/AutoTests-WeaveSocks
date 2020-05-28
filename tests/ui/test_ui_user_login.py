import time

import pytest

from src.api.user_service_api import UserServiceApi
from src.ui.locators import IndexPageLocators
from src.ui.pages.index_page import IndexPage


def test_user_can_login_with_valid_credentials(driver, fake_user):

    # create user
    UserServiceApi().create_user(fake_user)

    # login user
    link = IndexPageLocators.BASE_LINK
    page = IndexPage(driver, link)
    page.open()
    page.open_login_window()
    page.should_be_login_form()
    page.login_registered_user(fake_user["username"], fake_user["password"])


@pytest.mark.xfail(reason="user _sometimes_ can login with empty 'username' and 'password' fields, should be fixed")
def test_user_cannot_login_with_unfilled_form(driver):

    # try login with empty fields
    link = IndexPageLocators.BASE_LINK
    page = IndexPage(driver, link)
    page.open()
    page.open_login_window()
    page.should_be_login_form()
    page.click_login_button()
    page.is_present_invalid_login_credentials_text()
