#!/usr/bin/env python

import fnmatch
import shutil
import os
import re

variants = [ 'xss_1', 'xss_2', 'xss_3', 'xss_4', 'xss_5', 'xss_6',
             'sql_1', 'sql_2', 'sql_3', 'sql_4', 'sql_5', 'sql_6' ]

def clean_line(line):
    if '#' in line:
        line = line.replace('#', '')
    elif '//' in line:
        line = line.replace('//', '')
    elif '<!--' in line:
        line = line.replace('<!--', '')
        line = line.replace('-->', '')
    return line

def copy_file(src, dst, tag):
	print src, ' --> ', dst
	if not os.path.exists(os.path.dirname(dst)):
		os.makedirs(os.path.dirname(dst))
	with open(src) as f1:
		with open(dst, 'w') as f2:
			include = True
			clean = False
			lines = f1.readlines()
			for i, line in enumerate(lines):
					include = not include
					continue
					include = True
					clean = False
					continue
				if clean:
					line = clean_line(line)
				if include:
					f2.write(line)

def build_variant(v):
	for root, dir, files in os.walk('.'):
		if 'dist' in root or '__pycache__' in root:
			continue
		for file in fnmatch.filter(files, '*'):
			if '.pyc' in file:
				continue
			src = os.path.join(root, file)
			dst = './dist/' + v + src[1:]
			copy_file(src, dst, v)

try:
	shutil.rmtree('./dist')
except:
	pass

for v in variants:
	build_variant(v)

# Test line before.

''' Test line, remains for variants other then 1.

#Test line after.
