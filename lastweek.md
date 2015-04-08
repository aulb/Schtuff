Flash no flash:
How to acquire pic:
	- Focus on the subject (object), LOCK the camera settings (focus etc white balance)
	- Capture ambient image A (no flash)
	- Enable flash, capture flash image with minimal exposure time
	- Don't move both time

Flash vs no flash picture:
	No flash:
		- Natural lighting (close to the real color)
		- Low signal to noise ratio
		- Loss of detail
		- Longer exposure - motion blur

	Flash:
		- Harsh unnatural lighting
		- High SNR (what exactly is SNR)
		- More details
		- May cause unwanted artifacts (red eye, shadows)

Bilateral filtering:
	What is bilateral filtering??
	Smoothing that preserves edges.

	How?
	- Average pixels that are spatially close (x,y not far from each other, talking about coordinates here) AND similar in intensities
	- Implement edge-preserving smoothing (cause you smooth you lose)
	A_p^{Base} = \frac{1}{k(p)} \sum_{p^' in \Omega} g_d (p^' - p) g_r (A_p - A_p^') A_p^'
	g_d = spatial kernel
	p' - p = spatial distance
	g_r = intensity kernel
	A_p - A_p' = intensity difference
	- Away from edges, it behaves like a regular Gaussian smoothing
	- Close to edges, the gaussian kernel gets truncated (how...)
	- Effect: this smoothing does not cross edges.. (how?)

Joint bilateral filtering:
	What is JOINT bilateral filtering??
	- Flash images contains much better edge information (more detailed)
	- Do smoothing in the ambient image (no flash), but use flash image to provide the edge-stopping
	A_p^{NR} = \frac{1}{k(p)} \sum_{p^' in \Omega} g_d (p^' - p) g_r (F_p - F_p^') A_p^'
	F_p - F_p' = intensity difference in flash, spatial use ambient

Detail transfer:
	- Flash image contains high frequency content that may not be in the no-flash photo
	- Transfer details from high freq image

	Detail layer:
		F^{detail} = \frac{F + \eps}{F^{Base} + \eps}, \eps = 0.02, whats F^{Base}? 
		Whats epsilon for?
		F^{Base} = bilateral-filtered FLASH image
		A^{Base} = bilateral-filtered AMBIENT image

		Denoised image with detail transfer:
		A^{Final} = A^{NR}F^{Detail}

Dark Flash Photography? Do we even

Image morphing summary:
	- Define corresponding points on both images
	- Define triangulation on points (use same triangulation for both images) Delauney triangulation for example
	- For each t in 0:step:1, [0.1, 0.2.., 0.9] or maybe [0.5] and done
		a) Compute the average shape (weighted average of points) --?? Middle guy!!
		b) For each triangle in the average shape
			Get the affine projection to the corresponding triangles in each image
			For each pixel in triangle, find the corresponding points in each image and set value to weighted average (or interpolate)
		c) Save image as the next frame in the sequence

Eulerian Video Magnification: Lots of giberish, can you please go in detail with me?
	- Intensity of that pixel over time

	Details:
		- Each pixel is processed independently
		- Each pixel as a time series and apply signal processing to it
		- Laplace pyramid, filter each level (bandpass filter) amplify bandpassed signal and reconstruct
	Reading:
		Reconstruction using laplacian pyramid

	What does it see?
	Subtle color variation: - face get slightly redder when blood flows
	Amplifies motion

Data driven beautification: Ask!!
	Details:
		- Learn to predict human's evaluation of beauty 
			a) Collect lots of faces
			b) Extract a set of feature points (maybe manually, not easy) (corresponding points ala morphing??)
			c) The features used in training are 234 distances
			d) Have humans rate beauty to construct training set (manual), as a whole or features
			e) Learn to predict human evaluation
		- Finding a nearby more beautiful face
			a) For input face (unknown), compute the features (extract feature points HOW?? compute distance b/w them)
			b) Find the k nearest neighbours with similar features, compute their weighted average giving more weight to more beautiful features
			c) Find configuration of feature points which produces the beautiful set of features
			d) MORPH/warp the face onto the new feature points

Inpainting, big data for photo completion:
	Details:
		- Find similar image from LARGE dataset
		- Blend a region from that image into the hole
	How detail do you wanna be? Ask, do we need to know how matching works properly? How the data is compared? 
	Using what way? Nearest neighbours? Compressed? SSD?		
