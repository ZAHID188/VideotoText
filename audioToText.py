#numpy-scipy,whisper,torch,,pip install -U openai-whisper

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
        sentences = text.split("。")
        final=[]
        start_time = 0
        for i, sentence in enumerate(sentences):
            # Calculate the end time (assuming equal time per sentence)
            end_time = start_time + len(sentence) / len(text) * audio_duration
            # Print the sentence with timestamps
            final.append(f"[{start_time:.2f} - {end_time:.2f}]: {sentence.strip()}")
            # Update the start time
            start_time = end_time
        return final
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# current_directory = os.path.dirname(os.path.abspath(__file__))
# audio_path = os.path.join(current_directory, "audio/ad1.wav")
# text = audio_to_text(audio_path)
# print(text)

'''db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="zahid",
    password="1234",
    database="VIDEO_TO_TEXT"
)


cursor = db.cursor()
cursor.execute("""
  CREATE TABLE IF NOT EXISTS EXTRACTED_JAP_TEXT(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key', 
    original_Jap TEXT);""")

sql = "INSERT INTO EXTRACTED_JAP_TEXT (original_Jap) VALUES (%s)"
cursor.execute(sql, text)
db.commit()
db.close()
print("Data inserted successfully!")'''

