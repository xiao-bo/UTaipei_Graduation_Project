import cPickle
import Image
import _imaging
import numpy
import numpy as np
from theano.tensor import *
import os
#####
## this will pickle kaggle/gray/train 50000 to xiao.pkl 
#####


####test ####

bound=10000  ## number of data bound
input_low=sys.argv[1]
low=int(input_low)
pkl_name='/home/u10016043/data/RGB/300000/train'+str(low)+'.pkl'
#pkl_name='/home/u10016043/data/RGB/ing/train'+str(low)+'.pkl'

label_name='trainLabel'+str(low)+'.txt'
print label_name
train_pixel=numpy.empty((bound,3,1024),numpy.float64)

train_label=[] ## list have label


file_name=[]##file name

def pickle(tr_p,tr_l):     #let data into pkl
	lists=[tr_p,tr_l]
	output=open(pkl_name,'wb')
	cPickle.dump(lists,output)
	output.close()

def openpng(dirname):	
	im=Image.open(dirname)
	p=list(im.getdata())
	a=[]
	b=[float(i[0])/255 for i in p]
	c=[float(i[1])/255 for i in p]	
	d=[float(i[2])/255 for i in p]	
	a=list((b,c,d))
	return a

####read label.txt into label list
def readlabel(train_label):
	file_label=open(label_name,'r')
	print 'read label.....'
	for count in range(0,bound):
		i=file_label.readline().replace("\n","")
		train_label.append(i)
		print i
	file_label.close()
	return train_label



def buildpixel():###append pixel to train,vaild
	for i in range((low-1)*bound+1,low*(bound)+1):###build name[] has png name
		tmp='/home/u10016043/data/kaggle/source_data/train/'+str(i)+'.png'	
		file_name.append(tmp)
		print tmp	
	for count in range(0,bound):##50000 train
		p=openpng(file_name[count])
		train_pixel[count]=numpy.asarray(p,dtype=float)
		
		if (count%100)==0:
			print count
		
buildpixel()
train_label=readlabel(train_label)
#print len(test_name)
print 'pickle...'
print len(train_pixel)
print len(train_pixel[0])
print len(train_pixel[0][0])
#print train_pixel[0][0]
#print len(train_label)

#for x in range(0,1000):
#	print test_label[x]
pickle(train_pixel,train_label)


#print len(test_pixel)
#print len(pixel)
#print len(pixel[1])



