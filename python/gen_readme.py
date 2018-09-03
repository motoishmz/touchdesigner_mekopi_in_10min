#!/usr/bin/env python

"""
"""

import sys, os
import re
from moviepy.editor import *

def generateGif(src, dst, scale):
	try:
		clip = (VideoFileClip(src)
					.resize(scale))
		clip.write_gif(dst)
		print('[gif file generated]', dst)
		pass
	except:
		raise ValueError('generateGif failed. does the file ' + src + ' exist?')
		pass
	return

def generateTweetURI(basename):
	# +-@.+?-[0-9]+$
	patterns = re.match(r'[0-9]+?-@(.+?)_([0-9]+)$', basename)
	username = str(patterns[1])
	tweet = str(patterns[2])
	return 'https://twitter.com/' + username + '/status/' + tweet

def generateArticle(title, tweet_uri, image_path):
	# text = '## [' + basename + '](' + tweet_uri + ')\n'
	text = '## ' + basename + ')\n'
	text += '![](' + image_path + ')' + '\n'
	text += '\n'
	text += 'cite: [' + tweet_uri + '](' + tweet_uri + ')\n'
	text += '\n'
	return text

readme = open('readme.md','w')
myfiles = [f for f in os.listdir('./') if re.match(r'[0-9]+-@.+', f)]
for basename in myfiles:
	tweet_uri = generateTweetURI(basename)
	gif_path = 'gif/' + basename + '.gif'
	if not os.path.exists(gif_path):
		src = basename + '/TDMovieOut0.0.mov' #!!!
		dst = gif_path
		scale = 0.5 #!!!
		generateGif(src, dst, scale)
		pass
	
	article = generateArticle(basename, tweet_uri, gif_path)
	readme.write(article)
	print('[Succeeded] an article is added to readme:', basename)
	pass
readme.close()