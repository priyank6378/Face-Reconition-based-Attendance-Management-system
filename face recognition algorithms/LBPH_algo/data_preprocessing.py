import numpy as np
import cv2

def preprocess_data(data, noise_remove=True, scaling=True):
    # standard scaling
    if scaling:
        data = np.array(data)
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0)
        data = (data-mean)/std
        
    # removing noise:
    if noise_remove:
        new_data = []
        for i in data:
            tmp = cv2.GaussianBlur(i,(3,3),0)
#             tmp = cv2.bilateralFilter(tmp, 15,75,75)
            new_data.append(tmp)
    data = np.array(new_data)
    
    return data
