# Lj – Clawbot

> A comprehensive GitHub automation bot providing accessibility, AI collaboration, contribution pipeline enhancements, and self-healing ecosystem features.

---

## Features

### ♿ Advanced Accessibility & Personalization

| Feature | Description |
|---------|-------------|
| **AI-Powered Adaptations** | Automatically applies accessibility profiles (visual, motor, cognitive) based on `config/clawbot.yml` |
| **Multi-Language Documentation** | Automated multilingual translation of repository docs via DeepL |
| **Braille Export** | Exports Markdown docs into BRF (Braille-Ready Format, Grade 2) for tactile displays |

**Workflow:** [`.github/workflows/accessibility.yml`](.github/workflows/accessibility.yml)

---

### 🤖 AI Collaboration Framework

| Feature | Description |
|---------|-------------|
| **Hugging Face Integration** | Health-checks configured models; ready for inference hooks |
| **DeepL Integration** | Validates API availability; powers multilingual translation |
| **Intelligent Decision Making** | Scans repository data (stale issues, gaps) and suggests actions |

**Workflow:** [`.github/workflows/ai-collaboration.yml`](.github/workflows/ai-collaboration.yml)

---

### 🔄 Enhanced Automation

| Feature | Description |
|---------|-------------|
| **Action Version Checks** | Scans all workflow files for outdated `uses:` pins and reports them |
| **Config Validation** | Validates `config/clawbot.yml` on every Monday run |

**Workflow:** [`.github/workflows/dependency-updates.yml`](.github/workflows/dependency-updates.yml)

---

### 🚀 Contribution Pipeline Enhancements

| Feature | Description |
|---------|-------------|
| **AI-Enhanced PR Reviews** | Checks issue linking, accessibility compliance; auto-comments on PRs |
| **Contributor Assistants** | Auto-labels PRs (`documentation`, `ci/cd`, `accessibility`, `configuration`) |
| **Gamified Badges** | Awards ♿ Accessibility Champion, 🌐 Multilingual Hero, 🛡️ Dependency Guardian badges |

**Workflow:** [`.github/workflows/pr-review.yml`](.github/workflows/pr-review.yml)

---

### 🛡️ Ecosystem & Trust

| Feature | Description |
|---------|-------------|
| **Self-Healing Workflows** | Monitors all workflows every 6 hours; creates issue alerts on failures |
| **Auto-Retry** | Automatically re-triggers failed runs (up to `max_retries` attempts) |
| **Reputation System** | Tracks contributor scores; publishes a weekly [leaderboard](docs/leaderboard.md) |

**Workflows:** [`.github/workflows/self-healing.yml`](.github/workflows/self-healing.yml) · [`.github/workflows/reputation.yml`](.github/workflows/reputation.yml)

---

## Configuration

All features are controlled via [`config/clawbot.yml`](config/clawbot.yml).

```yaml
accessibility:
  ai_adaptations:
    enabled: true
  multilingual:
    enabled: true
    target_languages: [es, fr, de, zh, ar, pt, ja]
  braille:
    enabled: true

ai_collaboration:
  hugging_face:
    enabled: true
  deepl:
    enabled: true
  intelligent_decision_making:
    enabled: true

contribution_pipeline:
  gamification:
    enabled: true
  pr_review:
    enabled: true
  contributor_assistant:
    enabled: true

ecosystem:
  self_healing:
    enabled: true
    auto_retry: true
  reputation:
    enabled: true
```

### Required Secrets

| Secret | Used by |
|--------|---------|
| `DEEPL_API_KEY` | Translation workflow |
| `HUGGINGFACE_API_TOKEN` | AI collaboration workflow |
| `GITHUB_TOKEN` | All workflows (auto-provided) |

---

## Documentation

- [Contributor Leaderboard](docs/leaderboard.md)
