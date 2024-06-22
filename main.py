import os
from video_To_audio import extract_audio
from audioToText import audio_to_text
from convert_to_text import Con_to_text
from Jap_store_DB_v1 import jp_insert_into_database,NewdatabaseCreate,jp_get_value
from jap_en_cn import translation

# if database not created
# NewdatabaseCreate()  


current_directory = os.path.dirname(os.path.abspath(__file__))      #current directory
video_path = os.path.join(current_directory, "video/")              #d:\Programming\VideotoText\video/
file_list = os.listdir(video_path)                                  #['vid1.mp4','vid2.mp4']

def video_to_text_into_DB():
    for file in file_list:
        file_path = os.path.join(video_path, file)                      #d:\Programming\VideotoText\video/vid1.mp4
        file_name_without_ext=file.split('.')[0]                        #vid1
        audio_path = os.path.join(current_directory, "audio", f"{file_name_without_ext}.wav")   #d:\Programming\VideotoText\audio\vid1.wav
        extract_audio(file_path, audio_path)                            #  video >> audio
        Audio_to_Jap_text = str(audio_to_text(audio_path))             #audio > japnese text
        translated_text=translation(Audio_to_Jap_text)                 #translation
        jp_insert_into_database(file_path,file,str(Audio_to_Jap_text),str(translated_text[0]),str(translated_text[1]))  #insert into db
        if os.path.exists(audio_path):
            os.remove(audio_path)
        else:
            print(f"The file {audio_path} does not exist.")



def fetching_and_writing_TXT():
    for file in file_list:
        value_of_video_file=jp_get_value(file)
        file_name_without_ext=file.split('.')[0]                        
        txt_file_path=os.path.join(current_directory, "TXTFILES", f"{file_name_without_ext}.txt") 
        Con_to_text(txt_file_path,str(value_of_video_file))

video_to_text_into_DB()
fetching_and_writing_TXT()




