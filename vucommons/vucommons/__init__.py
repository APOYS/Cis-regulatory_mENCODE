import os 

def loadtemplate():
	tp = """#!/bin/bash
#$ -cwd
#$ -pe smp CORENUM 
#$ -j y
#$ -S /bin/bash
#$ -V

cd WD

COMMAND"""
	return tp

def arguments(template,corenum,wd,command):
	""" takes the template, insert the arguments : number of cores, working dir, and COMMAND
	"""
	return template.replace("CORENUM",corenum).replace("WD",wd).replace("COMMAND",command)

def qsub(string):
	""" qsub the altered template """
	os.system("qsub " + string)
	return