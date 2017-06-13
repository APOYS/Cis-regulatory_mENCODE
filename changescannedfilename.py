#!/usr/bin/env python
from sys import argv
import os

"""
INPUT: file, tag1. tag2
OUTPUT: a link of file that was changed into a different name 
"""

infile = argv[1]
tag1 = argv[2]
tag2 = argv[3]

motifname = open(infile).readline().strip().split()[3]
outfilename = tag1+'.'+ motifname +'.'+tag2

command = "ln -s %s %s" %(infile, outfilename)
print command
os.system(command) 
