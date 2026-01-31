#!/usr/bin/env python3
"""
Biblical Video Editor - Edit videos with teachings of Jesus Christ
Author: ljbudgie
Description: A script to add biblical quotes, verses, and teachings to video files
"""

import argparse
import sys
import os
from typing import List, Tuple, Optional
from pathlib import Path

try:
    from moviepy.editor import (
        VideoFileClip,
        TextClip,
        CompositeVideoClip,
        concatenate_videoclips,
    )
    from moviepy.video.fx import fadein, fadeout
except ImportError:
    print("Error: moviepy is not installed. Install it with: pip install moviepy")
    sys.exit(1)


class BiblicalVideoEditor:
    """Main class for editing videos with biblical content"""

    def __init__(self, input_video: str, output_video: str):
        """
        Initialize the video editor
        
        Args:
            input_video: Path to input video file
            output_video: Path to output video file
        """
        self.input_video = input_video
        self.output_video = output_video
        self.video_clip = None
        
        # Validate input file exists
        if not os.path.exists(input_video):
            raise FileNotFoundError(f"Input video not found: {input_video}")
    
    def load_video(self) -> VideoFileClip:
        """Load the input video file"""
        print(f"Loading video: {self.input_video}")
        self.video_clip = VideoFileClip(self.input_video)
        print(f"Video loaded: {self.video_clip.duration:.2f} seconds, "
              f"{self.video_clip.size[0]}x{self.video_clip.size[1]} resolution")
        return self.video_clip
    
    def add_text_overlay(
        self,
        text: str,
        position: Tuple[int, int] = ('center', 'bottom'),
        duration: Optional[float] = None,
        start_time: float = 0,
        font_size: int = 50,
        font_color: str = 'white',
        bg_color: str = 'transparent',
        font: str = 'Arial',
    ) -> CompositeVideoClip:
        """
        Add text overlay to the video
        
        Args:
            text: Text to display
            position: Position of text (default: center bottom)
            duration: Duration to display text (None = entire video)
            start_time: When to start showing text
            font_size: Size of the font
            font_color: Color of the text
            bg_color: Background color (use 'transparent' for no background)
            font: Font family name
            
        Returns:
            CompositeVideoClip with text overlay
        """
        if self.video_clip is None:
            raise ValueError("Video not loaded. Call load_video() first.")
        
        # Set duration to remaining video time if not specified
        if duration is None:
            duration = self.video_clip.duration - start_time
        
        print(f"Adding text overlay: '{text[:50]}...' at {start_time}s for {duration}s")
        
        # Create text clip
        txt_clip = TextClip(
            text,
            fontsize=font_size,
            color=font_color,
            font=font,
            size=self.video_clip.size,
            method='caption',
            align='center',
            bg_color=bg_color if bg_color != 'transparent' else None,
        )
        
        # Set position and timing
        txt_clip = txt_clip.set_position(position).set_duration(duration).set_start(start_time)
        
        # Add fade in/out effects
        txt_clip = fadein(txt_clip, 0.5)
        txt_clip = fadeout(txt_clip, 0.5)
        
        # Composite video with text
        self.video_clip = CompositeVideoClip([self.video_clip, txt_clip])
        
        return self.video_clip
    
    def add_intro_text(
        self,
        text: str,
        duration: float = 5.0,
        font_size: int = 70,
        bg_color: str = 'black',
    ) -> VideoFileClip:
        """
        Add an intro text clip before the main video
        
        Args:
            text: Intro text to display
            duration: Duration of intro
            font_size: Font size for intro
            bg_color: Background color
            
        Returns:
            Combined video with intro
        """
        if self.video_clip is None:
            raise ValueError("Video not loaded. Call load_video() first.")
        
        print(f"Adding intro text: '{text}' ({duration}s)")
        
        # Create intro text clip
        intro_clip = TextClip(
            text,
            fontsize=font_size,
            color='white',
            font='Arial',
            size=self.video_clip.size,
            method='caption',
            align='center',
            bg_color=bg_color,
        ).set_duration(duration)
        
        # Add fade effects
        intro_clip = fadein(intro_clip, 1.0)
        intro_clip = fadeout(intro_clip, 1.0)
        
        # Concatenate intro with main video
        self.video_clip = concatenate_videoclips([intro_clip, self.video_clip])
        
        return self.video_clip
    
    def add_outro_text(
        self,
        text: str,
        duration: float = 5.0,
        font_size: int = 70,
        bg_color: str = 'black',
    ) -> VideoFileClip:
        """
        Add an outro text clip after the main video
        
        Args:
            text: Outro text to display
            duration: Duration of outro
            font_size: Font size for outro
            bg_color: Background color
            
        Returns:
            Combined video with outro
        """
        if self.video_clip is None:
            raise ValueError("Video not loaded. Call load_video() first.")
        
        print(f"Adding outro text: '{text}' ({duration}s)")
        
        # Create outro text clip
        outro_clip = TextClip(
            text,
            fontsize=font_size,
            color='white',
            font='Arial',
            size=self.video_clip.size,
            method='caption',
            align='center',
            bg_color=bg_color,
        ).set_duration(duration)
        
        # Add fade effects
        outro_clip = fadein(outro_clip, 1.0)
        outro_clip = fadeout(outro_clip, 1.0)
        
        # Concatenate main video with outro
        self.video_clip = concatenate_videoclips([self.video_clip, outro_clip])
        
        return self.video_clip
    
    def save_video(self, codec: str = 'libx264', audio_codec: str = 'aac', fps: Optional[int] = None):
        """
        Save the edited video to output file
        
        Args:
            codec: Video codec to use
            audio_codec: Audio codec to use
            fps: Frames per second (None = use original)
        """
        if self.video_clip is None:
            raise ValueError("Video not loaded. Call load_video() first.")
        
        print(f"Saving video to: {self.output_video}")
        print("This may take a while depending on video length and quality...")
        
        # Use original fps if not specified
        if fps is None:
            fps = self.video_clip.fps
        
        # Write video file
        self.video_clip.write_videofile(
            self.output_video,
            codec=codec,
            audio_codec=audio_codec,
            fps=fps,
            preset='medium',
            threads=4,
        )
        
        print(f"Video saved successfully: {self.output_video}")
    
    def cleanup(self):
        """Clean up resources"""
        if self.video_clip is not None:
            self.video_clip.close()
            print("Resources cleaned up")


