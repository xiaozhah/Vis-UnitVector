# -*- coding: utf-8 -*-
import numpy as np
import json
from collections import OrderedDict
import glob
import os

def ReadFloatRawMat(datafile,column):
	data = np.fromfile(datafile,dtype=np.float32)
	if len(data)%column!=0:
		print 'ReadFloatRawMat %s, column wrong!'%datafile
		exit()
	if len(data)==0:
		print 'empty file: %s'%datafile
		exit()
	data.shape = [len(data)/column,column]
	return np.float64(data)

data = ReadFloatRawMat('Unit2Vec_tSNE.dat',2)[:10000]
txt = np.loadtxt('phone_name_frame_id.csv',dtype=str,usecols=(1,3))[:10000]
phone = np.loadtxt('filelist.lst',dtype=str)[:10000]

lab = txt[:,0]
dur = map(lambda i:int(i),txt[:,1])

mydict = [{"No "+str(i):{"name":phone[i],
						 "pos":data[i].tolist(),
						 "dur":dur[i],
						 "lab":lab[i]}} for i in range(len(data))]
#print json.dumps(mydict, indent=1)
with open('Unit2Vec_tSNE.json', 'w') as outfile:
    json.dump(mydict, outfile, indent=1)