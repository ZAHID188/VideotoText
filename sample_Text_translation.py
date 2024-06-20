
'''
ja_text="あんまり他の国はどうですか?例えばどんなアニメ好きなんですが"
en_text = translator.translate(ja_text, dest="en").text
zh_text = translator.translate(ja_text, dest="zh-cn").text
print(en_text)
print(zh_text)'''


import speech_recognition as sr
import os
from googletrans import Translator



def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        audio_duration = len(audio.frame_data) / audio.sample_rate 
    try:
        text = recognizer.recognize_whisper(audio, language="ja")
        # Split the text into sentences
        sentences = text.split("。")
        finalJap=[]
        finalEN=[]
        FinalCH=[]
        translator = Translator()

        start_time = 0
        # Process each sentence
        for i, sentence in enumerate(sentences):
            # Calculate the end time (assuming equal time per sentence)
            end_time = start_time + len(sentence) / len(text) * audio_duration
            # Print the sentence with timestamps
            en_text = translator.translate(sentence, dest="en").text

            # print(f"[{start_time:.2f} - {end_time:.2f}]: {sentence.strip()}")
            finalEN.append(f"[{start_time:.2f} - {end_time:.2f}]: {en_text.strip()}")
            # Update the start time
            start_time = end_time
        return finalEN
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Could not request results; {e}"

current_directory = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(current_directory, "audio/ad1.wav")
text = audio_to_text(audio_path)
print(text)
