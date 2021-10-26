import scipy.io as sio
import Methods
import Connect
import Viewer

# ### Load data and show content of it
# data = sio.loadmat('Data/data.mat') # Example data, private access
# cues = sio.loadmat('Data/cues.mat') # Example data's cue tye array
# cues = cues['c']
# Methods.print_all_content(data)

# ### Trial ID decomposition
# t_exp = Methods.get_trials(cues, mode='block', l=0, r=10)
# t_unx = Methods.get_trials(cues, mode='trial', l=0, r=60)

##############################################################################

trials = [i for i in range(40, 60)]
# trials = t_exp
# trials = t_unx

# ### Event related potential and current source density plots
# Methods.ERP_plot(save=True, data=data, key="pfc")
# Methods.CSD_plot(save=True, data=data, key='pfc')

# ### Power spectrum (multitaper) plots on heatmap
# Methods.psp_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=0,
#             fmax=100, normalize_w=True, pink_noise_filter=False, bw=45, k=0, title="PS, all trials ")

# ## Channelwise spectral coherence
# Connect.coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0)

# ### Selective or single trial parts: PSP and COH
# ### PSP
# Methods.psp_plotter(data=data, key='v4', save=True, t1=2500, t2=4500, fmin=0,
#             fmax=100, normalize_w=True, bw=45, k=0, trials=t_exp,
#             title="PS, block mode (expected)")

# ### Coherence (spectral)
# Connect.coherence_plotter(data=data, key='pfc', save=True, t1=500, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Coherence, trial 100, 200", trials=[i for i in range(0, 50)])

# ### Coherence (granger)
# Connect.s_granger_plotter(data=data, key='pfc', save=True, t1=100, t2=2500, fmin=4,
#             fmax=100, normalize_w=True, bw=45, k=0,
#             title="Granger causality (maxlag=6 min P-values) on block (exp) first 100 trials",
#             trials=[1], lag=6)


# ### Power spectral density array in bands
# psd, freqs = Methods.power_spectrum_density(data=data, key='pfc', save=True, t1=2000, t2=4500, fmin=0,
#             fmax=100, normalize_w=False, bw=45, k=0, trials=[i for i in range(2)])

# ### PSD ratio plotter
# Methods.psd_ratio_plotter(psd=psd[:, :, 1], freqs=freqs,
#                   title="T10SpectBandAvgPower")

### Comparisons
# Methods.psd_ratio_compare_plotter(psd1=psd[:, :, 1], psd2=psd[:, :, 0],
#                           freqs=freqs, title="PSDRatio_T20-T80")

# Methods.psd_ratio_compare_plotter(psd1=psd[:, :, 0], psd2=psd[:, :, 0],
#                           freqs=freqs, title="PSDRatio_T40-T60")


# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=data, key='v4', save=True
#                                 , time_window_size=200, time_overlap=50
#                                 , trials=trials, bw=50, tl=0, tr=4500, time_base=-1500)

# ### SC in time windows
# tsc = Connect.time_spectral_coherence(data=tpsd, key='key', save=True, trials=trials, ts=times)

# ### GC is time windows
# tgc = Connect.time_granger_causality(data=tpsd, key='key', save=True, trials=trials, ts=times)

# Viewer.run(data=tpsd, fqs=freqs, title="PSD in time, V4 area "
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(40, 60)])

# Viewer.run(data=tsc, fqs=freqs, title="Spectral coherence in time, V4 area "
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(40, 60)])

### Spectral coherence in time window
# tsc, chs, times = Connect.time_spectral_cohernece(data=data, key='pfc', save=True
#                                 , time_window_size=500, time_overlap=10
#                                 , trials=[i for i in range(40, 60)], bw=50, tl=0, tr=4500, time_base=-1500)
