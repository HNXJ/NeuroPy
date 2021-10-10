import scipy.io as sio
from Methods import *

### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# print_all_content(data)

### Event related potential and current source density plots
# ERP_plot(save=True, data=data, key="pfc")
# CSD_plot(save=True, data=data, key='pfc')

### Power spectrum (multitaper) plots on heatmap
# psp_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0, title="PS, all trials ")
# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0)

### Channelwise spectral coherence
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)
# coherence_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)

### Selective or single trial parts: PSP and COH
### PSP
# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0, trials=[100],
#             title="PS, trial 100")
# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0, trials=[400],
#             title="PS, trial 400")

### COH
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 100, 200", trials=[100, 200])
# coherence_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 400, 500", trials=[400, 500])

granger_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
            fmax=100, normalize_w=True, bw=45, k=0,
            title="Granger causality, trial 100, 200", trials=[100, 200], lag=12)
# granger_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 400, 500", trials=[400, 500], lag=2)