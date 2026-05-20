def assert_success_response(response):
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    return data


def assert_response_has_success_true(data):
    assert "success" in data
    assert data["success"] is True


def assert_non_empty_string(value):
    assert isinstance(value, str)
    assert len(value.strip()) > 0