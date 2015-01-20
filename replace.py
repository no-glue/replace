#!/usr/bin/env python

import os
import re
import argparse
import sys

def replace(fileName, toReplace, replaceWith):
  fh = file(fileName, 'r')
  content = fh.read()
  fh.close()
  pattern = re.compile(toReplace)
  content, num = pattern.subn(replaceWith, content)
  fh = file(fileName, 'w')
  fh.write(content)
  fh.close()

if __name__ == "__main__":
  argv = sys.argv[1:]
  parser = argparse.ArgumentParser()
  parser.add_argument("-fileName")
  parser.add_argument("-toReplace")
  parser.add_argument("-replaceWith")
  args = parser.parse_args(argv)
  replace(args.fileName, args.toReplace, args.replaceWith)
