#!/usr/bin/env python3
"""
Example script demonstrating advanced usage of the Biblical Video Editor
"""

import os
from biblical_quotes import (
    get_all_quotes,
    get_beatitudes,
    get_quotes_by_theme,
    save_quotes_to_file,
    get_random_quote
)


def create_example_quote_files():
    """Create example quote files for different themes"""
    
    # Create output directory
    os.makedirs('examples', exist_ok=True)
    
    # Save all beatitudes
    print("Creating beatitudes.txt...")
    save_quotes_to_file('examples/beatitudes.txt', get_beatitudes())
    
    # Save quotes about love
    print("Creating love_quotes.txt...")
    love_quotes = get_quotes_by_theme('love')
    save_quotes_to_file('examples/love_quotes.txt', love_quotes)
    
    # Save quotes about faith
    print("Creating faith_quotes.txt...")
    faith_quotes = get_quotes_by_theme('faith')
    save_quotes_to_file('examples/faith_quotes.txt', faith_quotes)
    
    # Save quotes about kingdom
    print("Creating kingdom_quotes.txt...")
    kingdom_quotes = get_quotes_by_theme('kingdom')
    save_quotes_to_file('examples/kingdom_quotes.txt', kingdom_quotes)
    
    # Save "I am" statements
    print("Creating i_am_statements.txt...")
    i_am_quotes = [q for q in get_all_quotes() if "I am" in q]
    save_quotes_to_file('examples/i_am_statements.txt', i_am_quotes)
    
    # Create a short devotional set
    print("Creating daily_devotional.txt...")
    devotional_quotes = [
        "Blessed are the peacemakers, for they will be called children of God. - Matthew 5:9",
        "Love your neighbor as yourself. - Matthew 22:39",
        "I am the light of the world. Whoever follows me will never walk in darkness. - John 8:12",
        "Come to me, all you who are weary and burdened, and I will give you rest. - Matthew 11:28",
        "Peace I leave with you; my peace I give you. - John 14:27",
    ]
    save_quotes_to_file('examples/daily_devotional.txt', devotional_quotes)
    
    print("\n✓ All example quote files created in 'examples/' directory")
    print("\nYou can now use these files with the video editor:")
    print("  python video_editor.py input.mp4 output.mp4 --quote-file examples/beatitudes.txt")


def show_example_commands():
    """Display example command-line usages"""
    
    examples = """
    
    BIBLICAL VIDEO EDITOR - EXAMPLE COMMANDS
    ========================================
    
    1. SIMPLE TEXT OVERLAY
       Add a single quote to your video:
       
       python video_editor.py input.mp4 output.mp4 \\
         --text "Love your neighbor as yourself - Matthew 22:39"
    
    
    2. INTRO + TEXT + OUTRO
       Create a complete video with intro and outro:
       
       python video_editor.py input.mp4 output.mp4 \\
         --intro "The Teachings of Jesus Christ" \\
         --text "Blessed are the merciful - Matthew 5:7" \\
         --outro "Go in Peace"
    
    
    3. CUSTOMIZED TEXT APPEARANCE
       Control the look of your text:
       
       python video_editor.py input.mp4 output.mp4 \\
         --text "I am the way, the truth, and the life - John 14:6" \\
         --font-size 70 \\
         --font-color gold \\
         --position center
    
    
    4. TIMED TEXT OVERLAY
       Add text at a specific moment:
       
       python video_editor.py input.mp4 output.mp4 \\
         --text "Peace be with you - John 20:21" \\
         --start-time 15 \\
         --duration 7
    
    
    5. MULTIPLE QUOTES FROM FILE
       Add several quotes distributed throughout the video:
       
       python video_editor.py input.mp4 output.mp4 \\
         --quote-file examples/beatitudes.txt \\
         --font-size 55
    
    
    6. SOCIAL MEDIA SHORT CLIP
       Perfect for Instagram or TikTok:
       
       python video_editor.py short_video.mp4 inspirational.mp4 \\
         --intro "Daily Inspiration" \\
         --text "Let your light shine before others - Matthew 5:16" \\
         --font-size 45 \\
         --position center \\
         --outro "Share the Light"
    
    
    7. SERMON ENHANCEMENT
       Add scripture references to sermon videos:
       
       python video_editor.py sermon.mp4 sermon_edited.mp4 \\
         --intro "Today's Message: Love and Forgiveness" \\
         --text "Love your enemies and pray for those who persecute you - Matthew 5:44" \\
         --start-time 600 \\
         --duration 10
    
    
    8. WORSHIP/MEDITATION VIDEO
       Create a peaceful meditation video:
       
       python video_editor.py nature_scene.mp4 meditation.mp4 \\
         --intro "Be Still and Know" \\
         --quote-file examples/daily_devotional.txt \\
         --font-size 50 \\
         --font-color white \\
         --outro "Peace be with you"
    
    
    9. THE CHOSEN SERIES ENHANCEMENT
       Add relevant quotes to episodes:
       
       python video_editor.py chosen_clip.mp4 chosen_enhanced.mp4 \\
         --text "Come, follow me - Matthew 4:19" \\
         --start-time 120 \\
         --duration 6 \\
         --position bottom
    
    
    10. BATCH PROCESSING EXAMPLE (using a shell script)
        Process multiple videos with different themes:
        
        for theme in love faith peace; do
          python video_editor.py input_${theme}.mp4 output_${theme}.mp4 \\
            --quote-file examples/${theme}_quotes.txt
        done
    
    
    TIPS:
    -----
    • Use --position top/center/bottom to control text placement
    • Font colors: white, black, yellow, red, blue, gold, etc.
    • Background colors: transparent, black, rgba(0,0,0,0.7) for semi-transparent
    • Keep font sizes between 40-80 for best readability
    • Allow 5-8 seconds duration for viewers to read quotes
    • Test with short clips before processing long videos
    
    """
    
    print(examples)


