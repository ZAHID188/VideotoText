
from pydub import AudioSegment
import speech_recognition as sr

def extract_audio(video_path, audio_path):
    video = AudioSegment.from_file(video_path)
    video.export(audio_path, format="wav")
    print("AUDIO Extracted!")

# Get the current directory of the script




