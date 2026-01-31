#!/usr/bin/env python3
"""
Example demonstrating Python API usage of Biblical Video Editor

This shows how to use the video editor as a Python library
instead of just a command-line tool.

Note: This requires moviepy to be installed:
    pip install -r requirements.txt
"""

from biblical_quotes import (
    get_random_quote,
    get_beatitudes,
    get_quotes_by_theme,
)

# Example 1: Simple usage
def simple_example():
    """Basic example - add a quote to a video"""
    from video_editor import BiblicalVideoEditor
    
    # Create editor
    editor = BiblicalVideoEditor('input.mp4', 'output.mp4')
    
    # Load, edit, and save
    editor.load_video()
    editor.add_text_overlay(
        text="Love your neighbor as yourself - Matthew 22:39",
        position=('center', 'bottom'),
        font_size=60
    )
    editor.save_video()
    editor.cleanup()
    
    print("✓ Simple example completed!")


# Example 2: Complete video with intro, quotes, and outro
def complete_example():
    """Complete example with multiple elements"""
    from video_editor import BiblicalVideoEditor
    
    editor = BiblicalVideoEditor('input.mp4', 'output.mp4')
    
    # Load video
    editor.load_video()
    
    # Add intro
    editor.add_intro_text(
        text="The Teachings of Jesus Christ",
        duration=5.0,
        font_size=70
    )
    
    # Add main quote
    editor.add_text_overlay(
        text=get_random_quote(),
        position=('center', 'bottom'),
        duration=8.0,
        start_time=10.0,
        font_size=55,
        font_color='gold'
    )
    
    # Add outro
    editor.add_outro_text(
        text="Go and spread the Good News",
        duration=4.0
    )
    
    # Save
    editor.save_video()
    editor.cleanup()
    
    print("✓ Complete example finished!")


# Example 3: Multiple quotes at different times
def multiple_quotes_example():
    """Add multiple quotes at specific timestamps"""
    from video_editor import BiblicalVideoEditor
    
    editor = BiblicalVideoEditor('long_video.mp4', 'output.mp4')
    editor.load_video()
    
    # Get beatitudes
    beatitudes = get_beatitudes()
    
    # Add each beatitude at 30-second intervals
    for idx, quote in enumerate(beatitudes):
        start_time = idx * 30
        editor.add_text_overlay(
            text=quote,
            position=('center', 'bottom'),
            duration=8.0,
            start_time=start_time,
            font_size=50
        )
    
    editor.save_video()
    editor.cleanup()
    
    print(f"✓ Added {len(beatitudes)} quotes to video!")


# Example 4: Theme-based video
def theme_video_example():
    """Create a video focused on a specific theme"""
    from video_editor import BiblicalVideoEditor
    
    # Get love-themed quotes
    love_quotes = get_quotes_by_theme('love')
    
    editor = BiblicalVideoEditor('nature_scene.mp4', 'love_video.mp4')
    editor.load_video()
    
    # Add intro
    editor.add_intro_text("Jesus Teaches About Love", duration=4)
    
    # Distribute love quotes throughout video
    video_duration = editor.video_clip.duration
    interval = video_duration / (len(love_quotes) + 1)
    
    for idx, quote in enumerate(love_quotes):
        editor.add_text_overlay(
            text=quote,
            start_time=interval * (idx + 1),
            duration=7.0,
            font_size=55,
            font_color='white'
        )
    
    editor.add_outro_text("Love one another", duration=3)
    
    editor.save_video()
    editor.cleanup()
    
    print(f"✓ Created love-themed video with {len(love_quotes)} quotes!")


# Example 5: Batch processing multiple videos
def batch_processing_example():
    """Process multiple videos with different quotes"""
    import glob
    from video_editor import BiblicalVideoEditor
    
    # Get all mp4 files in input directory
    video_files = glob.glob('input_videos/*.mp4')
    
    for video_file in video_files:
        # Generate output filename
        output_file = video_file.replace('input_videos/', 'output_videos/')
        output_file = output_file.replace('.mp4', '_edited.mp4')
        
        print(f"Processing: {video_file}")
        
        # Create editor
        editor = BiblicalVideoEditor(video_file, output_file)
        editor.load_video()
        
        # Add random quote
        editor.add_text_overlay(
            text=get_random_quote(),
            position=('center', 'bottom'),
            font_size=50
        )
        
        editor.save_video()
        editor.cleanup()
        
        print(f"✓ Saved: {output_file}")
    
    print(f"\n✓ Processed {len(video_files)} videos!")


# Example 6: Custom positioning and styling
def custom_styling_example():
    """Demonstrate custom text positioning and styling"""
    from video_editor import BiblicalVideoEditor
    
    editor = BiblicalVideoEditor('input.mp4', 'styled_output.mp4')
    editor.load_video()
    
    # Top-positioned quote with custom colors
    editor.add_text_overlay(
        text="I am the way, the truth, and the life - John 14:6",
        position=('center', 50),  # 50 pixels from top
        duration=10.0,
        font_size=65,
        font_color='yellow',
        bg_color='rgba(0, 0, 0, 0.7)'  # Semi-transparent black background
    )
    
    # Center-positioned quote
    editor.add_text_overlay(
        text="Blessed are the peacemakers - Matthew 5:9",
        position=('center', 'center'),
        start_time=15.0,
        duration=8.0,
        font_size=70,
        font_color='white'
    )
    
    editor.save_video()
    editor.cleanup()
    
    print("✓ Custom styling example completed!")


# Main function to show available examples
def main():
    """Show available examples"""
    print("\n" + "="*60)
    print("BIBLICAL VIDEO EDITOR - PYTHON API EXAMPLES")
    print("="*60)
    print("\nAvailable examples:")
    print("1. simple_example() - Basic usage")
    print("2. complete_example() - Intro + quote + outro")
    print("3. multiple_quotes_example() - Multiple quotes at intervals")
    print("4. theme_video_example() - Theme-based video")
    print("5. batch_processing_example() - Process multiple videos")
    print("6. custom_styling_example() - Custom positioning/styling")
    print("\nUsage:")
    print("  from python_api_examples import simple_example")
    print("  simple_example()")
    print("\nNote: Requires actual video files and moviepy installed")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
