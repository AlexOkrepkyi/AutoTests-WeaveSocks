from src.api.user_service_api import UserServiceApi


def test_get_total_number_of_users_in_database():
    print(UserServiceApi().get_total_number_of_users_in_database())


def test_get_total_number_of_user_addresses_in_database():
    print(UserServiceApi().get_total_number_of_user_addresses_in_database())


def test_get_total_number_of_user_cards_in_database():
    print(UserServiceApi().get_total_number_of_user_cards_in_database())


def test_number_of_users_in_database_increases_after_new_registration(fake_user):
    UserServiceApi().verify_number_of_users_in_database_increases_after_new_registration(fake_user)


