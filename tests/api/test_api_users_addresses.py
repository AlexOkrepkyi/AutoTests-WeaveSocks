from src.api.conditions import status_code
from src.api.user_service_api import UserServiceApi


def test_user_can_post_address(faker, fake_user):

    resp = UserServiceApi().create_user(fake_user)
    user_id = resp.get_field("id")

    user_address = {"street": faker.street_name(), "number": faker.building_number(), "country": faker.country(),
                    "city": faker.city(), "postcode": faker.postcode(), "userID": f"{user_id}"}

    resp = UserServiceApi().create_user_address(user_address)
    resp.should_have(status_code(200))
