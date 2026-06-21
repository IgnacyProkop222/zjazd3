# Test Template Example

- Fixture: `smtp_mock`, `db_tmp`
- Test: `test_add_subscriber_valid` — assert subscriber added and persisted
- Test: `test_add_subscriber_invalid_email` — assert validation error
- Test: `test_send_email_single_recipient` — mock SMTP and assert send called
