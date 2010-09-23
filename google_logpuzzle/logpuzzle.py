#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import shutil
"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):

  """Returns a list of puzzle urls from the given logfile
  extracting the host name from the file itself. Screens out 
  duplicate urls and returns the urls sorted in 
  increasing order."""
  paths,url_list=[],[]
  f=open(filename,'r')
  text=f.readlines()

  if filename=='animal_code.google.com':
    for long_urls in text:
      check=re.findall(r'/edu/languages/google-python-class/images/puzzle/a-\w+.jpg',long_urls)
      if check and check not in paths:paths.append(check)
    for url in paths:url_list.append('http://code.google.com'+url[0])
    sorted_urls= sorted(url_list)
    url_list=sorted_urls
    return url_list

  else:
    for long_urls in text:
      check=(re.findall(r'(/edu/languages/google-python-class/images/puzzle/p-\w+-)(\w+.jpg)',long_urls))
      if check and tuple(check[0]) not in paths:paths.append(tuple(check[0]))
    sorted_urls=sorted(paths,key=lambda x: x[-1])
    for url in sorted_urls:url_list.append('http://code.google.com'+url[0]+url[1])	
    return url_list
  

def download_images(img_urls, dest_dir):

  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  i=0
  os.mkdir(dest_dir)
  os.chdir(dest_dir)
  for url in img_urls:
    if urllib.urlretrieve(url,filename='img'+str(i)):print 'Retrieving image...'
    i+=1
  f=open('index.html','w')
  i=0
  while i<len(img_urls):
	  f.write('<img src="img'+str(i)+'"/>')
	  i+=1
  f.close()
      
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)

if __name__ == '__main__':
  main()
