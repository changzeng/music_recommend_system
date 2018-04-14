import os
import sys
import wave  
import struct
import pickle
from scipy import *  

def convert_wav_to_frames():
	wav_path = "music/wav/"
	frames_path ="music/frames/"
	for _file in os.listdir(wav_path):
		#读取wav文件，我这儿读了个自己用python写的音阶的wav  
		filename = wav_path + _file
		frame_name = frames_path+_file.replace(".wav", ".frames")
		wavefile = wave.open(filename, 'r') # open for writing 

		# check if frames file exists
		if os.path.exists(frame_name):
			continue

		#读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到滴。  
		nchannels = wavefile.getnchannels()  
		sample_width = wavefile.getsampwidth()  
		framerate = wavefile.getframerate()  
		numframes = wavefile.getnframes()  
		  
		print("%s channel" % _file,nchannels)  
		print("%s sample_width" % _file,sample_width)  
		print("%s framerate" % _file,framerate)
		print("%s numframes" % _file,numframes)

		#建一个y的数列，用来保存后面读的每个frame的amplitude。  
		y = zeros(numframes)  

		#for循环，readframe(1)每次读一个frame，取其前两位，是左声道的信息。右声道就是后两位啦。  
		#unpack是struct里的一个函数，用法详见http://docs.python.org/library/struct.html。简单说来就是把＃packed的string转换成原来的数据，无论是什么样的数据都返回一个tuple。这里返回的是长度为一的一个  
		#tuple，所以我们取它的第零位。  
		for i in range(numframes):  
		    val = wavefile.readframes(1)  
		    left = val[0:2]
			#right = val[2:4]  
		    v = struct.unpack('h', left )[0]  
		    y[i] = v 

		    process_bar = "%s progress: (%8d)/(%8d) %4.2f%%" % (_file, i+1, numframes, (i+1.0)/numframes*100) + (" "*100 + "\r") if (i+1) != numframes else ""
		    sys.stdout.write(process_bar)
		    sys.stdout.flush()

		with open(frame_name, "wb") as fd:
			pickle.dump(y, fd, True)

if __name__ == "__main__":
	convert_wav_to_frames()