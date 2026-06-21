# Mailer Complete Testing - Instructions

Purpose: Guidance for writing tests covering all Mailer components.

Contents:
- Test scope: validation, email sending, subscribers, web interface
- Fixture conventions and mocks (SMTP, DB stubs)
- Recommended test structure: arrange/act/assert
- Examples location: `resources/templates/` and `resources/examples/`

Recommendations:
- Each public function: min 2 tests (happy path + edge/error)
- Use pytest fixtures and parametrize cases
- Mock external services and avoid sending real emails
