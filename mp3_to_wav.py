# encoding: utf-8

import os
import sys
from pydub import AudioSegment

mp3_path = "music/mp3/"
wav_path = "music/wav/"

for _file in os.listdir(mp3_path):
	if _file == ".DS_Store":
		continue
	if os.path.exists(wav_path+wav_name):
		continue
	msg = "processing %s\r"+" "*100 % _file
	sys.stdout.write(msg)
	sys.stdout.flush()
	wav_name = _file.replace(".mp3", ".wav")
	sound = AudioSegment.from_mp3(mp3_path+_file)
	sound.export(wav_path+wav_name, format="wav")