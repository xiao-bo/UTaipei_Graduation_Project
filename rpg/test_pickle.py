import cPickle
import Image
import _imaging
import numpy
import numpy as np
from theano.tensor import *
import sys
#####
## this will pickle kaggle/test into to test*.pkl,there has 20 pkl
#####


####test ####

bound=10000  ## number of data bound

test_pixel=numpy.zeros((bound,3,1024),numpy.float64) ## list have pixel
input_low=sys.argv[1]
low=int(input_low)
#low=1## represent currently testX.pkl version 1=test1.pkl  2=test2.pkl...
pkl_name='/home/u10016043/data/RGB/300000/test'+str(low)+'.pkl'
#pkl_name='/home/u10016043/data/RGB/ing/test'+str(low)+'.pkl'

test_label=[]
file_name=[]

def pickle(te_p,te_l):     #let data into pkl
	lists=[te_p,te_l]
	output=open(pkl_name,'wb')
	cPickle.dump(lists,output)
	output.close()

def openpng(dirname):	
	im=Image.open(dirname)
	p=list(im.getdata())
	b=[float(i[0])/256 for i in p]
	c=[float(i[1])/256 for i in p]
	d=[float(i[2])/256 for i in p]
	a=list((b,c,d))
	#print p
	#for y in range(0,1024):
		#p[y]=[float(x)/256 for x in p[y]]

	#print p[0]
	return a

####append 0 into test_label list
def readlabel(test_label):	
	print 'read label.....'
	for count in range(0,bound):##
		test_label.append('0')
	return test_label


def testpixel():
	for i in range((low-1)*bound+1,low*(bound)+1):###build name[] has png name
		##low represent currently testX.pkl version   
		tmp='/home/u10016043/data/kaggle/source_data/test/'+str(i)+'.png'
		file_name.append(tmp)
		
	for count in range(0,bound):
		p=openpng(file_name[count])
		test_pixel[count]=numpy.asarray(p,dtype=float)
		if (count%100)==0:
			print count
			print low


#tmp='/home/u10016043/public_html/test2.png'
#p=openpng(tmp)
#print len(p)

testpixel()
test_label=readlabel(test_label)
#print len(test_name)
print 'pickle...'
print len(test_pixel)
print len(test_pixel[0])
print len(test_pixel[0][0])
#print test_pixel
#print test_pixel[0]
#print test_pixel[0][0]
#print len(test_label)
#for x in range(0,1000):
#	print test_label[x]
pickle(test_pixel,test_label)


#print len(test_pixel)
#print len(pixel)
#print len(pixel[1])



