import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import mne
import cv2


def correlation_pearson(x, y):

    c = np.corrcoef(x.reshape([-1]), y.reshape([-1]))
    return c[0, 1]


def rdm(x, p=0):
    
    c = np.zeros([x.shape[p], x.shape[p]])
    for i in range(x.shape[p]):
        
        for j in range(i, x.shape[p]):
            
            if p == 0:
                c[i, j] = 1 - correlation_pearson(x[i, ], x[j, ])
            elif p == 1:
                c[i, j] = 1 - correlation_pearson(x[:, i, ], x[:, j, ])
            elif p == 2:
                c[i, j] = 1 - correlation_pearson(x[:, :, i, ], x[:, :, j, ])
            elif p == 3:
                c[i, j] = 1 - correlation_pearson(x[:, :, :, i, ], x[:, :, :, j, ])
            c[j, i] = c[i, j]
            
    return c


def time_rdm(x, p=0):
    
    
            