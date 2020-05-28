import pytest

from src.ui.locators import IndexPageLocators
from src.ui.pages.index_page import IndexPage


def test_is_present_tab_catalogue(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_is_present_tab_catalogue()


def test_is_present_log_in_form_button(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_is_present_log_in_form_button()


def test_is_present_register_form_button(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_is_present_register_button()


def test_is_present_logo(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_is_present_logo()


@pytest.mark.verify_size
def test_logo_has_expected_height(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_logo_has_expected_height()


@pytest.mark.verify_size
def test_verify_logo_has_expected_width(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_logo_has_expected_width()


@pytest.mark.footer
def test_verify_footer_pages_has_expected_number_of_elements(driver):
    link = IndexPageLocators.BASE_LINK
    index_page = IndexPage(driver, link)
    index_page.open()
    index_page.verify_footer_pages_has_expected_number_of_elements()