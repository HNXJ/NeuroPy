import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import mne
import cv2


def correlation_pearson(x, y):

    c = np.corrcoef(x.reshape([-1]), y.reshape([-1]))
    return c[0, 1]

def rdm(x):
    
    for i in range(x.shape[0]):
        
        for j in range(i, x.shape[0]):
            
            c[i, j] = 1 - correlation_pearson(x[i, ], x[j, ])
            c[j, i] = c[i, j]
            