import os
import requests


class APIClient:
    """Small reusable wrapper around requests.Session."""

    def __init__(self, base_url: str | None = None, timeout: float = 10.0):
        self.base_url = (base_url or os.getenv(
            "API_BASE_URL", "https://jsonplaceholder.typicode.com"
        )).rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get(self, path: str):
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, timeout=self.timeout)

    def close(self):
        self.session.close()
