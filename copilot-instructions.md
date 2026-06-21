# GitHub Copilot Instructions - Mailer Project

## 1. Python i Zależności
- Używaj Python 3.9+
- Zależności deklaruj w `requirements.txt`
- Type hints obowiązkowe dla funkcji i metod publicznych
- Formatowanie kodu: PEP 8, black, flake8
- Unikaj linijek dłuższych niż 88 znaków

## 2. Struktura kodu
- Moduły: max 500 linii
- Funkcje: max 50 linii
- Klasy: pojedyncza odpowiedzialność
- Oddziel logikę biznesową od warstwy web
- W `mailer/` umieszczaj logikę wysyłania emaili i zarządzania subskrybentami
- `templates/` zawiera tylko HTML i Jinja2 templates
- `static/` zawiera CSS i JavaScript, bez logiki Pythona
- `tests/` zawiera tylko testy pytest

## 3. Testy
- Wymagane: pytest + pytest-cov
- Minimum 80% coverage dla kodu produkcyjnego
- Mockuj zewnętrzne usługi takie jak SMTP
- Testy powinny obejmować happy path, edge cases i error handling
- Każda funkcja publiczna powinna mieć przynajmniej 2 testy
- Używaj parametryzowanych testów tam, gdzie ma to sens

## 4. Bezpieczeństwo
- Nie chować secrets w repozytorium
- Używaj environment variables dla konfiguracji SMTP, API keys i haseł
- Waliduj dane wejściowe, szczególnie adresy email i dane formularzy
- W aplikacji webowej: ochrona przed XSS i CSRF
- Nie commituj credentials ani plików konfiguracyjnych z hasłami

## 5. Git
- Commity stosuj zgodnie z konwencją conventional commits
- Branch naming: `feature/*`, `bugfix/*`, `docs/*`
- PR powinien mieć opis, listę zmian i testy
- Unikaj dużych commitów z mieszanką funkcjonalności i refaktoringu

## 6. Obsługa błędów
- Zwracaj czytelne wyjątki i komunikaty błędów
- Loguj błędy w serwerze email i w UI
- Nie ujawniaj tajnych informacji w komunikatach użytkownika
- Używaj walidacji na wejściu i defensywnego programowania

## 7. Testowanie i Skill
- W testach odwołuj się do `Mailer Complete Testing Skill` dla wzorców
- Mockuj SMTP, walidację email i dane subskrybentów
- Pokrywaj zarówno logikę `mailer/`, jak i warstwę `web` oraz `templates`
