import pytest
from random import randint
from faker import Faker
from selenium import webdriver

from src.ui.locators import IndexPageLocators


@pytest.fixture
def faker():
    faker = Faker()
    return faker


@pytest.fixture
def fake_user():
    faker = Faker()
    user = {"username": faker.name(), "password": faker.password(), "email": faker.email()}
    return user


@pytest.fixture()
def wrong_card_number():
    number = randint(100000000000000, 999999999999999)
    return str(number)


@pytest.fixture()
def driver():
    print("\n--- start driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("\n--- quit driver ---")
    driver.quit()


@pytest.fixture()
def driver_index_page():
    print("\n--- start driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(IndexPageLocators.BASE_LINK)  # link to the indicated page
    yield driver
    print("\n--- quit driver ---")
    driver.quit()
