# Biblical Video Editor - Quick Reference

## Installation
```bash
git clone https://github.com/ljbudgie/Lj.git
cd Lj
pip install -r requirements.txt
sudo apt-get install imagemagick  # Ubuntu/Debian
```

## Common Commands

### Add Simple Quote
```bash
python video_editor.py input.mp4 output.mp4 \
  --text "Love your neighbor - Matthew 22:39"
```

### Add Intro + Outro
```bash
python video_editor.py input.mp4 output.mp4 \
  --intro "Jesus Said..." \
  --outro "Amen"
```

### Customize Text
```bash
python video_editor.py input.mp4 output.mp4 \
  --text "I am the light of the world - John 8:12" \
  --font-size 70 \
  --font-color gold \
  --position center
```

### Multiple Quotes
```bash
python video_editor.py input.mp4 output.mp4 \
  --quote-file examples/beatitudes.txt
```

### Timed Quote
```bash
python video_editor.py input.mp4 output.mp4 \
  --text "Peace be with you - John 20:21" \
  --start-time 30 \
  --duration 8
```

## Options Reference

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--text` | `-t` | Quote text | None |
| `--intro` | `-i` | Intro text | None |
| `--outro` | `-o` | Outro text | None |
| `--quote-file` | `-q` | File with quotes | None |
| `--start-time` | `-s` | Start time (sec) | 0 |
| `--duration` | `-d` | Duration (sec) | Full video |
| `--font-size` | `-fs` | Font size | 50 |
| `--font-color` | `-fc` | Text color | white |
| `--bg-color` | `-bg` | Background | transparent |
| `--position` | | top/center/bottom | bottom |

## Helper Commands

```bash
# Browse quotes interactively
python examples.py interactive

# Show example commands
python examples.py examples

# Generate example quote files
python examples.py create-files

# Test biblical quotes
python biblical_quotes.py

# Run test suite
python test_editor.py
```

## Quote Files Available

- `examples/beatitudes.txt` - The Beatitudes (7 quotes)
- `examples/love_quotes.txt` - Teachings on love (4 quotes)
- `examples/faith_quotes.txt` - Teachings on faith (1 quote)
- `examples/kingdom_quotes.txt` - Kingdom teachings (6 quotes)
- `examples/i_am_statements.txt` - "I am" statements (7 quotes)
- `examples/daily_devotional.txt` - Daily devotional (5 quotes)

## Tips

- **Font Size**: Use 40-80 for readability
- **Duration**: Allow 5-8 seconds to read quotes
- **Testing**: Test with short clips first
- **Colors**: white, black, yellow, gold, red, blue
- **Position**: bottom is least intrusive

## Get Help

```bash
python video_editor.py --help
```

## Common Issues

**"No module named 'moviepy'"**
```bash
pip install -r requirements.txt
```

**"Failed to read text"**
```bash
# Install ImageMagick
sudo apt-get install imagemagick  # Ubuntu
brew install imagemagick          # macOS
```

## Documentation

- **README.md** - Full documentation
- **USAGE.md** - Detailed usage guide
- **PROJECT_SUMMARY.md** - Project overview

---

*"Let your light shine before others." - Matthew 5:16*
