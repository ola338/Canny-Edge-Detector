# Canny edge detector
The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. 

## Steps
The process of Canny edge detector algorithm can be broken down to six different steps:

1. Apply Gaussian filter to smooth the image in order to remove the noise.
2. Find the gradient magnitude of the image.
3. Apply non maximum suppression to get rid of spurious response to edge detection.
4. Find the Otsu threshold of the image.
5. Apply double threshold to determine potential edges using the determined Otsu threshold.
6. Track edge by hysteresis - the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

## Results
Example image before and after canny edge detection.
![Example screenshot](./images/after_processing/canny_edge_detection.png)
## Used Technologies 
- Language: Python 3.9
- Libraries: skimage, scipy, numpy, matplotlib.pyplot
