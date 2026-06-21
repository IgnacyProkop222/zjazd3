# Email Templates Skill

## Cel umiejętności
Skill ma wspierać projekt Mailer w tworzeniu funkcjonalnych i bezpiecznych szablonów emaili. Obejmuje projektowanie HTML i plain text templates, dziedziczenie szablonów, podstawienie zmiennych oraz testowanie kompletności i renderowania.

## Kontekst
- Projekt: Mailer
- Funkcjonalność: Email Templates
- Zastosowanie: powiadomienia, newslettery, potwierdzenia
- Typ: HTML + plain text, multiplatformowe email template

## Zasady projektowe
- Szablony powinny być czytelne i proste do rozszerzenia
- Oddziel logikę treści od logiki renderowania
- Używaj Jinja2 dla template inheritance i variable substitution
- Dla wiadomości tekstowych generuj plain text obok HTML
- Testuj rendering dla każdego kluczowego szablonu

## Template inheritance
Szablon bazowy zawiera wspólne fragmenty:
- nagłówek
- stopka
- style CSS
- strukturę layoutu

Przykład podstawowego szablonu bazowego:

```jinja
{# templates/base_email.html #}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <style>
      body { font-family: Arial, sans-serif; color: #333; }
      .content { margin: 20px; }
      .footer { font-size: 12px; color: #777; }
    </style>
  </head>
  <body>
    <div class="content">
      {% block body %}{% endblock %}
    </div>
    <div class="footer">
      {% block footer %}This email was sent by Mailer{% endblock %}
    </div>
  </body>
</html>
```

Przykład szablonu z rozszerzeniem:

```jinja
{# templates/welcome_email.html #}
{% extends "base_email.html" %}

{% block body %}
<h1>Witaj, {{ user_name }}!</h1>
<p>Dziękujemy za dołączenie do listy mailingowej.</p>
<p>Twoje konto: {{ user_email }}</p>
{% endblock %}
```

## Variable substitution
- Używaj nazwanych zmiennych, np. `{{ user_name }}` i `{{ confirmation_link }}`
- Waliduj, że wymagane zmienne są obecne przed renderowaniem
- Unikaj bezpośredniego wstrzykiwania HTML w wartościach zmiennych
- Dla tekstu używaj `|e` lub domyślnego autoescape w Jinja2

## HTML/Plain text templates
- Dla każdego wysyłanego emaila zapewnij wersję HTML i plain text
- Plain text może być generowany ręcznie lub konwertowany z HTML
- Wygenerowany tekst powinien być czytelny bez formatowania HTML
- Używaj `multipart/alternative` w payload emaila

## Template testing
Testy powinny obejmować:
- poprawne renderowanie z kompletem danych
- brakujące zmienne generujące czytelny błąd
- zgodność HTML i plain text
- brak niebezpiecznych tagów lub skryptów

Przykład testu:

```python
import pytest
from mailer.email_templates import EmailTemplateRenderer

class TestEmailTemplateRenderer:
    @pytest.fixture
    def renderer(self):
        return EmailTemplateRenderer(template_folder="templates")

    def test_render_welcome_email(self, renderer):
        context = {"user_name": "Anna", "user_email": "anna@example.com"}
        html, text = renderer.render("welcome_email.html", context)

        assert "Witaj, Anna" in html
        assert "anna@example.com" in text
        assert "<h1>" in html
        assert "Witaj," in text
```

## Przykłady
### Welcome
- Szablon powitalny
- `{{ user_name }}`, `{{ user_email }}`, `{{ login_url }}`

### Confirmation
- Potwierdzenie rejestracji lub zapisu
- `{{ confirmation_link }}`, `{{ expire_time }}`

### Newsletter
- Lista artykułów, linki i podsumowanie
- `{{ items }}`, `{{ unsubscribe_url }}`

## Najlepsze praktyki
- Zawsze specjalizuj szablon dla konkretnego typu wiadomości
- Utrzymuj CSS inline i prosty
- Unikaj złożonych logik w Jinja2
- Parametryzuj testy dla różnych wariantów danych
- Dokumentuj wymagane pola w docstringach funkcji renderujących

## Implementacja wspierająca
Proponowana klasa renderująca:

```python
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Dict, Tuple

class EmailTemplateRenderer:
    def __init__(self, template_folder: str):
        self.env = Environment(
            loader=FileSystemLoader(template_folder),
            autoescape=select_autoescape(["html", "xml"]),
        )

    def render(self, template_name: str, context: Dict[str, str]) -> Tuple[str, str]:
        template = self.env.get_template(template_name)
        html = template.render(**context)
        text = self._render_text_version(template_name, context)
        return html, text

    def _render_text_version(self, template_name: str, context: Dict[str, str]) -> str:
        text_template_name = template_name.replace(".html", ".txt")
        template = self.env.get_template(text_template_name)
        return template.render(**context)
```

## Podsumowanie
Skill `email-templates` zapewnia kompletny zestaw zasad i przykładów do tworzenia, renderowania oraz testowania szablonów email w projekcie Mailer. Dzięki temu można łatwo wspierać różne typy wiadomości, zachowując spójność i bezpieczeństwo.
