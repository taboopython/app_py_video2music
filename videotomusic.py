import os
import sys
import moviepy.editor as mp

input_file = os.environ.get('INPUT_FILE')

if not input_file:
    print("Error: No input file specified.")
    sys.exit(1)

if not input_file.endswith(".mp4"):
    print("Error: The file must be a .mp4 file.")
    sys.exit(1)

output_file = input_file.rsplit(".", 1)[0] + ".mp3"

video = mp.VideoFileClip(input_file)
video.audio.write_audiofile(output_file)