def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Biblical Video Editor - Add teachings of Jesus Christ to videos',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Add a simple text overlay
  python video_editor.py input.mp4 output.mp4 --text "Love your neighbor as yourself - Matthew 22:39"
  
  # Add intro and outro
  python video_editor.py input.mp4 output.mp4 --intro "The Teachings of Jesus" --outro "Go and spread the Good News"
  
  # Add text overlay at specific time
  python video_editor.py input.mp4 output.mp4 --text "I am the way, the truth, and the life - John 14:6" --start-time 10 --duration 5
  
  # Combine multiple options
  python video_editor.py input.mp4 output.mp4 --intro "Jesus Said..." --text "Blessed are the peacemakers - Matthew 5:9" --outro "Amen"
        """
    )
    
    parser.add_argument('input', help='Input video file path')
    parser.add_argument('output', help='Output video file path')
    parser.add_argument(
        '--text', '-t',
        help='Text overlay to add to the video (biblical quote or teaching)',
        default=None
    )
    parser.add_argument(
        '--intro', '-i',
        help='Intro text to display before the video',
        default=None
    )
    parser.add_argument(
        '--outro', '-o',
        help='Outro text to display after the video',
        default=None
    )
    parser.add_argument(
        '--start-time', '-s',
        type=float,
        default=0,
        help='Start time for text overlay in seconds (default: 0)'
    )
    parser.add_argument(
        '--duration', '-d',
        type=float,
        default=None,
        help='Duration for text overlay in seconds (default: entire video)'
    )
    parser.add_argument(
        '--font-size', '-fs',
        type=int,
        default=50,
        help='Font size for text overlay (default: 50)'
    )
    parser.add_argument(
        '--font-color', '-fc',
        default='white',
        help='Font color for text (default: white)'
    )
    parser.add_argument(
        '--bg-color', '-bg',
        default='transparent',
        help='Background color for text (default: transparent)'
    )
    parser.add_argument(
        '--position',
        default='bottom',
        choices=['top', 'center', 'bottom'],
        help='Position of text overlay (default: bottom)'
    )
    parser.add_argument(
        '--quote-file', '-q',
        help='File containing biblical quotes (one per line)',
        default=None
    )
    
    return parser.parse_args()


def main():
    """Main function"""
    args = parse_arguments()
    
    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Check if at least one editing option is provided
    if not any([args.text, args.intro, args.outro, args.quote_file]):
        print("Warning: No text overlay, intro, or outro specified. Creating a copy of the input video.")
        print("Use --help to see available options.")
    
    try:
        # Initialize editor
        editor = BiblicalVideoEditor(args.input, args.output)
        
        # Load video
        editor.load_video()
        
        # Add intro if specified
        if args.intro:
            editor.add_intro_text(args.intro)
        
        # Add text overlay if specified
        if args.text:
            position_map = {
                'top': ('center', 50),
                'center': ('center', 'center'),
                'bottom': ('center', 'bottom'),
            }
            position = position_map.get(args.position, ('center', 'bottom'))
            
            editor.add_text_overlay(
                text=args.text,
                position=position,
                duration=args.duration,
                start_time=args.start_time,
                font_size=args.font_size,
                font_color=args.font_color,
                bg_color=args.bg_color,
            )
        
        # Add quotes from file if specified
        if args.quote_file:
            if os.path.exists(args.quote_file):
                with open(args.quote_file, 'r') as f:
                    quotes = [line.strip() for line in f if line.strip()]
                
                # Distribute quotes evenly across the video
                video_duration = editor.video_clip.duration
                interval = video_duration / (len(quotes) + 1)
                
                for idx, quote in enumerate(quotes):
                    start_time = interval * (idx + 1)
                    editor.add_text_overlay(
                        text=quote,
                        position=('center', 'bottom'),
                        duration=5.0,
                        start_time=start_time,
                        font_size=args.font_size,
                        font_color=args.font_color,
                        bg_color=args.bg_color,
                    )
            else:
                print(f"Warning: Quote file not found: {args.quote_file}")
        
        # Add outro if specified
        if args.outro:
            editor.add_outro_text(args.outro)
        
        # Save the edited video
        editor.save_video()
        
        # Cleanup
        editor.cleanup()
        
        print("\n✓ Video editing completed successfully!")
        print(f"✓ Output saved to: {args.output}")
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
