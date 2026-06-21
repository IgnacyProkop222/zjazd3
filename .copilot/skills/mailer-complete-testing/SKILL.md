# Mailer Complete Testing Skill

## Cel umiejętności
Kompleksowy skill dla testowania komponentów systemu Mailer. Zapewnia wzorce dla testów walidacji, wysyłania emaili, zarządzania subskrybentami oraz interfejsu Flask.

## Komponenty do testowania

### 1. Email Validation
- Format email
- Długość
- Specjalne znaki
- Empty values

### 2. Email Sending
- Single recipient
- Multiple recipients
- Attachment handling
- Error handling
- Connection failures

### 3. Subscribers Management
- Add subscriber
- Remove subscriber
- List subscribers
- Duplicate prevention
- Invalid emails

### 4. Web Interface (Flask)
- Routes accessibility
- Form validation
- Error handling
- HTML rendering
- Response status codes

## Test Template

Opisuj strukturę testów w formie słownej zamiast podawać gotowych skryptów. Na przykład:
- przygotowanie konfiguracji testowej w fixture
- testowanie scenariusza poprawnego przebiegu
- testowanie edge cases i błędów
- testowanie warunków brzegowych i nieprawidłowych danych

## Coverage Requirements
- Functions: 100%
- Branches: 80%
- Lines: 85%

## Tools
- pytest
- pytest-cov
- pytest-mock
- coverage

## Zalecenia
- Używaj mocków dla SMTP i zewnętrznych HTTP requestów.
- Twórz testy izolowane, bez wysyłania rzeczywistych emaili.
- Pokrywaj każdy przypadek użycia i każdy warunek błędu.
- Dokumentuj fixture, inputy i oczekiwane rezultaty.
