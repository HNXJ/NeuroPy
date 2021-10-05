import scipy.io as sio
from Methods import *

### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# print_all_content(data)

### Event related potential and current source density plots
# ERP_plot(save=True, data=data, key="pfc")
# CSD_plot(save=True, data=data, key='pfc')

### Power spectrum (multitaper) plots on heatmap
psp_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=0,
            fmax=100, normalize_w=True, bw=45, k=0, title="PS, all trials ")
# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0)

### Channelwise spectral coherence
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)
# coherence_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)

### Single trial parts
psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
            fmax=100, normalize_w=True, bw=45, k=0, trials=[100],
            title="PS, trial 100")
psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
            fmax=100, normalize_w=True, bw=45, k=0, trials=[400],
            title="PS, trial 400")
