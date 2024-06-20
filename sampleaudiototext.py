


import speech_recognition as sr
import os
import mysql.connector



def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        audio_duration = len(audio.frame_data) / audio.sample_rate 
    try:
        text = recognizer.recognize_whisper(audio, language="ja")
        # Split the text into sentences
        sentences = text.split("。")
        final=[]
        start_time = 0
        # Process each sentence
        for i, sentence in enumerate(sentences):
            # Calculate the end time (assuming equal time per sentence)
            end_time = start_time + len(sentence) / len(text) * audio_duration
            # Print the sentence with timestamps
            # print(f"[{start_time:.2f} - {end_time:.2f}]: {sentence.strip()}")
            final.append(f"[{start_time:.2f} - {end_time:.2f}]: {sentence.strip()}")
            # Update the start time
            start_time = end_time
        return final
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Could not request results; {e}"

current_directory = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(current_directory, "audio/ad1.wav")
text = audio_to_text(audio_path)
print(text)




'''
#gpt4-0 
import os
import whisper
import speech_recognition as sr

def audio_to_text_with_timestamps(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language="ja")
    
    sentences = []
    current_text = ""
    current_start = result['segments'][0]['start']
    
    for segment in result['segments']:
        current_text += segment['text']
        if any(punct in segment['text'] for punct in ['。', '.']):
            sentences.append((current_start, segment['end'], current_text.strip()))
            current_start = segment['end']
            current_text = ""
    
    if current_text:  # Add any leftover text
        sentences.append((current_start, result['segments'][-1]['end'], current_text.strip()))
    
    return sentences

# Example usage
current_directory = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(current_directory, "audio/ad1.wav")
text_with_timestamps = audio_to_text_with_timestamps(audio_path)

for start_time, end_time, text in text_with_timestamps:
    print(f"From {start_time:.2f} to {end_time:.2f}: {text}")'''