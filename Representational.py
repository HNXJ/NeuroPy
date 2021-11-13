import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import mne
import cv2


def correlation_pearson(x, y):

    c = np.corrcoef(x.reshape([-1]), y.reshape([-1]))
    return c[0, 1]


def rdm(x, p_dim=0):
    
    c = np.zeros([x.shape[p_dim], x.shape[p_dim]])
    for i in range(x.shape[p_dim]):
        
        for j in range(i, x.shape[p_dim]):
            
            if p_dim == 0:
                c[i, j] = 1 - correlation_pearson(x[i, ], x[j, ])
            elif p_dim == 1:
                c[i, j] = 1 - correlation_pearson(x[:, i, ], x[:, j, ])
            elif p_dim == 2:
                c[i, j] = 1 - correlation_pearson(x[:, :, i, ], x[:, :, j, ])
            elif p_dim == 3:
                c[i, j] = 1 - correlation_pearson(x[:, :, :, i, ], x[:, :, :, j, ])
            c[j, i] = c[i, j]
            
    return c


def time_rdm(x, p_dim=3, t_dim=0, title="RDM", dlabel="A", times=None, trials=None):
    
    rdm_ = np.zeros([x.shape[t_dim], x.shape[p], x.shape[p]])
    for i in range(x.shape[t_dim]):
        rdm_ = Representational.rdm(x[i:i+1, :, :, trials], p_dim=p_dim)
        
    Viewer.heatmap(data=rdm_, fqs=None, title=title, bands=False
                , xlabel=dlabel, ylabel=dlabel, fr=times, tr=trials)
    
    return
