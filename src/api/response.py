import logging
import allure


class AssertableResponse:

    def __init__(self, response):
        self._response = response
        logging.info(f"Request: {response.request.body}")
        logging.info(f"Response: {response.json()}")

    @allure.step("then API response should have {1}")  # {1} means it tales 1st parameter as a string
    def should_have(self, condition):
        condition.match(self._response)
        return self  # why returning self?

    @allure.step("then get body field {1}")
    def get_field(self, name):
        return self._response.json()[name]
