class Condition:
    pass


class StatusCodeCondition:

    def __init__(self, expected_status_code):
        self._expected_status_code = expected_status_code

    def match(self, response):
        actual_status_code = response.status_code
        assert actual_status_code == self._expected_status_code, f"{actual_status_code} != {self._expected_status_code}"

    def __repr__(self):
        return f"status code: {self._expected_status_code}"


status_code = StatusCodeCondition
