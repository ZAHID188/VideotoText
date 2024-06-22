import os
# from video_To_audio import extract_audio
from audioToText import audio_to_text
from Jap_store_DB import jp_insert_into_database,NewdatabaseCreate
# from Jap_store_DB_v1 import jp_insert_into_database,NewdatabaseCreate

from jap_en_cn import translation

current_directory = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_directory, "video/vid1.mp4")
audio_path = os.path.join(current_directory, "audio/ad1.wav")

# extract_audio(video_path, audio_path)
Jap_text = str(audio_to_text(audio_path))
translated_text=translation(Jap_text)
print(Jap_text)
print(translated_text)


vid_title = os.path.basename(video_path)
# NewdatabaseCreate()
jp_insert_into_database(video_path,vid_title,str(Jap_text),str(translated_text[0]),str(translated_text[1]))
