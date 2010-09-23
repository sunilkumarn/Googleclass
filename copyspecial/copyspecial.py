import sys
import os
import re
import shutil
def copy(dir,target_dir):
	""" 
	Copies special files from a particular directory 
	into a target directory.
	"""
	files = os.listdir(dir)
	for name in files:
		check = re.findall(r'__(\w+)__',name)
		if check:
			shutil.copy(name,target_dir)

def main():
	args = sys.argv[1:]
	if args:
		dir = args[0]
		target_dir = args[1]
	else:
		print "Usage: python ['filename'] ['directory'] ['target directory']"
	copy(dir,target_dir)
main()

		


