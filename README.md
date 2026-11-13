# API Automation Testing with Python and Pytest

A reusable starter framework for REST API checks using Python, Requests and Pytest.

## Features
- Reusable HTTP client and fixture
- Positive and negative GET tests
- Status, content type, JSON structure and field assertions
- Configurable base URL
- HTML test reports

## Requirements
Python 3.10+, pip and network access.

## Setup
```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests
```bash
pytest -v
pytest --html=reports/report.html --self-contained-html
```

Default target: JSONPlaceholder demo API. Configure another authorized target with `API_BASE_URL`.

```bash
# PowerShell
$env:API_BASE_URL="https://jsonplaceholder.typicode.com"
# macOS/Linux
export API_BASE_URL="https://jsonplaceholder.typicode.com"
pytest
```

## Structure
- `clients/api_client.py` — reusable requests wrapper
- `api_tests/` — tests and fixtures
- `docs/FRAMEWORK-DESIGN.md` — architecture and extension notes
- `requirements.txt` — dependencies
- `pytest.ini` — test discovery and options

## Test coverage
Collection retrieval, single-resource retrieval, unknown-resource response, JSON structure, and a simple response-time threshold.

The deterministic API-client unit suite also verifies base URL normalization, environment-variable precedence, URL construction, timeout forwarding, session headers and cleanup, and propagation of `requests.Timeout` exceptions. The client does not silently suppress request exceptions; calling code should handle them according to the application's retry and error-reporting policy.

## Engineering practices
Use deterministic assertions, short timeouts, isolated test data, environment-based configuration, and secret redaction. Network/service outages should be distinguished from application defects.

## Evidence integrity
Run the suite before reporting pass rates. Public demo responses can change or be unavailable; the repository is a starter framework, not proof of a completed production assessment.

## Author
Michael Uma — QA Automation Portfolio.


## Continuous integration

GitHub Actions runs the deterministic API-client unit tests on pushes and pull requests targeting `main`. These tests mock the HTTP session, so they validate URL construction, timeout forwarding, environment-based configuration, request headers, and timeout-exception propagation without depending on a live third-party API.

The live JSONPlaceholder integration checks remain separate:

```bash
pytest -q api_tests/test_posts.py
```

Those integration checks require network access and depend on the public demo service being available. Treat service/network failures separately from defects in the API client.
