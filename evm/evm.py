import argparse

import evm.utils as utils


def magnify_color(vid, fps, low, high, levels=3, alpha=20):
	"""
	Function: magnify_color
	-----------------------
		Magnifies the color of a video

	Args:
	-----
		vid: the input video as a numpy array
		fps: the frame rate of the video
		low: the low frequency band to amplify
		high: the high frequency band to amplify
		levels: the depth at which to make the gaussian pyramid
		alpha: the factor with which to amplify the color

	Returns:
	--------
		The video with amplified color
	"""
	gauss = utils.gaussian_video(vid, levels=levels)
	filtered = utils.temporal_ideal_filter(gauss, low, high, fps)
	amplified = alpha * filtered
	return utils.reconstruct_video_g(amplified, vid, levels=levels)


def magnify_motion(vid, fps, low, high, levels=3, amplification=20):
	"""
	Function: magnify_motion
	-----------------------
		Magnifies the motion of a video

	Args:
	-----
		vid: the input video as a numpy array
		fps: the frame rate of the video
		low: the low frequency band to amplify
		high: the high frequency band to amplify
		levels: the depth at which to make the laplacian pyramid
		alpha: the factor with which to amplify the motion

	Returns:
	--------
		The video with amplified motion
	"""
	lap_video_list = utils.laplacian_video(vid, levels=levels)
	filtered_video_list = []
	for i in range(levels):
		filtered_video = utils.butter_bandpass_filter(
			lap_video_list[i], low, high, fps)
		filtered_video *= amplification
		filtered_video_list.append(filtered_video)
	recon = utils.reconstruct_video_l(filtered_video_list)
	final = vid + recon
	return final


types = {
	'color':magnify_color,
	'motion':magnify_motion
}


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', type=str)
	parser.add_argument('type', type=str)
	parser.add_argument('low', type=float)
	parser.add_argument('high', type=float)
	parser.add_argument('levels', type=int)
	parser.add_argument('alpha', type=float)
	parser.add_argument('--outputfile', type=str, default='out.avi')
	args = parser.parse_args()

	vid, fps = utils.load_video(args.filename)
	if args.type in types:
		res = types[args.type](
			vid,
			fps,
			args.low,
			args.high,
			args.levels,
			args.alpha)
		utils.save_video(res, args.outputfile)
	else:
		raise KeyError("{} is not a valid type.  Only one of these work: {}".format(args.type, types.keys()))
		# res = magnify_color(vid, fps, args.low, args.high, args.levels, args.alpha)

