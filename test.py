import Datasets
import Methods
import Connect
import Viewer

import numpy as np
import pandas as pd
import warnings


##############################################################################


warnings.filterwarnings("ignore")


##############################################################################


# ### Load dataset

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(filename="Data/data.mat")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]


##############################################################################

    
# ### Event related potential and current source density plots

# Methods.ERP_plot(data=dataset.signals['pfc'], title="ERP of pfc for all trials", save=True, filename="ERP_plot")
# Methods.CSD_plot(data=dataset.signals['v4'], title="Average CSD for all trials", save=True, filename="ACSD_plot")
  

##############################################################################


### Power spectral density array in bands

# trials = [40, 60]
# psd, freqs = Methods.power_spectrum_density(data=dataset.signals['pfc'], save=True, t1=1000, t2=4000, fmin=0,
#             fmax=100, normalize_w=True, bw=75, k=3, trials=trials)
# Methods.customplot(x=psd[:, :, 0].transpose(), save=True, show=True, filename="PSD_plot.html"
#                 , w=251, h=16, t=freqs, y=[i for i in range(16)], relative=True
#                 ,xlabel="T", ylabel="A", title="Plot", reverse=True
#                 ,xtext=False, xtext_labels=[])


##############################################################################


# ### PSD ratio plotter
# Methods.psd_ratio_plotter(psd=psd[:, :, 0], freqs=freqs,
#                   title="T40SpectBandAvgPower")
# Methods.psd_ratio_compare_plotter(psd1=psd[:, :, 1], psd2=psd[:, :, 0],
#                           freqs=freqs, title="PSDRatio_T60-T40")


# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=50
#                                 , trials=trials, bw=50, tl=0, tr=4000, time_base=-1500)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd.txt")


##############################################################################


# # Average PSD
# tpsd_m = np.zeros([tpsd.shape[0], tpsd.shape[1], tpsd.shape[2], 12]) 
# for i in range(12):
#     tpsd_m[:, :, :, i] = np.mean(tpsd[:, :, :, i*50:(i+1)*50], 3)

# ### SC in time windows
# tsc = Connect.time_spectral_correlation(data=tpsd, trials=[1, 2], ts=times)

### Spectral cohernece in time windows
# tsch, times, fr = Connect.time_spectral_coherence(data=dataset.signals['pfc'], time_window_size=500
#                                 , time_overlap=0, trials=[0, 1, 2], bw=50, tl=0
#                                 , tr=3500, time_base=-1500)
# ### Average TSC
# tsc_m = np.zeros([tsc.shape[0], tsc.shape[1], tsc.shape[2], 12]) 
# for i in range(12):
#     tsc_m[:, :, :, i] = np.mean(tsc[:, :, :, i*50:(i+1)*50], 3)


##############################################################################


# ### GC is time windows
# tgc, times = Connect.time_granger_causality(data=dataset.signals['pfc'], time_window_size=500
#                                 , time_overlap=0, trials=trials, bw=50, tl=0
#                                 , tr=3500, time_base=-1500)

# Methods.save_list([tgc, times], "Data/1-600-tgc.txt")
# [tgc, times] = Datasets.load_list("Data/1-600-tgc-250ms.txt")

# # ### Average TGC
# tgc_m = np.zeros([tgc.shape[0], tgc.shape[1], tgc.shape[2], 12]) 
# for i in range(12):
#     tgc_m[:, :, :, i] /= np.max(np.max(np.max(tgc[:, :, :, i])))


##############################################################################


# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms.txt")

# for i in range(tpsd.shape[0]):
#     for j in range(tpsd.shape[3]):
#         tpsd[i, :, :, j] /= np.max(np.max(tpsd[i, :, :, j])) + 0.0001
#         tpsd[i, :, :, j] = np.sqrt(tpsd[i, :, :, j])        

        
##############################################################################


# Viewer.heatmap(data=tpsd, fqs=freqs, title="PSD in time, pfc area ", bands=True
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)

# Viewer.heatmap(data=tsc, fqs=freqs, title="Spectral correlation in time, V4 area ", bands=False
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)

