from src.api.conditions import status_code
from src.api.user_service_api import UserServiceApi


def test_user_can_register_with_valid_credentials(fake_user):
    resp = UserServiceApi().create_user(fake_user)
    resp.should_have(status_code(200))


def test_registered_user_has_id(fake_user):
    resp = UserServiceApi().create_user(fake_user)
    user_id = resp.get_field("id")
    assert len(user_id) > 0, f"\n--- User ID's length is {len(user_id)}, but should be > 0 ---"
