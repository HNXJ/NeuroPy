import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import mne
import cv2


def rdm(x):
    
    for i in range(x.shape[0]):
        
        for j in range(i, x.shape[0]):
            
            