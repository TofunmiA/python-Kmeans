from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from sklearn.metrics import pairwise_distances_argmin
import numpy as np
import time
import matplotlib.pyplot as plt


def kmeans_colors(img, k, max_iter=100):
    """
    Performs k-means clusering on the pixel values of an image.
    Used for color-quantization/compression.

    Args:
        img: The input color image of shape [h, w, 3]
        k: The number of color clusters to be computed

    Returns:
        img_cl:  The color quantized image of shape [h, w, 3]
    """

    img_cl = None
    
    img = np.array(img, dtype=np.float64) / 255
    
    # Load Image and transform to a 2D numpy array.
    w, h, d = original_shape = tuple(img.shape)
    assert d == 3
    img = np.reshape(img, (w * h, d)) 
    
    #KMeans
    image_array_sample = shuffle(img, random_state=0)[:1000]
    kmeans = KMeans(n_clusters = k, random_state=0, max_iter= 100).fit(image_array_sample)    
    
    #K-Means for cluster
    #get labels for all points
    labels = kmeans.predict(img)   
    clusters_ = kmeans.cluster_centers_ 
    
    d = clusters_.shape[1]
    img_cl = np.zeros((w, h, d))    
    label_idx = 0
    for i in range(w):
        for j in range(h):
            img_cl[i][j] = clusters_[labels[label_idx]]
            label_idx += 1
    #print(img_cl)
    return img_cl
    pass

    return img_cl