def interactive_quote_selector():
    """Interactive tool to help select quotes"""
    
    print("\n" + "="*60)
    print("INTERACTIVE QUOTE SELECTOR")
    print("="*60)
    
    all_quotes = get_all_quotes()
    
    print(f"\nTotal available quotes: {len(all_quotes)}")
    print("\nOptions:")
    print("1. Show all quotes")
    print("2. Show quotes by theme (love, faith, peace, etc.)")
    print("3. Get random quote")
    print("4. Show beatitudes")
    print("5. Show 'I am' statements")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\nALL QUOTES:")
            print("-" * 60)
            for i, quote in enumerate(all_quotes, 1):
                print(f"{i}. {quote}")
        
        elif choice == '2':
            theme = input("Enter theme (love/faith/peace/kingdom/etc.): ").strip()
            quotes = get_quotes_by_theme(theme)
            if quotes:
                print(f"\nQUOTES ABOUT '{theme.upper()}':")
                print("-" * 60)
                for i, quote in enumerate(quotes, 1):
                    print(f"{i}. {quote}")
            else:
                print(f"No quotes found for theme: {theme}")
        
        elif choice == '3':
            print("\nRANDOM QUOTE:")
            print("-" * 60)
            print(get_random_quote())
        
        elif choice == '4':
            beatitudes = get_beatitudes()
            print(f"\nTHE BEATITUDES ({len(beatitudes)} quotes):")
            print("-" * 60)
            for i, quote in enumerate(beatitudes, 1):
                print(f"{i}. {quote}")
        
        elif choice == '5':
            i_am = [q for q in all_quotes if "I am" in q]
            print(f"\n'I AM' STATEMENTS ({len(i_am)} quotes):")
            print("-" * 60)
            for i, quote in enumerate(i_am, 1):
                print(f"{i}. {quote}")
        
        elif choice == '6':
            print("\nGoodbye! God bless you!")
            break
        
        else:
            print("Invalid choice. Please enter 1-6.")


def main():
    """Main function"""
    import sys
    
    print("\n" + "="*60)
    print("BIBLICAL VIDEO EDITOR - EXAMPLES AND UTILITIES")
    print("="*60)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'create-files':
            create_example_quote_files()
        elif command == 'examples':
            show_example_commands()
        elif command == 'interactive':
            interactive_quote_selector()
        else:
            print(f"Unknown command: {command}")
            print_usage()
    else:
        print_usage()


def print_usage():
    """Print usage information"""
    print("""
Usage: python examples.py [command]

Commands:
  create-files    Create example quote files in examples/ directory
  examples        Show example command-line usages
  interactive     Interactive quote selector and browser
  
Examples:
  python examples.py create-files
  python examples.py examples
  python examples.py interactive
  
For video editing help:
  python video_editor.py --help
    """)


if __name__ == '__main__':
    main()
