import cPickle
import Image
import _imaging
import numpy
import numpy as np
from theano.tensor import *

#####
## this will pickle source_data/png to train1-4.pkl and valid.pkl 
#####

####test ####

bound=500  ## number of data bound

train1_pixel=numpy.empty((bound/5,3,1024),numpy.float64)
train2_pixel=numpy.empty((bound/5,3,1024),numpy.float64)
train3_pixel=numpy.empty((bound/5,3,1024),numpy.float64)
train4_pixel=numpy.empty((bound/5,3,1024),numpy.float64)
valid_pixel=numpy.empty((bound/5,3,1024),numpy.float64) ## list have pixel

tmp_label=[]
train1_label=[] ## train_label[0]
train2_label=[] ## train_label[1]
train3_label=[] ## train_label[2]
train4_label=[] ## train_label[3]
valid_label=[]

file_name=[]##file name


def pickle(pixel,label,pkl_name):     #let data into pkl
	lists=[pixel,label]
	output=open(pkl_name,'wb')
	cPickle.dump(lists,output)
	output.close()

def openpng(dirname):	
	im=Image.open(dirname)
	p=list(im.getdata())
	a=[]
	print len(p)
	"""
	b=[float(i[0])/256 for i in p]   
	c=[float(i[1])/256 for i in p]   
	d=[float(i[1])/256 for i in p]   
	a=list((b,c,d))"""
	#p[:]=[float(x)/256 for x in p]   ## norlized
	return a

####read label.txt into label list
def readlabel(train1_label,train2_label,train3_label,train4_label,vaild_label):
	file_label=open('dataLabel.txt','r')
	
	print 'read label.....'

	for count in range(0,bound):
		if count <(bound)/5:
			i=file_label.readline().replace("\n","")
			train1_label.append(i)
		elif (count>=(bound*1)/5)and(count<(bound*2)/5):
			i=file_label.readline().replace("\n","")
			train2_label.append(i)
		elif (count>=(bound*2)/5)and(count<(bound*3)/5):
			i=file_label.readline().replace("\n","")
			train3_label.append(i)
		elif (count>=(bound*3)/5)and(count<(bound*4)/5):
			i=file_label.readline().replace("\n","")
			train4_label.append(i)
		elif (count>=(bound*4)/5)and(count<bound):
			i=file_label.readline().replace("\n","")
			valid_label.append(i)
	file_label.close()
	#return train_label,valid_label



def buildpixel():###append pixel to train,vaild,test
	for i in range(1,bound+1):###build name[] has png name
		tmp='/home/u10016043/data/kaggle/source_data/train/'+str(i)+'.png'
		file_name.append(tmp)
	for count in range(0,bound):
		p=openpng(file_name[count])
		if count <(bound)/5:
			train1_pixel[count]=numpy.asarray(p,dtype=float)
		elif (count >=(bound)/5)and(count<(bound*2)/5):
			train2_pixel[count-(bound)/5]=numpy.asarray(p,dtype=float)
		elif (count >=(bound)*2/5)and(count<(bound*3)/5):
			train3_pixel[count-(bound)*2/5]=numpy.asarray(p,dtype=float)
		elif (count >=(bound)*3/5)and(count<(bound*4)/5):
			train4_pixel[count-(bound)*3/5]=numpy.asarray(p,dtype=float)
		elif (count >=(bound*4)/5)and(count<bound):
			valid_pixel[count-(bound*4)/5]=numpy.asarray(p,dtype=float)

		if (count%100)==0:
			print count
#buildpixel()
#readlabel(train1_label,train2_label,train3_label,train4_label,valid_label)
openpng('/home/u10016043/1.png')
print 'pickle...'
pkl1_name='/home/u10016043/data/RGB/300000/train1.pkl'
pkl2_name='/home/u10016043/data/RGB/300000/train2.pkl'
pkl3_name='/home/u10016043/data/RGB/300000/train3.pkl'
pkl4_name='/home/u10016043/data/RGB/300000/train4.pkl'
pkl5_name='/home/u10016043/data/RGB/300000/valid.pkl'
"""

pkl1_name='/home/u10016043/data/RGB/ing/train1.pkl'
pkl2_name='/home/u10016043/data/RGB/ing/train2.pkl'
pkl3_name='/home/u10016043/data/RGB/ing/train3.pkl'
pkl4_name='/home/u10016043/data/RGB/ing/train4.pkl'
pkl5_name='/home/u10016043/data/RGB/ing/valid.pkl'
pickle(train1_pixel,train1_label,pkl1_name)
pickle(train2_pixel,train2_label,pkl2_name)
pickle(train3_pixel,train3_label,pkl3_name)
pickle(train4_pixel,train4_label,pkl4_name)
pickle(valid_pixel,valid_label,pkl5_name)
"""
