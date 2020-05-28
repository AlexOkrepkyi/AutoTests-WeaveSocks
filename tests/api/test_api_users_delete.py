from src.api.conditions import status_code
from src.api.user_service_api import UserServiceApi


def test_user_can_be_deleted(fake_user):
    resp = UserServiceApi().create_user(fake_user)
    user_id = resp.get_field("id")
    resp = UserServiceApi().delete_user(user_id)
    resp.should_have(status_code(200))


