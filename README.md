# VideotoText

requirements.txt is for necessary packages

python version `Python 3.12.0` and `pip 23.2.1`

Install ffmpeg and then add in system's PATH environment variable for audio 
check using `ffmpeg -version`
> ffmpeg version 2024-06-03-git-77ad449911-full_build-www.gyan.dev Copyright (c) 2000-2024 the FFmpeg developers
built with gcc 13.2.0 (Rev5, Built by MSYS2 project)'''


check `req.py` for installing neccesary packeges

`pip install -U openai-whisper` for audio to text -numpy,torch, etc diffrent packege included in this package

#db mysql 8.4.0 

# MAIN.py
will run whole system

video_to_text_into_DB() >>> will run the video files from the folder and store in the DB
fetching_and_writing_TXT() >>>> will fetch the information from database and make a txt file

# 1. Video_To_audio.py
In this file `video` will be extracted into `audio`

# 2. audioToText.py
In this file `audio` will be extracted into `japanese text` 
japanese text will be marked with timeframe

# 3. Jap_store_DB.py
 `japanese text` will be store into `DB`
 1. video loaction
 2. video title
 3. japnese text


# 4. jap_en_cn.py
argostranslate -200mb, 
install packeges-zh,ja,en
[translation](https://pypi.org/project/argostranslate/)
In this file `japanese text` will be translated into `English and Chinese` and store into `DB`