# Viewer.heatmap(data=tsch, fqs=fr, title="Spectral coherence in time, PFC area ", bands=False
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)

# Viewer.heatmap(data=tgc, fqs=freqs, title="Granger causality in time, pfc area "
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)

# Viewer.heatmap(data=tpsd_m, fqs=freqs, title="PSD in time, pfc area ", bands=True
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(12)])

# Viewer.heatmap(data=tsc_m, fqs=freqs, title="Spectral coherence in time, V4 area ", bands=False
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(12)])

# Viewer.heatmap(data=tgc_m, fqs=freqs, title="Granger causality in time, pfc area "
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[i for i in range(12)])


##############################################################################


# ### Clustering

# X = Learning.pca_cluster(X=x, Y=y, components=dim, visualize=True, tit="PFC-PSD-PCA"
#             , save=True, name="pcapfcpsd")

# X = Learning.tsne_cluster(X=x, Y=y, components=3, perplx=3, learning_rate=10, visualize=True
#                           , iterations=10000, tit="3D-PFC-PSD-tSNE"
#                           , save=True, name="3dpfctsne")


##############################################################################


# ### Demos
# run_1(11, 61, 5)
# run_2(3, 2, 5)
# run_ratio_tpsd(tps=tpsd_m, t1=5, t2=6)

# def run_1(trial1=1, trial2=151, f=4): # single trial psd ratios
#     ### PSD ratio plotter
#     Methods.psd_ratio_plotter(psd=tpsd[f, :, :, trial1], freqs=freqs,
#                       title="T" + str(trial1) + "SpectBandAvgPower")
    
#     ## Comparisons
#     Methods.psd_ratio_compare_plotter(psd1=tpsd[f, :, :, trial1], psd2=tpsd[f, :, :, trial2],
#                               freqs=freqs, title="PSDRatio_T" + str(trial1) + "-T" + str(trial2))

#     return

# def run_2(trial1=1, trial2=2, f=4): # single trial psd ratios
#     ### PSD ratio plotter 
#     Methods.psd_ratio_plotter(psd=tpsd_m[f, :, :, trial1], freqs=freqs,
#                       title="T" + str((trial1-1)*50) + "-" + str(trial1*50) + "SpectBandAvgPower")
    
#     ## Comparisons
#     Methods.psd_ratio_compare_plotter(psd1=tpsd[f, :, :, trial1], psd2=tpsd[f, :, :, trial2],
#                               freqs=freqs, title="PSDRatio_Tlower" + str(trial1*50) + "-Tlower" + str(trial2*50))

#     return


##############################################################################


# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms.txt")

# for i in range(tpsd.shape[0]):
#     for j in range(tpsd.shape[3]):
#         tpsd[i, :, :, j] /= np.max(np.mean(tpsd[i, :, :, j])) + 0.0001
#         tpsd[i, :, :, j] = np.sqrt(tpsd[i, :, :, j])

# trials = [i for i in range(200, 300)]
# dim = 3
# # y = (np.array(trials)//50)%2
# y = np.reshape(dataset.cue_cr[trials], [-1]) #+ 5 * ((np.array(trials)//50)%2)

# x = tpsd[:, 11:15, :, trials].reshape([-1, len(trials)]).transpose()

# Connect.time_tsne_cluster(data=tpsd[:, 9:16, 2:7, :], y=y, trials=trials, dim=3, perplx=5, learning_rate=25, 
#                       n_iter=5000, times=times, title="tSNE in time for granger causality values",
#                       name="TtSNE3DGC", ee=10, method="exact")

# X = Learning.tsne_cluster(X=x, Y=y, components=dim, perplx=5,
#                                     learning_rate=20, visualize=True,
#                                     iterations=5000, tit="tSNE-it6000-px180-lr100",
#                                     save=True, name="plot", ee=5, init='pca')#, method="exact")
    
# X = Learning.pca_cluster(X=x, Y=y, components=dim, visualize=True, tit="PFC-PSD-PCA"
#             , save=True, name="pcapfcpsd")

##############################################################################