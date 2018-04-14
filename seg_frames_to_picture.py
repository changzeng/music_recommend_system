# encoding: utf-8

import os
import sys
import pickle
import argparse
import numpy as np
import matplotlib.pyplot as plt

def seg_frames(file_name, seg_time=1.0):
	if file_name == ".gitignore" or file_name == ".DS_Store":
		return
	save_path = "music/picture/" + file_name.replace(".frames", "") + "/"
	if not os.path.exists(save_path):
		os.mkdir(save_path)
	else:
		return

	with open("music/frames/"+file_name, "rb") as fd:
		wave_data = pickle.load(fd)

	# 帧率
	framerate = 44100
	wave_data = wave_data * 1.0 / max(wave_data)
	framenum = len(wave_data)
	total_time = framenum * 1.0 / framerate

	index = 1
	seg_length = int(framerate * seg_time)
	picture_num = int(framenum / seg_length)
	for frame_start in range(0, framenum, seg_length):
		plt.figure(0)
		frame_end = frame_start + seg_length
		if frame_end > framenum:
			break
		x_aixis = np.arange(frame_start, frame_end)*(1.0 / framerate)
		seg_wave_data = wave_data[frame_start: frame_end]
		plt.plot(x_aixis, seg_wave_data)
		plt.xlim(x_aixis[0], x_aixis[-1])
		plt.ylim(-1.0, 1.0)
		plt.savefig(save_path + "%d.jpg" % index)

		msg = "%s progress: (%8d)/(%8d) %4.2f%%" % (file_name, index, picture_num, (index*1.0)/picture_num*100) + (" "*100 + "\r") if (index) != picture_num else ""
		sys.stdout.write(msg)
		sys.stdout.flush()

		index += 1
		plt.close(0)

	print("Done!  %s" % file_name)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='corpus generation.')
	parser.add_argument('--seg_time', type=float, default=1, help="time length of each segmentation")
	args = parser.parse_args()

	files = os.listdir("music/frames")
	try:
		files.remove(".DS_Store")
	except:
		pass

	for file in files:
		seg_frames(file)
