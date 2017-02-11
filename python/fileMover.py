#This program moves files from one directory to the other in three different ways.

import shutil
import os

def move(pathFrom, pathTo):
 #os.rename(pathFrom, pathTo)
 #shutil.move(pathFrom, pathTo)
 os.system('move ' + pathFrom + ' ' + pathTo)

"""
f = open('c:\\z\\pb.txt')
for l in f:
 l = l.strip()
 os.rename('c:\\books\\' + l, 'c:\\pythonbooks\\' + l)
print('Done')
"""
move('c:\\books\\MasteringTextMiningWithR.html', 'c:\\rbooks\\')