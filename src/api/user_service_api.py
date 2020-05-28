import json

import allure
import requests
from src.api.base_service_api import BaseServiceApi
from src.api.response import AssertableResponse


class UserServiceApi(BaseServiceApi):

    @allure.step
    def create_user(self, user):
        return AssertableResponse(requests.post(url=self._base_url + "/register",
                                                data=json.dumps(user),  # 'dumps' converts 'dict' type to 'str' type
                                                headers=self._headers))

    @allure.step
    def delete_user(self, user_id):
        return AssertableResponse(requests.delete(url=self._base_url + f"/customers/{user_id}",
                                                  headers=self._headers))

    # for some reason user card is not posting, though all the data are being send in the valid format;
    # 4 cards are already existing, their quantity doesn't change
    @allure.step
    def create_user_card(self, user_card):
        return AssertableResponse(requests.post(url=self._base_url + "/cards",
                                                data=json.dumps(user_card),
                                                headers=self._headers))

    # for some reason user address is not posting, though all the data are being send in the valid format
    # 4 cards are already existing, their quantity doesn't change
    @allure.step
    def create_user_address(self, user_address):
        return AssertableResponse(requests.post(url=self._base_url + "/addresses",
                                                data=json.dumps(user_address),
                                                headers=self._headers))

    @allure.step
    def get_total_number_of_users_in_database(self):
        return len(requests.get(url=self._base_url + "/customers").json()["_embedded"]["customer"])

    @allure.step
    def get_total_number_of_user_addresses_in_database(self):
        return len(requests.get(url=self._base_url + "/addresses").json()["_embedded"]["address"])

    @allure.step
    def get_total_number_of_user_cards_in_database(self):
        return len(requests.get(url=self._base_url + "/cards").json()["_embedded"]["card"])

    @allure.step
    def get_user_by_id(self, user_id):
        return AssertableResponse(requests.get(url=self._base_url + f"/customers/{user_id}"))

    @allure.step
    def get_user_address_by_id(self, user_id):
        return AssertableResponse(requests.get(url=self._base_url + f"/addresses/{user_id}"))

    @allure.step
    def verify_number_of_users_in_database_increases_after_new_registration(self, fake_user):
        # total current users in database before
        users_before = UserServiceApi().get_total_number_of_users_in_database()

        # create new user
        UserServiceApi().create_user(fake_user)

        # total current users in database after
        users_after = UserServiceApi().get_total_number_of_users_in_database()
        assert users_after == users_before + 1, f"\n--- {users_after} != {users_before + 1} ---"
