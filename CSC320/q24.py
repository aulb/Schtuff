"""
Need: 
  - Compute x,y gradient using the sobel operator [1,0,-1] and [1,0,-1]^T
  - Compute the magnitude of the gradient @ each pixel, in python dot product with self and sqrt
  - Quantize the gradient based on angle, different sections of the angles corresponds to different pixel
  - Look at the pixel in the direction of its gradient and if the neighbours got higher gradient magnitude then kill this guy
  - Repeat
"""
