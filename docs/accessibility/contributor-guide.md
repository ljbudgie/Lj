# Accessibility-First Contributor Guide

This guide explains how to write inclusive, accessible documentation and code
for this repository. It reflects **The Burgess Principle**: Clawbot remains open,
extensible, and adaptable for global accessibility needs while preserving
individual sovereignty.

---

## Why Accessibility Matters

Accessible content benefits everyone, not only people with disabilities.
Clear writing, properly labelled images, and well-structured documents improve
comprehension, discoverability, and machine readability.

---

## 1. Writing Accessible Markdown

### Document Structure

#### Heading Hierarchy

Use headings in order — never skip a level. Screen readers rely on a logical
heading hierarchy to help users navigate.

```markdown
# Page Title (H1 — one per document)
## Major section (H2)
### Sub-section (H3)
```

❌ **Wrong** — skipping from H1 to H3 confuses screen readers:
```markdown
# Title
### Section   ← skipped H2
```

#### Plain Language

- Prefer short sentences and common words.
- Spell out acronyms on first use: e.g. "WCAG (Web Content Accessibility Guidelines)".
- Use active voice where possible.

---

## 2. Images and Graphics

Every image **must** have a descriptive `alt` attribute.

### Markdown syntax

```markdown
![A golden retriever puppy sitting on green grass](images/puppy.jpg)
```

### HTML `<img>` tags

```html
<img src="images/diagram.png" alt="Flow diagram showing the data pipeline: input → processing → output" />
```

### Rules for writing alt text

| Situation | Guidance |
|---|---|
| Informative image | Describe the content and function concisely (1–2 sentences). |
| Decorative image | Use an empty alt: `alt=""`. Do **not** omit the attribute. |
| Complex diagram / chart | Provide a short alt plus a longer description in the surrounding text. |
| Text in an image | Include all text visible in the image in the alt attribute. |

> **Automated check**: The `inclusive-docs` workflow will flag images with missing
> or empty alt text and open a PR comment listing all issues.

---

## 3. Video and Audio Content

### Captions for video

All video files added to the repository **must** be accompanied by a caption
file (`.vtt` or `.srt`) in the same directory with the same base name:

```
videos/
  demo-tour.mp4
  demo-tour.vtt     ← captions required
```

### Audio transcripts

Audio files (`.mp3`, `.wav`, etc.) trigger the **Speech-to-Text** workflow
automatically. The generated transcript is committed to `transcriptions/` and
should be reviewed for accuracy before merging.

---

## 4. Code and UI Accessibility

When contributing HTML or JavaScript, ensure:

- All interactive elements are reachable via keyboard (`Tab`, `Enter`, `Space`).
- Form inputs have associated `<label>` elements or `aria-label` attributes.
- Colour contrast meets WCAG 2.1 AA (minimum 4.5:1 for normal text).
- No information is conveyed by colour alone.
- Focus indicators are visible.

The **Accessibility Testing** workflow runs `axe-core` on all HTML files in
pull requests and posts a summary comment.

---

## 5. Documentation Templates

Copy the templates in this directory when creating new documentation:

| Template | Purpose |
|---|---|
| [`alt-text-template.md`](alt-text-template.md) | Record and review alt text for images |
| *(WCAG checklist — coming soon)* | Self-review before PR |

---

## 6. Automated Workflows Summary

| Workflow | Trigger | What it does |
|---|---|---|
| `speech-to-text.yml` | Push of audio files or manual | Transcribes audio with OpenAI Whisper |
| `accessibility-testing.yml` | Push/PR of HTML/CSS/JS | Scans with axe-core for WCAG violations |
| `text-to-speech.yml` | Push of docs or manual | Generates MP3 audio from Markdown using gTTS or Amazon Polly |
| `inclusive-docs.yml` | Push/PR of docs or images | Checks alt text, heading hierarchy, and creates alt-text stubs |

---

## 7. The Burgess Principle

> *Openness, extensibility, and adaptability — with sovereignty for the individual.*

Every accessibility integration should:

1. **Remain optional** — workflows can be disabled without breaking core functionality.
2. **Be provider-agnostic** — prefer open-source tools (Whisper, axe-core, gTTS) with
   commercial options (Polly, Google TTS) available via configuration.
3. **Avoid locking in data** — transcripts, audio files, and reports are stored in
   the repository and are fully portable.
4. **Respect privacy** — no audio or text is sent to external services without explicit
   opt-in through repository secrets or workflow inputs.
