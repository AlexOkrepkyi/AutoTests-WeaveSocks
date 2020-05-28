
rm -rf allure_results
pytest -sv tests/api/test_api_users_register.py
~/.allure/allure-2.13.2/bin/allure serve allure_results
