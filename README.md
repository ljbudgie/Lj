# Lj

Clawbot — an open, extensible automation ecosystem built on **The Burgess Principle**:
open, extensible, and adaptable for global needs while preserving individual sovereignty.

---

## ♿ Accessibility Features

This repository includes a suite of accessibility-first workflows and templates
that automate common inclusive-design tasks.

### Automated Workflows

| Workflow | File | Description |
|---|---|---|
| Speech-to-Text | [`.github/workflows/speech-to-text.yml`](.github/workflows/speech-to-text.yml) | Transcribes audio files using [OpenAI Whisper](https://github.com/openai/whisper). Triggers on upload of `.mp3`, `.wav`, `.m4a`, `.ogg`, or `.flac` files. |
| Accessibility Testing | [`.github/workflows/accessibility-testing.yml`](.github/workflows/accessibility-testing.yml) | Runs [axe-core](https://github.com/dequelabs/axe-core) WCAG 2.1 AA scans on HTML files in every push and pull request. |
| Text-to-Speech | [`.github/workflows/text-to-speech.yml`](.github/workflows/text-to-speech.yml) | Converts Markdown documentation to MP3 audio using [gTTS](https://pypi.org/project/gTTS/) (default) or Amazon Polly. |
| Inclusive Docs | [`.github/workflows/inclusive-docs.yml`](.github/workflows/inclusive-docs.yml) | Checks images for missing alt text, validates heading hierarchy, and generates alt-text stub files for newly added images. |

### Documentation & Templates

| Document | Description |
|---|---|
| [`docs/accessibility/contributor-guide.md`](docs/accessibility/contributor-guide.md) | Accessibility-first contribution guidelines: alt text rules, caption requirements, WCAG colour contrast, and more. |
| [`docs/accessibility/alt-text-template.md`](docs/accessibility/alt-text-template.md) | Copy-paste template for recording alt text, video captions, and audio transcript metadata. |

### Quick Start

1. **Audio transcription** — place audio files in `audio/` and push; transcripts appear in `transcriptions/`.
2. **Accessibility scan** — push or open a PR containing HTML files; axe-core results are posted as a PR comment.
3. **Documentation audio** — push changes to `docs/` or `README.md`; MP3 versions are generated in `audio-docs/`.
4. **Image alt text** — open a PR with images; the workflow flags missing alt text and comments on the PR.

### Configuration

| Secret / Input | Workflow | Purpose |
|---|---|---|
| *(none required)* | speech-to-text | Uses local Whisper by default |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | text-to-speech | Required only when `provider=polly` |
| `AWS_DEFAULT_REGION` | text-to-speech | Defaults to `us-east-1` |

All workflows are **opt-in** and provider-agnostic in line with The Burgess Principle.