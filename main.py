import scipy.io as sio
from Methods import *
from Granger import *

### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# cues = sio.loadmat('cues.mat') # Example data's cue tye array
# cues = cues['c']
# print_all_content(data)

### Trial ID decomposition
t_exp = get_trials(cues, mode='block', l=0, r=100)
t_unx = get_trials(cues, mode='trial', l=0, r=100)


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
#             fmax=100, normalize_w=True, bw=45, k=0, trials=t_exp,
#             title="PS, block mode (expected)")

# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0, trials=t_unx,
            # title="PS, trial mode (unexpected)")

### Coherence (spectral)
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 100, 200", trials=[100, 200])

### Coherence (granger)
s_granger_plotter(data=data, key='pfc', save=True, t1=100, t2=2500, fmin=4,
            fmax=100, normalize_w=True, bw=45, k=0,
            title="Granger causality (maxlag=6 min P-values) on block (exp) first 100 trials",
            trials=t_exp, lag=6)

s_granger_plotter(data=data, key='pfc', save=True, t1=100, t2=2500, fmin=4,
            fmax=100, normalize_w=True, bw=45, k=0,
            title="Granger causality (maxlag=6 min P-values) on trial (unexp) first 100 trials",
            trials=t_unx, lag=6)

