import plotly.graph_objects as go
import plotly.express as px
import scipy.io as sio
import numpy as np

from Methods import *
import plotly
import cv2


# data = sio.loadmat('data.mat') # Example data, private access
# print_all_content(data)
# ch_names = [str(i) for i in range(1, 17)]
# info = mne.create_info(ch_names=ch_names, sfreq=1000)
# d = np.transpose(data['lfp'][:, 0:16, 0])

# raw = mne.io.RawArray(d, info, first_samp=0, copy='auto', verbose=None)
# f = mne.time_frequency.psd_multitaper(raw, fmin=4, fmax=36, tmin=None, tmax=None,
#                                   bandwidth=2, adaptive=False, low_bias=True,
#                                   normalization='length', picks=ch_names, proj=False,
#                                   n_jobs=1, verbose=None)

# customplot(f[0].transpose(), save=True, show=True, filename="plot.html"
#                , w=300, h=200, t=np.linspace(4, 36, 300)
#                , y=np.linspace(1, 16, 200), relative=True
#                , xlabel="Freq", ylabel="Ch", title="Plot"
#                , reverse=True)

### Event related potential and current source density plots
# ERP_plot(save=True, data=data, key="pfc")
# CSD_plot(save=True, data=data, key='pfc')

### Power spectrum (multitaper) plots on heatmap
# psp_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=0,
#             fmax=100, normalize_w=False, bw=45, k=0)
# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=False, bw=45, k=0)

### Channelwise spectral coherence
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)
# coherence_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)


