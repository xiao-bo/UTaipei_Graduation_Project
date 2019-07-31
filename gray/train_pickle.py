import cPickle
import Image
import _imaging
import numpy
import numpy as np
from theano.tensor import *

#####
## this will pickle kaggle/gray/train 50000 to xiao.pkl 
#####


####test ####

bound=30  ## number of data bound

train_pixel=numpy.empty(((bound/2),3,1024),numpy.float64)
vaild_pixel=numpy.empty(((bound/2),3,1024),numpy.float64) ## list have pixel

train_label=[] ## list have label
vaild_label=[]


file_name=[]##file name

def pickle(tr_p,va_p,tr_l,va_l):     #let data into pkl
	lists=[[tr_p,tr_l],[va_p,va_l]]
	output=open('/home/u10016043/data/RGB/ing/train.pkl','wb')
	cPickle.dump(lists,output)
	output.close()

def openpng(dirname):	
	im=Image.open(dirname)
	p=list(im.getdata())
	a=[]
	b=[i[0]for i in p]
	c=[i[1]for i in p]	
	d=[i[2]for i in p]	
	a=list((b,c,d))
	return a

####read label.txt into label list
def readlabel(train_label,vaild_label):
	file_label=open('trainLabels.txt','r')
	print 'read label.....'
	for count in range(0,bound):
		i=file_label.readline().replace("\n","")
		if count <len(train_pixel):##<50000 train
			train_label.append(i)
		else:
			vaild_label.append(i)
	file_label.close()
	return train_label,vaild_label



def buildpixel():###append pixel to train,vaild
	for i in range(1,bound+1):###build name[] has png name
		tmp='/home/u10016043/data/kaggle/source_data/train/'+str(i)+'.png'	
		file_name.append(tmp)
		
	for count in range(0,bound):##50000 train
		p=openpng(file_name[count])
		#print p
		
		if count <len(train_pixel):
			train_pixel[count]=numpy.asarray(p,dtype=float)
			#print train_pixel
		else:	
			vaild_pixel[count-len(train_pixel)]=numpy.asarray(p,dtype=float)
		
		if (count%100)==0:
			print count
		
buildpixel()
#train_label,vaild_label=readlabel(train_label,vaild_label)
#print len(test_name)
print 'pickle...'
print len(train_pixel)
print len(train_pixel[0])
print len(train_pixel[0][0])
#print train_pixel[0][0]
#print len(train_label)
#print len(vaild_pixel)
#print len(vaild_label)
#for x in range(0,1000):
#	print test_label[x]
#pickle(train_pixel,vaild_pixel,train_label,vaild_label)


#print len(test_pixel)
#print len(pixel)
#print len(pixel[1])



