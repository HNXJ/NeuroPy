import scipy.io as sio
import Methods
import Connect
import Viewer
import numpy as np


# ### Load data and show content of it
# data = sio.loadmat('Data/data.mat') # Example data, private access
# cues = sio.loadmat('Data/cues.mat') # Example data's cue tye array
# cues = cues['c']
# Methods.print_all_content(data)

# ### Trial ID decomposition
# t_exp = Methods.get_trials(cues, mode='block', l=0, r=10)
# t_unx = Methods.get_trials(cues, mode='trial', l=0, r=60)

##############################################################################

# trials = [i for i in range(245, 255)]
# trials = t_exp
# trials = t_unx
trials = [i for i in range(0, 600)]

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

# ## Comparisons
# Methods.psd_ratio_compare_plotter(psd1=psd[:, :, 1], psd2=psd[:, :, 0],
#                           freqs=freqs, title="PSDRatio_T20-T80")

# Methods.psd_ratio_compare_plotter(psd1=psd[:, :, 0], psd2=psd[:, :, 1],
#                           freqs=freqs, title="PSDRatio_T40-T60")


## PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=data, key='pfc'
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=50
#                                 , trials=trials, bw=50, tl=0, tr=4000, time_base=-1500)

# Methods.save_list([tpsd, freqs, times], "Data/1-600-tpsd.txt")
[tpsd, freqs, times] = Methods.load_list("Data/1-600-tpsd.txt")

## Average PSD
# tpsd_m = np.zeros([tpsd.shape[0], tpsd.shape[1], tpsd.shape[2], 12]) 
# for i in range(12):
#     tpsd_m[:, :, :, i] = np.mean(tpsd[:, :, :, i*50:(i+1)*50], 3)

# ## SC in time windows
# tsc = Connect.time_spectral_coherence(data=tpsd, key='key', save=True, trials=trials, ts=times)

# ## Average PSD
# tsc_m = np.zeros([tsc.shape[0], tsc.shape[1], tsc.shape[2], 12]) 
# for i in range(12):
#     tsc_m[:, :, :, i] = np.mean(tsc[:, :, :, i*50:(i+1)*50], 3)

# ### GC is time windows
# tgc, times = Connect.time_granger_causality(data=data, key='pfc', time_window_size=500
#                                 , time_overlap=0, trials=trials, bw=50, tl=0
#                                 , tr=3500, time_base=-1500)

# Methods.save_list([tgc, times], "Data/1-600-tgc.txt")
[tgc, times] = Methods.load_list("Data/1-600-tgc.txt")

# ## Average TGC
# tgc_m = np.zeros([tgc.shape[0], tgc.shape[1], tgc.shape[2], 12]) 
# for i in range(12):
#     tgc_m[:, :, :, i] = np.mean(tgc[:, :, :, i*5:(i+1)*5], 3)


# Viewer.run(data=tpsd, fqs=freqs, title="PSD in time, pfc area ", bands=True
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)

# Viewer.run(data=tsc, fqs=freqs, title="Spectral coherence in time, V4 area ", bands=False
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)

# Viewer.run(data=tgc, fqs=freqs, title="Granger causality in time, pfc area "
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)



# Viewer.run(data=tpsd_m, fqs=freqs, title="PSD in time, pfc area ", bands=True
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(12)])

# Viewer.run(data=tsc_m, fqs=freqs, title="Spectral coherence in time, V4 area ", bands=False
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(12)])

# Viewer.run(data=tgc_m, fqs=freqs, title="Granger causality in time, pfc area "
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(12)])


def run_1(trial1=1, trial2=151, f=4): # single trial psd ratios
    ### PSD ratio plotter
    Methods.psd_ratio_plotter(psd=tpsd[f, :, :, trial1], freqs=freqs,
                      title="T" + str(trial1) + "SpectBandAvgPower")
    
    ## Comparisons
    Methods.psd_ratio_compare_plotter(psd1=tpsd[f, :, :, trial1], psd2=tpsd[f, :, :, trial2],
                              freqs=freqs, title="PSDRatio_T" + str(trial1) + "-T" + str(trial2))

    return

def run_2(trial1=1, trial2=2, f=4): # single trial psd ratios
    ### PSD ratio plotter
    Methods.psd_ratio_plotter(psd=tpsd_m[f, :, :, trial1], freqs=freqs,
                      title="T" + str((trial1-1)*50) + "-" + str(trial1*50) + "SpectBandAvgPower")
    
    ## Comparisons
    Methods.psd_ratio_compare_plotter(psd1=tpsd[f, :, :, trial1], psd2=tpsd[f, :, :, trial2],
                              freqs=freqs, title="PSDRatio_Tlower" + str(trial1*50) + "-Tlower" + str(trial2*50))

    return

def run_ratio_tpsd(tps=None, t1=1, t2=2):

    trp = []
    for i in range(tps.shape[0]):
        
        trp.append(tps[i, :, :, t1]/tps[i, :, :, t2])
    
    trp = np.array(trp).reshape([tps.shape[0], tps.shape[1], tps.shape[2], 1])

    # trpsd1 = trpsd(tps=tpsd_m, t1=1, t2=2)
    Viewer.run(data=trpsd1, fqs=freqs, title="Max SP in time, pfc area on {}-{} x50".format(t1, t2), bands=True
               , xlabel="Frequency", ylabel="Channel", fr=times, tr=[1])

    return

# run_1(11, 61, 5)
# run_2(3, 2, 5)
run_ratio_tpsd(tps=tpsd_m, t1=5, t2=6)
