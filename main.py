import plotly.graph_objects as go
import plotly.express as px
import scipy.io as sio
import numpy as np

from Methods import *
import plotly
import cv2


data = sio.loadmat('data.mat') # Example data, private access
print_all_content(data)

ERP_plot(save=True, data=data, key="pfc")
CSD_plot(save=True, data=data, key='pfc')

psp_plotter(data=data, key='pfc', save=True)
