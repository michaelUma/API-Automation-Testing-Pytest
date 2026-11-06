# Framework Design

## Layers
- Tests describe expected API behavior.
- Fixtures create and close the client.
- APIClient centralizes base URL, timeout, and HTTP session.
- Environment variables configure the target without changing source.

## Extension roadmap
1. Add JSON Schema validation.
2. Add parametrized negative tests.
3. Add bearer-token injection from environment variables.
4. Add request/response logging with secret redaction.
5. Add CI execution and report publication.

## Reliability
Tests call a public demo service and require network access. A timeout or outage is an environment failure until investigated, not automatically an application defect.
