# Biblical Video Editor (Lj)

A Python-based video editing tool to incorporate teachings of Jesus Christ into video content. Perfect for creating inspirational videos with biblical quotes, verses, and teachings.

## Features

- 🎬 **Video Editing**: Add text overlays, intros, and outros to video files
- 📖 **Biblical Quotes**: Built-in database of 40+ teachings from Jesus Christ
- 🎨 **Customizable Text**: Control font size, color, position, and timing
- 🎥 **Professional Effects**: Automatic fade in/out transitions
- 🖥️ **Command-Line Interface**: Easy-to-use CLI with multiple options
- 📝 **Batch Processing**: Add multiple quotes from a file
- 🎞️ **Universal Compatibility**: Works with MP4, AVI, MOV, and other video formats

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ljbudgie/Lj.git
cd Lj
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

3. **Install ImageMagick (required for text rendering):**

**Ubuntu/Debian:**
```bash
sudo apt-get install imagemagick
```

**macOS (with Homebrew):**
```bash
brew install imagemagick
```

**Windows:**
Download and install from [ImageMagick website](https://imagemagick.org/script/download.php)

## Quick Start

### Basic Usage

Add a simple text overlay to a video:
```bash
python video_editor.py input.mp4 output.mp4 --text "Love your neighbor as yourself - Matthew 22:39"
```

### Add Intro and Outro

```bash
python video_editor.py input.mp4 output.mp4 \
  --intro "The Teachings of Jesus" \
  --outro "Go and spread the Good News"
```

### Customize Text Appearance

```bash
python video_editor.py input.mp4 output.mp4 \
  --text "Blessed are the peacemakers - Matthew 5:9" \
  --font-size 60 \
  --font-color yellow \
  --position center
```

### Add Text at Specific Time

```bash
python video_editor.py input.mp4 output.mp4 \
  --text "I am the way, the truth, and the life - John 14:6" \
  --start-time 10 \
  --duration 5
```

### Use Multiple Quotes from a File

First, create a quotes file (e.g., `my_quotes.txt`):
```text
Love your enemies - Matthew 5:44
Do to others as you would have them do to you - Luke 6:31
Peace be with you - John 20:21
```

Then apply all quotes:
```bash
python video_editor.py input.mp4 output.mp4 --quote-file my_quotes.txt
```

## Biblical Quotes Database

The project includes a comprehensive database of Jesus's teachings from the Gospels:

### Use the Quotes Database

```python
from biblical_quotes import get_random_quote, get_all_quotes, get_quotes_by_theme

# Get a random quote
quote = get_random_quote()

# Get all quotes
all_quotes = get_all_quotes()

# Get quotes by theme
love_quotes = get_quotes_by_theme('love')
faith_quotes = get_quotes_by_theme('faith')

# Save quotes to a file
from biblical_quotes import save_quotes_to_file
save_quotes_to_file('beatitudes.txt', get_beatitudes())
```

### Quote Categories

The database includes:
- **The Beatitudes** (Matthew 5:3-12)
- **The Great Commandments** (Love God and neighbor)
- **I Am Statements** (John's Gospel)
- **Teachings on Love and Forgiveness**
- **Teachings on Faith and Prayer**
- **Teachings on Humility and Service**
- **Teachings on Worry and Trust**
- **Parables and Wisdom**

## Command-Line Options

```
usage: video_editor.py [-h] [--text TEXT] [--intro INTRO] [--outro OUTRO]
                       [--start-time START_TIME] [--duration DURATION]
                       [--font-size FONT_SIZE] [--font-color FONT_COLOR]
                       [--bg-color BG_COLOR] [--position {top,center,bottom}]
                       [--quote-file QUOTE_FILE]
                       input output

positional arguments:
  input                 Input video file path
  output                Output video file path

optional arguments:
  -h, --help            Show this help message and exit
  --text TEXT, -t TEXT
                        Text overlay to add to the video (biblical quote)
  --intro INTRO, -i INTRO
                        Intro text to display before the video
  --outro OUTRO, -o OUTRO
                        Outro text to display after the video
  --start-time START_TIME, -s START_TIME
                        Start time for text overlay in seconds (default: 0)
  --duration DURATION, -d DURATION
                        Duration for text overlay in seconds (default: entire video)
  --font-size FONT_SIZE, -fs FONT_SIZE
                        Font size for text overlay (default: 50)
  --font-color FONT_COLOR, -fc FONT_COLOR
                        Font color for text (default: white)
  --bg-color BG_COLOR, -bg BG_COLOR
                        Background color for text (default: transparent)
  --position {top,center,bottom}
                        Position of text overlay (default: bottom)
  --quote-file QUOTE_FILE, -q QUOTE_FILE
                        File containing biblical quotes (one per line)
```

## Example Workflows

### Creating Inspirational Content

For content creators making inspirational videos (e.g., from "The Chosen" series):

```bash
# Add an intro with the episode theme
python video_editor.py chosen_ep1.mp4 chosen_ep1_edited.mp4 \
  --intro "Episode 1: Jesus Calls His Disciples" \
  --text "Come, follow me, and I will make you fishers of men - Matthew 4:19" \
  --start-time 30 \
  --duration 8

# Add multiple relevant quotes throughout
python video_editor.py sermon_video.mp4 sermon_edited.mp4 \
  --quote-file sermon_quotes.txt \
  --font-size 55 \
  --position bottom
```

### Educational Content

For Sunday school or Bible study materials:

```bash
# Create a video with beatitudes
python -c "from biblical_quotes import get_beatitudes, save_quotes_to_file; \
  save_quotes_to_file('beatitudes.txt', get_beatitudes())"

python video_editor.py background_video.mp4 beatitudes_video.mp4 \
  --intro "The Beatitudes - Sermon on the Mount" \
  --quote-file beatitudes.txt \
  --outro "Matthew 5:3-12"
```

## Project Structure

```
Lj/
├── video_editor.py       # Main video editing script
├── biblical_quotes.py    # Database of biblical teachings
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── examples/            # Example videos and configurations (optional)
```

## Technical Details

### Dependencies

- **moviepy**: Video editing library (handles video/audio processing)
- **ImageMagick**: Required for text rendering
- **numpy**: Numerical operations
- **Pillow**: Image processing

### Video Codecs

The editor uses:
- Video codec: `libx264` (H.264)
- Audio codec: `aac`
- Preset: `medium` (balanced quality/speed)

### Text Effects

All text overlays automatically include:
- 0.5s fade-in effect
- 0.5s fade-out effect
- Centered alignment
- Caption method for proper text wrapping

## Use Cases

### Content Creators
- Add biblical context to sermon videos
- Create social media inspirational clips
- Enhance "The Chosen" or other biblical film content

### Churches & Ministries
- Create worship service videos with scripture
- Produce educational materials for Bible studies
- Share weekly devotional videos

### Personal Use
- Create personalized scripture meditation videos
- Compile favorite teachings into video format
- Share inspirational content with friends and family

## Troubleshooting

### ImportError: No module named 'moviepy'
Install dependencies:
```bash
pip install -r requirements.txt
```

### OSError: MoviePy Error: Failed to read text
Install ImageMagick:
- Ubuntu/Debian: `sudo apt-get install imagemagick`
- macOS: `brew install imagemagick`
- Windows: Download from ImageMagick website

### Video processing is slow
- Use shorter videos for testing
- Consider using a lower resolution input video
- The script uses 4 threads by default for encoding

### Text doesn't appear
- Check if ImageMagick is properly installed
- Try using a different font (Arial is default)
- Verify the text color contrasts with the video

## Contributing

Contributions are welcome! Feel free to:
- Add more biblical quotes to the database
- Improve text rendering effects
- Add new features (transitions, filters, etc.)
- Report bugs or suggest improvements

## License

This project is open source and available for use in spreading the Gospel.

## Credits

- Biblical quotes are from the New International Version (NIV) of the Bible
- Built with Python and MoviePy
- Created with the purpose of sharing Jesus's teachings through modern media

## Contact

For questions, suggestions, or support, please open an issue on GitHub.

---

*"Let your light shine before others, that they may see your good deeds and glorify your Father in heaven." - Matthew 5:16*