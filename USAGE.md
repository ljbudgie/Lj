# Usage Guide - Biblical Video Editor

## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Command Reference](#command-reference)
4. [Biblical Quotes Database](#biblical-quotes-database)
5. [Advanced Usage](#advanced-usage)
6. [Tips and Best Practices](#tips-and-best-practices)
7. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- ImageMagick (for text rendering)

### Step-by-Step Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ljbudgie/Lj.git
cd Lj
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install ImageMagick:**

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install imagemagick
```

**macOS (requires Homebrew):**
```bash
brew install imagemagick
```

**Windows:**
- Download from: https://imagemagick.org/script/download.php
- Run the installer
- Make sure to check "Install legacy utilities" during installation

### Verify Installation

```bash
# Test the biblical quotes module
python biblical_quotes.py

# Show help for the video editor
python video_editor.py --help
```

## Quick Start

### Example 1: Simple Text Overlay

Add a biblical quote to your video:

```bash
python video_editor.py input.mp4 output.mp4 \
  --text "Love your neighbor as yourself - Matthew 22:39"
```

### Example 2: Add Intro and Outro

```bash
python video_editor.py input.mp4 output.mp4 \
  --intro "The Teachings of Jesus" \
  --outro "Go in Peace"
```

### Example 3: Customize Appearance

```bash
python video_editor.py input.mp4 output.mp4 \
  --text "Blessed are the peacemakers - Matthew 5:9" \
  --font-size 60 \
  --font-color yellow \
  --position center
```

## Command Reference

### Basic Syntax

```bash
python video_editor.py INPUT OUTPUT [OPTIONS]
```

### Positional Arguments

| Argument | Description |
|----------|-------------|
| `INPUT` | Path to input video file |
| `OUTPUT` | Path to output video file |

### Optional Arguments

#### Text Content Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--text TEXT` | `-t` | Text overlay (biblical quote) | None |
| `--intro INTRO` | `-i` | Intro text before video | None |
| `--outro OUTRO` | `-o` | Outro text after video | None |
| `--quote-file FILE` | `-q` | File with multiple quotes | None |

#### Timing Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--start-time SECONDS` | `-s` | When to show text | 0 |
| `--duration SECONDS` | `-d` | How long to show text | Entire video |

#### Appearance Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--font-size SIZE` | `-fs` | Font size | 50 |
| `--font-color COLOR` | `-fc` | Text color | white |
| `--bg-color COLOR` | `-bg` | Background color | transparent |
| `--position POS` | | Text position (top/center/bottom) | bottom |

### Color Options

Supported colors include:
- **Named colors**: white, black, red, blue, green, yellow, gold, silver, orange, purple
- **Hex colors**: #FFFFFF, #000000, etc.
- **RGB**: rgb(255, 255, 255)
- **RGBA** (with transparency): rgba(0, 0, 0, 0.7)

## Biblical Quotes Database

### Using the Database in Python

```python
from biblical_quotes import (
    get_random_quote,
    get_all_quotes,
    get_beatitudes,
    get_quotes_by_theme,
    save_quotes_to_file
)

# Get a random quote
quote = get_random_quote()
print(quote)

# Get all quotes (42 total)
all_quotes = get_all_quotes()

# Get the Beatitudes (7 quotes)
beatitudes = get_beatitudes()

# Get quotes by theme
love_quotes = get_quotes_by_theme('love')
faith_quotes = get_quotes_by_theme('faith')
kingdom_quotes = get_quotes_by_theme('kingdom')

# Save quotes to a file
save_quotes_to_file('my_quotes.txt', love_quotes)
```

### Quote Categories

The database includes 42 teachings from Jesus, organized into:

1. **The Beatitudes** (Matthew 5:3-12) - 7 quotes
2. **The Great Commandments** - 2 quotes
3. **"I Am" Statements** (John's Gospel) - 7 quotes
4. **Love and Forgiveness** - 4 quotes
5. **Faith and Prayer** - 5 quotes
6. **Humility and Service** - 3 quotes
7. **Worry and Trust** - 3 quotes
8. **Kingdom of God** - 3 quotes
9. **Truth and Light** - 3 quotes
10. **Following Jesus** - 3 quotes
11. **Final Commands** - 2 quotes

### Example Helper Scripts

#### Create Quote Files

```bash
# Create all example quote files
python examples.py create-files

# This creates:
# - examples/beatitudes.txt
# - examples/love_quotes.txt
# - examples/faith_quotes.txt
# - examples/kingdom_quotes.txt
# - examples/i_am_statements.txt
# - examples/daily_devotional.txt
```

#### Interactive Quote Browser

```bash
python examples.py interactive
```

#### Show Example Commands

```bash
python examples.py examples
```

## Advanced Usage

### Multi-Quote Videos

Add multiple quotes distributed throughout a video:

```bash
# First, create a quotes file
cat > my_quotes.txt << EOF
Love your enemies - Matthew 5:44
Do to others as you would have them do to you - Luke 6:31
Peace be with you - John 20:21
EOF

# Apply to video
python video_editor.py input.mp4 output.mp4 --quote-file my_quotes.txt
```

The quotes will be automatically distributed evenly throughout the video.

### Complex Example: Complete Video Production

```bash
# Create a video with intro, multiple quotes, and outro
python video_editor.py chosen_episode.mp4 chosen_edited.mp4 \
  --intro "Episode 3: Jesus Calls Matthew" \
  --quote-file examples/daily_devotional.txt \
  --font-size 55 \
  --font-color gold \
  --position bottom \
  --outro "To be continued..."
```

### Timed Quote Insertion

Add a quote at a specific timestamp:

```bash
# Add quote starting at 2 minutes (120 seconds) for 8 seconds
python video_editor.py sermon.mp4 sermon_edited.mp4 \
  --text "Blessed are the pure in heart - Matthew 5:8" \
  --start-time 120 \
  --duration 8 \
  --font-size 65
```

### Batch Processing

Process multiple videos with a shell script:

```bash
#!/bin/bash
# batch_process.sh

for video in videos/*.mp4; do
  filename=$(basename "$video" .mp4)
  python video_editor.py "$video" "output/${filename}_edited.mp4" \
    --intro "Daily Devotional" \
    --text "$(python -c 'from biblical_quotes import get_random_quote; print(get_random_quote())')" \
    --outro "God bless you"
done
```

### Python API Usage

You can also use the editor as a Python library:

```python
from video_editor import BiblicalVideoEditor
from biblical_quotes import get_random_quote

# Create editor instance
editor = BiblicalVideoEditor('input.mp4', 'output.mp4')

# Load video
editor.load_video()

# Add intro
editor.add_intro_text('Welcome', duration=3)

# Add text overlay
editor.add_text_overlay(
    text=get_random_quote(),
    position=('center', 'bottom'),
    duration=8,
    start_time=10,
    font_size=60,
    font_color='white'
)

# Add outro
editor.add_outro_text('Amen', duration=3)

# Save and cleanup
editor.save_video()
editor.cleanup()
```

## Tips and Best Practices

### Text Readability

1. **Font Size**: Use 40-80 for best readability
   - Small videos (480p): 40-50
   - Medium videos (720p): 50-60
   - Large videos (1080p+): 60-80

2. **Duration**: Allow 5-8 seconds per quote for viewers to read comfortably

3. **Contrast**: Ensure text color contrasts well with video background
   - Light backgrounds: Use dark text (black, navy)
   - Dark backgrounds: Use light text (white, gold, yellow)
   - Mixed backgrounds: Use text with semi-transparent background

4. **Position**:
   - `bottom`: Best for most content (doesn't block main action)
   - `center`: Good for emphasis or simple backgrounds
   - `top`: Use sparingly, can feel intrusive

### Video Quality

1. **Test First**: Always test with a short clip before processing long videos
2. **Codec Settings**: Default settings balance quality and file size
3. **Processing Time**: Expect 1-2x real-time (10 min video = 10-20 min processing)

### Quote Selection

1. **Context Matters**: Choose quotes that relate to video content
2. **Length**: Keep quotes concise (under 100 characters ideal)
3. **Themes**: Group related quotes for cohesive messaging

### Performance Tips

1. **Use shorter clips for testing**
2. **Process in batches overnight for many videos**
3. **Consider video resolution** - lower resolution processes faster

## Troubleshooting

### Common Issues

#### "No module named 'moviepy'"

**Solution:**
```bash
pip install -r requirements.txt
```

#### "MoviePy Error: Failed to read text"

**Cause:** ImageMagick not installed or not in PATH

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install imagemagick

# macOS
brew install imagemagick

# Windows: Reinstall ImageMagick with legacy utilities
```

#### Video processing is very slow

**Solutions:**
1. Use a shorter test video first
2. Reduce video resolution
3. Close other applications
4. Consider using a more powerful computer for large videos

#### Text doesn't appear in video

**Possible causes and solutions:**
1. **Wrong font**: Try using 'Arial' or another common font
2. **Color issue**: Text might be same color as background
3. **ImageMagick issue**: Reinstall ImageMagick
4. **Timing**: Check start-time and duration settings

#### "Input file not found"

**Solution:**
- Use absolute paths: `/home/user/videos/input.mp4`
- Or ensure you're in the correct directory
- Verify file exists: `ls -l input.mp4`

#### Audio is out of sync

**Solution:**
- This is rare with default settings
- Try re-encoding the input video first:
```bash
ffmpeg -i input.mp4 -c:v libx264 -c:a aac input_reencoded.mp4
```

### Getting Help

1. **Check documentation**: `python video_editor.py --help`
2. **View examples**: `python examples.py examples`
3. **Test components**: `python biblical_quotes.py`
4. **Report issues**: Open an issue on GitHub with:
   - Python version
   - OS and version
   - Error message
   - Command you ran

### Debug Mode

For verbose output, you can modify the script or add print statements to see what's happening at each step.

## System Requirements

### Minimum
- CPU: Dual-core processor
- RAM: 4 GB
- Storage: 1 GB free space
- OS: Linux, macOS, or Windows

### Recommended
- CPU: Quad-core or better
- RAM: 8 GB or more
- Storage: 10 GB free space (for video processing)
- OS: Linux or macOS (better performance)

### Video Formats

**Supported Input:**
- MP4, AVI, MOV, MKV, FLV, WMV, and most common formats

**Output:**
- MP4 (H.264 video, AAC audio)

## Performance Benchmarks

Approximate processing times on a mid-range laptop:

| Video Length | Resolution | Processing Time |
|--------------|------------|-----------------|
| 1 minute | 720p | 1-2 minutes |
| 5 minutes | 720p | 5-10 minutes |
| 10 minutes | 1080p | 15-25 minutes |
| 30 minutes | 1080p | 45-90 minutes |

*Note: Times vary based on CPU, effects used, and system load*

## Next Steps

1. **Start Simple**: Try adding a single quote to a short video
2. **Explore Quotes**: Use `python examples.py interactive` to browse available quotes
3. **Create Custom Collections**: Make your own quote files for specific themes
4. **Share**: Create inspirational content to share on social media or with your community

---

For more information, see the main [README.md](README.md) file.

*"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." - Matthew 5:16*
