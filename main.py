import os
from video_To_audio import extract_audio
from audioToText import audio_to_text

current_directory = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_directory, "video/vid1.mp4")
audio_path = os.path.join(current_directory, "audio/ad1.wav")

# extract_audio(video_path, audio_path)
text = audio_to_text(audio_path)
print(text)