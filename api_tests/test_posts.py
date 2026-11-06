def test_list_posts_returns_json_array(api):
    response = api.get("/posts")

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) > 0


def test_get_existing_post_has_expected_fields(api):
    response = api.get("/posts/1")

    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
    assert isinstance(post["userId"], int)


def test_unknown_post_returns_not_found(api):
    response = api.get("/posts/999999")

    assert response.status_code == 404


def test_response_time_is_within_learning_threshold(api):
    response = api.get("/posts/1")

    assert response.status_code == 200
    # A simple demo threshold, not a production SLA.
    assert response.elapsed.total_seconds() < 3.0
