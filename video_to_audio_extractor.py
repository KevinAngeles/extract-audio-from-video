import os
import subprocess

def time_to_seconds(hours, minutes, seconds, milliseconds=0):
    """Convert hours, minutes, seconds, and milliseconds to total seconds."""
    return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

def extract_audio_ffmpeg(input_file, output_file, start_time=None, end_time=None):
    """
    Extract audio from video file using FFmpeg.
    
    Args:
        input_file (str): Path to input video file
        output_file (str): Path to save output MP3 file
        start_time (float, optional): Start time in seconds. If None, starts from beginning.
        end_time (float, optional): End time in seconds. If None, goes to end of file.
    """
    try:
        # Build the base FFmpeg command
        cmd = ['ffmpeg', '-y', '-i', input_file]
        
        # Add start time if specified
        if start_time is not None:
            cmd.extend(['-ss', str(start_time)])
        
        # Add duration if both start and end times are specified
        if start_time is not None and end_time is not None:
            duration = end_time - start_time
            cmd.extend(['-t', str(duration)])
        
        # Add output options
        cmd.extend([
            '-q:a', '0',  # Best quality
            '-map', 'a',   # Only audio
            output_file
        ])
        
        # Run FFmpeg
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully extracted audio to {output_file}")
            return True
        else:
            print(f"FFmpeg error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def get_time_input(prompt):
    """Helper function to get time input from user."""
    print(f"\n{prompt}:")
    hours = int(input("  Hours: ") or 0)
    minutes = int(input("  Minutes: ") or 0)
    seconds = int(input("  Seconds: ") or 0)
    milliseconds = int(input("  Milliseconds (0-999): ") or 0)
    return time_to_seconds(hours, minutes, seconds, milliseconds)

def main():
    print("Video to MP3 Extractor (Using FFmpeg)")
    print("-" * 32)
    
    # Get input file path
    input_file = input("Enter the path to the video file: ").strip('"')
    
    if not os.path.exists(input_file):
        print("Error: File not found!")
        exit(1)
    
    # Ask if user wants to extract full video or a portion
    print("\nExtraction options:")
    print("1. Extract full video")
    print("2. Extract specific portion")
    choice = input("Choose an option (1 or 2): ").strip()
    
    start_time = None
    end_time = None
    
    while choice.strip() not in ['1', '2']:
        choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == '2':
        # Get time range for partial extraction
        print("\nEnter the time range for extraction:")
        start_time = get_time_input("Start time")
        end_time = get_time_input("End time")
        
        if end_time <= start_time:
            print("Error: End time must be after start time!")
            exit(1)
    
    # Set output file name
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    default_name = f"{base_name}_extracted"
    new_name = input(f"\nEnter the name for the extracted MP3 file (without extension) or press enter to use the name {default_name}: ").strip('"')
    output_file = f"{new_name}.mp3" if new_name else f"{default_name}.mp3"
    
    # Extract audio
    if choice == '1':
        print("\nExtracting full audio...")
    else:
        print(f"\nExtracting audio from {start_time:.2f}s to {end_time:.2f}s...")
    
    extract_audio_ffmpeg(input_file, output_file, start_time, end_time)

if __name__ == "__main__":
    main()
