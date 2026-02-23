# Alt-Text & Caption Template

Use this template when adding images, diagrams, or video to the repository.
Copy the relevant section, fill it in, and include the link alongside your
media file so reviewers can verify accessibility compliance.

---

## Image Alt-Text Record

| Field | Value |
|---|---|
| **File path** | `images/example.png` |
| **Alt text** | *(Replace with a concise, descriptive phrase — 1–2 sentences max)* |
| **Is decorative?** | No / Yes — if Yes, use `alt=""` in HTML or `![ ](path)` in Markdown |
| **Additional long description** | *(Only needed for complex diagrams — add as surrounding paragraph or `aria-describedby`)* |

### Writing Good Alt Text

- ✅ `"Bar chart comparing monthly active users in 2024 and 2025, showing a 40% increase in Q3 2025."`
- ✅ `"Photograph of the Clawbot logo: a blue claw icon on a white background."`
- ❌ `"image"` — too vague
- ❌ `"chart.png"` — filename is not a description
- ❌ `"Click here"` — describes action, not content

---

## Video Caption Checklist

For every `.mp4` / `.webm` video added to the repository:

- [ ] Caption file (`.vtt` or `.srt`) exists in the same directory with the same base name.
- [ ] Captions include all spoken dialogue.
- [ ] Captions identify non-speech audio that conveys meaning (e.g. `[applause]`, `[alarm beeping]`).
- [ ] Speaker labels are included when multiple speakers are present.
- [ ] Caption file is encoded in UTF-8.

### Minimal VTT Example

```vtt
WEBVTT

00:00:01.000 --> 00:00:04.000
Welcome to the Clawbot accessibility demo.

00:00:04.500 --> 00:00:07.000
This workflow automatically transcribes your audio files.
```

---

## Audio Transcript Checklist

For every audio file (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`):

- [ ] Audio is placed in the `audio/` directory to trigger automatic transcription.
- [ ] The auto-generated transcript in `transcriptions/` has been reviewed for accuracy.
- [ ] Any corrections have been committed alongside the audio file.
- [ ] The transcript file is linked from the relevant documentation page.

---

## Diagram / Infographic Extended Description

For complex visuals (flowcharts, architecture diagrams, infographics):

1. Provide a short alt text (max 125 characters) in the `alt` attribute.
2. Add a longer description immediately below the image in the document body.

**Template:**

```markdown
![Short description (max 125 chars)](path/to/diagram.svg)

**Diagram description:** Full prose description of all data, relationships, and
key takeaways conveyed by the diagram, so a user who cannot see it still receives
equivalent information.
```

---

*For more guidance, see the [Contributor Accessibility Guide](contributor-guide.md).*
