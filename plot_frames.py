# encoding: utf-8

import pickle
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import *  

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='corpus generation.')
	parser.add_argument('--file_name', type=str, default=None, help="sepcify the frames file name you want to plot")
	parser.add_argument('--seg_time', type=float, default=2, help="time length of each segmentation")
	args = parser.parse_args()

	# 帧率
	framerate = 44100

	with open("music/frames/"+args.file_name, "rb") as fd:
		wave_data = pickle.load(fd)
	wave_data = wave_data * 1.0 / max(wave_data)

	framenum = len(wave_data)
	total_time = framenum * 1.0 / framerate
	time = np.arange(0, framenum)*(1.0 / framerate)

	seg_length = int(framerate * args.seg_time)
	x_aixis = np.arange(0, seg_length)*(1.0 / framerate)
	seg_wave_data = wave_data[0: seg_length]
	plt.plot(x_aixis, seg_wave_data)
	plt.xlim(0, args.seg_time)
	plt.ylim(-1.0, 1.0)

	# plt.plot(time,wave_data)
	# plt.xlabel("Time(s)")
	# plt.ylabel("Amplitude")
	# plt.title("Single channel wavedata")
	# plt.grid('on')
	plt.show()