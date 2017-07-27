"""
In: a filename with a motif inside, conserve motif set

Out: filename link with either conserve or non-conserve mark in it 

"""

from sys import argv


tomtomfile = argv[1]
infile = argv[2]


cHuman = {}
cMouse = {}
for line in open (tomtomfile):
	if "Query" not in line:
		cHuman[line.strip().split()[0].split('.')[0]] = 1
		cMouse[line.strip().split()[1].split('.')[0]] = 1

seen = {}
retain = {}
others = {}
similar = {}
different = {}
#out = open("human.mouse.tagged.tomtom.best",'w')
for line in open(tomtomfile):
    if "Query" in line: 
        continue
    tmp = line.strip().split()
    if tmp[0] not in seen:
        #out.write(line)
        #print tmp[0]
        m1 = markonly(tmp[0])
        m2 = markonly(tmp[1])
        if m1 == m2:
            print tmp[0],tmp[1]
            retain[tmp[0]] = tmp[1]
            seen[tmp[0]] = 1
        else:
            marks1 = m1.split('_')
            marks2 = m2.split('_')
            issimilar = False
            for mark in marks1:
                if mark in marks2:
                    issimilar = True
            if issimilar:
                similar[tmp[0]] = tmp[1]
                seen[tmp[0]] = 1
            else:
                different[tmp[0]] = tmp[1]
                seen[tmp[0]] = 1


