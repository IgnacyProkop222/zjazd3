# Email Validation - Instructions

Purpose: Provide guidance and examples for implementing email validation in the Mailer project.

Contents:
- Purpose and when to use this skill
- Required function signature and return values
- Examples location: `resources/examples/`

Required validations:
- Type and emptiness checks
- Local-part and domain format checks
- Length limits
- Allowed special characters per simplified RFC 5322

Examples included:
- `resources/examples/validator_example.py` — simple validator usage example

Usage:
- Use this skill to generate validation helpers and tests.
- Prefer returning boolean or raising a specific ValidationError for invalid inputs.
