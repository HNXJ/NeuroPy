import scipy.io as sio
from Methods import *
from Connect import *
from Viewer import *


# ### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# cues = sio.loadmat('cues.mat') # Example data's cue tye array
# cues = cues['c']
# print_all_content(data)

# ### Trial ID decomposition
t_exp = get_trials(cues, mode='block', l=0, r=10)
t_unx = get_trials(cues, mode='trial', l=0, r=10)

##############################################################################




# ### Event related potential and current source density plots
# ERP_plot(save=True, data=data, key="pfc")
# CSD_plot(save=True, data=data, key='pfc')

# ### Power spectrum (multitaper) plots on heatmap
# psp_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=0,
#             fmax=100, normalize_w=True, pink_noise_filter=False, bw=45, k=0, title="PS, all trials ")

### Channelwise spectral coherence
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)

### Selective or single trial parts: PSP and COH
### PSP
# psp_plotter(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0, trials=t_exp,
#             title="PS, block mode (expected)")

# ### Coherence (spectral)
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 100, 200", trials=[i for i in range(0, 50)])
# coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 100, 200", trials=[i for i in range(50, 100)])

# ### Coherence (granger)
# s_granger_plotter(data=data, key='pfc', save=True, t1=100, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Granger causality (maxlag=6 min P-values) on block (exp) first 100 trials",
#             trials=t_exp, lag=6)

# s_granger_plotter(data=data, key='pfc', save=True, t1=100, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Granger causality (maxlag=6 min P-values) on trial (unexp) first 100 trials",
#             trials=t_unx, lag=6)

# psd, freqs = power_spectrum_density(data=data, key='pfc', save=True, t1=2000, t2=4500, fmin=0,
#             fmax=100, normalize_w=False, bw=45, k=0, trials=[i for i in range(100)])

# psd_ratio_plotter(psd=psd[:, :, 10], freqs=freqs,
#                   title="T10SpectBandAvgPower")

# tpsd, freqs = time_power_spectrum_density(data=data, key='pfc', save=True
#                                 , time_window_size=500, time_overlap=10
#                                 , trials=t_exp, bw=50, tl=0, tr=4500)

# psd_ratio_plotter(psd=tpsd[6, :, :, 9], freqs=freqs,
#                   title="T10SpectBandAvgPower")

# psd_ratio_compare_plotter(psd1=psd[:, :, 20], psd2=psd[:, :, 80],
#                           freqs=freqs, title="PSDRatio_T20-T80")

# psd_ratio_compare_plotter(psd1=psd[:, :, 40], psd2=psd[:, :, 60],
#                           freqs=freqs, title="PSDRatio_T40-T60")
