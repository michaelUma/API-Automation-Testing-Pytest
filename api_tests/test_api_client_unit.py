import os
from unittest.mock import Mock, patch

from clients.api_client import APIClient


def test_client_normalizes_base_url_and_sets_accept_header():
    with patch("clients.api_client.requests.Session") as session_factory:
        session = session_factory.return_value

        client = APIClient(base_url="https://example.test/api/")

        assert client.base_url == "https://example.test/api"
        session.headers.update.assert_called_once_with(
            {"Accept": "application/json"}
        )

        client.close()
        session.close.assert_called_once_with()


def test_client_uses_environment_base_url_when_not_provided():
    with patch.dict(os.environ, {"API_BASE_URL": "https://env.example/api/"}):
        with patch("clients.api_client.requests.Session") as session_factory:
            client = APIClient()

            assert client.base_url == "https://env.example/api"

            client.close()


def test_explicit_base_url_overrides_environment_value():
    with patch.dict(os.environ, {"API_BASE_URL": "https://env.example/api"}):
        with patch("clients.api_client.requests.Session"):
            client = APIClient(base_url="https://explicit.example/v1/")

            assert client.base_url == "https://explicit.example/v1"

            client.close()


def test_get_joins_base_url_and_path_and_passes_timeout():
    with patch("clients.api_client.requests.Session") as session_factory:
        session = session_factory.return_value
        expected_response = Mock()
        session.get.return_value = expected_response

        client = APIClient(
            base_url="https://example.test/api/",
            timeout=2.5,
        )

        response = client.get("/posts")

        assert response is expected_response
        session.get.assert_called_once_with(
            "https://example.test/api/posts",
            timeout=2.5,
        )

        client.close()


def test_get_uses_default_timeout_and_accepts_path_without_leading_slash():
    with patch("clients.api_client.requests.Session") as session_factory:
        session = session_factory.return_value

        client = APIClient(base_url="https://example.test/api")

        client.get("posts")

        session.get.assert_called_once_with(
            "https://example.test/api/posts",
            timeout=10.0,
        )

        client.close()
