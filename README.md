# Mailer — Copilot Skills & Agents Exercise

This repository contains the Mailer project exercises for creating GitHub Copilot configuration:

- `copilot-instructions.md` — global Copilot instructions for the Mailer project
- `.copilot/skills/` — skills created for the exercises (email-validation, mailer-complete-testing, email-templates)
- `.agents/` — agent definitions and workflows (docs-generator-agent)

Work is stored on the `copilot-config` branch. The `main` branch has been kept clean — changes are proposed from `copilot-config`.

How to use:

1. Checkout the feature branch:

```bash
git checkout copilot-config
git pull origin copilot-config
```

2. Review skills and agents in `.copilot/` and `.agents/`.

3. To propose merging the changes, create a Pull Request from `copilot-config` to `main` on GitHub.

If you want, I can create the PR for you.