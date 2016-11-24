
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os


# Write code to produce a mirror reflection of image I, followed by a rotation by 42 degrees around (1,1)
def q55():
	reflect = array([
		[0,1,0],
		[1,0,0],
		[0,0,1]
		])
	translate = array([
		[1,0,1],
		[0,1,1],
		[0,0,1]
		])
	theta = 0.733038286 # 42 degrees
	r = array([
		[cos(-theta), -sin(-theta),0],
        [sin(-theta), cos(-theta), 0],
        [0          ,           0, 1]
        ])
	return dot(dot(reflect, translate), r)


def rot_im(im, theta, h=None):
    # Setting up the homography: to rotate forward, need to translate to the
    # centre, then rotate, then translate back. To rotate *backward* (to get
    # the colour from the original image at the right coordinates, need to do
    # the opposite
    
    #Rotation matrix: rotate by -theta counterclockwise (i.e., by theta 
    #clockwise)
	if (h == None):
	    # r = array([
    	# 	[cos(-theta), -sin(-theta),0],
     #        [sin(-theta), cos(-theta), 0],
     #        [0          ,           0, 1]
     #        ])
	        
	    # #Translation matrix: translate (0,0) to the centre
	    # t1 = array([
    	# 	[1, 0, im.shape[0]/2.],
     #        [0, 1, im.shape[1]/2.],
     #        [0, 0, 1]
     #        ])

	    # #Translation matrix: translate the centre to 0,0
	    # t2 = array([
    	# 	[1, 0, -im.shape[0]/2.],
     #        [0, 1, -im.shape[1]/2.],
     #        [0, 0, 1]
            # ])  
		reflect = array([
			[0,1,0],
			[1,0,0],
			[0,0,1]
			])
		translate = array([
			[1,0,0],
			[0,1,0],
			[0,0,1]
			])
		theta = pi/8 # 42 degrees
		r = array([
			[cos(-theta), -sin(-theta),0],
		    [sin(-theta), cos(-theta), 0],
		    [0          ,           0, 1]
		    ])         
	    
	    # Sequence, translate center -> rotate -> translate origin
	    # Combine all the warps together using multiplication
		h = dot(dot(reflect, translate), r)#dot(dot(t1, r), t2) 
    
    #Construct the coordinates on the *target* image new_im
	x = arange(im.shape[0]) # Just like range but array([...])
	y = arange(im.shape[1])
	xy = meshgrid(x,y) 
	# 0,0 0,1 0,2
	# 1,0 1,1 1,2
	# ...

	# Make homogeneous coordinate system
	#xyf has all the same coordinates as xy, but they are all 
	#columns in a 3xIMSIZE matrix:
	# IMSIZE = height * width
	#[x0  x1 ...         x_IMSIZE
	# y0   y1...         y_IMSIZE
	# 1    1...          1]
	xyf = zeros((3, xy[0].flatten().shape[0]))

	xyf[0, :] = xy[0].flatten()
	xyf[1, :] = xy[1].flatten()
	xyf[2, :] = ones(xyf[0,1].shape)

	#Now ready to apply the homography to xyf
	#xyf_t is the coordinates in the *original* image im
	xyf_t = dot(h, xyf)
	xyf_t[0, :] = xyf_t[0, :]/xyf_t[2, :]
	xyf_t[1, :] = xyf_t[1, :]/xyf_t[2, :]
	xyf_t[2, :] = xyf_t[2, :]/xyf_t[2, :]

	#Round the coordinates. In effect, this is 
	#nearest-neighbour interpolation
	xyf_t = around(dot(h, xyf)).astype(int32)

	#Reshape the arrays back to be in the same format as
	#xy
	xy_t = [xyf_t[0,:].reshape(xy[0].shape), 
	        xyf_t[1,:].reshape(xy[1].shape)]

	#A trick to not bother with coordinates which are outside the original
	# image: copy everything onto a canvas that's all zeroes and larger
	#than im, so that "out of range" coordinates point to 0 intensities
	# ??? Whats going on here
	canvas = zeros(4*array(im.shape))
	canvas[2*im.shape[0]:3*im.shape[0], 2*im.shape[1]:3*im.shape[1]] = im

	#Now copy the intensities from the old image at xy_t onto the new image
	#at xy
	new_im = zeros(im.shape)
	new_im[xy[0], xy[1]] = canvas[2*im.shape[0]+xy_t[0], 2*im.shape[1]+xy_t[1]]
	return new_im

if __name__ == '__main__':
	im = imread("Panda-Face.jpg") / 255.

	theta = pi/3
	im_r = zeros(im.shape)
	#h = q55()

	# Do with each channel
	im_r[:,:,0] = rot_im(im[:,:,0], theta)
	im_r[:,:,1] = rot_im(im[:,:,1], theta)
	im_r[:,:,2] = rot_im(im[:,:,2], theta)


	close('all')
	imshow(im_r)
	show()
