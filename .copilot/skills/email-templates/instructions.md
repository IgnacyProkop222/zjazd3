# Email Templates - Instructions

Purpose: Describe template conventions, required files and examples for email templates.

Contents:
- Template layout: base HTML (`resources/templates/base_email.html`)
- Per-message templates: `welcome_email.html`, `welcome_email.txt`
- Variable conventions and required context keys
- Testing recommendations and examples location: `resources/templates/` and `resources/examples/`

Security:
- Autoescape HTML by default
- Avoid embedding untrusted HTML in variables
