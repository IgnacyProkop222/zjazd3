# Example usage of EmailValidator

from validators import EmailValidator

examples = [
    "user@example.com",
    "user+tag@domain.co.uk",
    "invalid@",
    "@domain.com",
]

for e in examples:
    print(e, EmailValidator.validate(e))
