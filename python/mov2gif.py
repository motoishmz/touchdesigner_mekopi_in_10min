#!/usr/bin/env python

'''
DEPENDENCIES:
pip install moviepy

$ python ./mov2gif.py input.mov output.gif 0.5
'''

import sys
import os
from moviepy.editor import *

if len(sys.argv) <= 2:
	print ('usage: ', sys.argv[0], '[INPUT_MOV_FILENAME]', '[OUTPUT_GIF_FILENAME]', '[SCALE]')
	sys.exit(-1)

assert(os.path.exists(sys.argv[1]))
INPUT_MOV_FILENAME = sys.argv[1]

OUTPUT_GIF_FILENAME = sys.argv[2]
SCALE = sys.argv[3]

clip = (VideoFileClip(INPUT_MOV_FILENAME)
        .resize(SCALE))
clip.write_gif(OUTPUT_GIF_FILENAME)
