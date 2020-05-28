import pytest

from src.api.conditions import status_code
from src.api.user_service_api import UserServiceApi


@pytest.mark.cards
def test_user_can_add_card(faker, fake_user):
    resp = UserServiceApi().create_user(fake_user)
    user_id = resp.get_field("id")

    user_card = {"longNum": faker.credit_card_number(), "expires": faker.credit_card_expire(),
                 "ccv": faker.credit_card_security_code(), "userID": f"{user_id}"}

    resp = UserServiceApi().create_user_card(user_card)
    resp.should_have(status_code(200))


@pytest.mark.xfail(reason="'card' field should take only long card numbers with 16 digits")
def test_user_card_should_be_16_digits_long(faker, fake_user, wrong_card_number):
    resp = UserServiceApi().create_user(fake_user)
    user_id = resp.get_field("id")

    user_card = {"longNum": wrong_card_number, "expires": faker.credit_card_expire(),
                 "ccv": faker.credit_card_security_code(), "userID": f"{user_id}"}

    resp = UserServiceApi().create_user_card(user_card)
    resp.should_have(status_code(400))
