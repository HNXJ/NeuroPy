import Datasets
import Methods
import Connect
import Viewer
import Learning

import numpy as np
import pandas as pd
import warnings


##############################################################################


warnings.filterwarnings("ignore")


##############################################################################


# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]


##############################################################################


[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms.txt")

for i in range(tpsd.shape[0]):
    for j in range(tpsd.shape[3]):
        tpsd[i, :, :, j] /= np.max(np.max(tpsd[i, :, :, j])) + 0.0001
        tpsd[i, :, :, j] = np.sqrt(tpsd[i, :, :, j])

trials = [i for i in range(120, 380)]
dim = 3
y = (np.array(trials)//50)%2
yl = []

for i in range(len(trials)):
    if y[i] == 1:
        yl.append("Trial(unpredictable)")
    elif y[i] == 0:
        yl.append("Block(predictable)")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("cor")
#     elif y[i] == 0:
#         yl.append("err")
        
y = np.reshape(dataset.cue_cr[trials], [-1])*3 #+ 5 * ((np.array(trials)//50)%2)

x = tpsd[:, 9:16, 2:7, trials].reshape([-1, len(trials)*tpsd.shape[0]]).transpose()

# Connect.time_tsne_cluster(data=tpsd[:, 10:16, 3:7, :], y=yl, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD",
#                           name="TtSNE3DGC", ee=15, method="exact")

# X = Learning.tsne_cluster(X=x, Y=y, components=dim, perplx=5,
#                                     learning_rate=25, visualize=True,
#                                     iterations=5000, tit="tSNE-it6000-px180-lr100",
#                                     save=True, name="plot", ee=10, init='pca')#, method="exact")
    
# X = Learning.pca_cluster(X=x, Y=y, components=dim, visualize=True, tit="PFC-PSD-PCA"
#             , save=True, name="pcapfcpsd")

##############################################################################


# Viewer.scatter(data=X, y=y, dim=dim, frames=1, title="TSNE cluster in time",
#                xlabel="", ylabel="", fr=times, trials=trials, bands=False)

trials = [i for i in range(600)]

# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-1000ms.txt")
# tsc = Connect.time_spectral_correlation(data=tpsd, trials=trials, ts=times)
# Datasets.save_list([tsc], "Data/1-600-tsc-500ms.txt")
# trials = [i for i in range(100, 300, 1)]

# tgc, times = Connect.time_granger_causality(data=dataset.signals['pfc'],
#                                         time_window_size=250, time_overlap=0,
#                                         trials=trials, bw=50, tl=0, tr=4000,
#                                         time_base=-1500)

# Datasets.save_list([tgc, times], "Data/1-600-tgc-250ms.txt")


##############################################################################


# trials = [i for i in range(40, 60, 1)]
# y = (np.array(trials)//50)%2

# [tgc, times] = Datasets.load_list("Data/1-600-tgc-250ms.txt")

# Connect.time_tsne_cluster(data=tgc[:, 3:16, 3:16, :], y=y, trials=trials, dim=3, perplx=120, learning_rate=250, 
#                       n_iter=5000, times=times, title="tSNE in time for granger causality values",
#                       name="TtSNE3DGC", ee=20, method="exact")


##############################################################################


### Best tSNE/PCAs
# Connect.time_pca_cluster(data=tpsd, y=y, trials=trials, dim=3, times=times, title="TPCA3D", name="TPCA3D")
# Connect.time_tsne_cluster(data=tpsd[:, 3:15, 2:6, :], y=y, trials=trials, dim=3, perplx=70, learning_rate=10, 
#                       n_iter=5000, times=times, title="tSNE in time", name="TtSNE3D")


############################################################################################################################################################


[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-250ms.txt")

for i in range(tpsd.shape[0]):
    for j in range(tpsd.shape[3]):
        tpsd[i, :, :, j] /= np.max(np.max(tpsd[i, :, :, j])) + 0.0001
        tpsd[i, :, :, j] = np.sqrt(tpsd[i, :, :, j])

trials = [i for i in range(37, 39)]
dim = 3
y = (np.array(trials)//50)%2
yl = []

for i in range(len(trials)):
    if y[i] == 1:
        yl.append("Trial(unpredictable)")
    elif y[i] == 0:
        yl.append("Block(predictable)")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("cor")
#     elif y[i] == 0:
#         yl.append("err")
        
# y = np.reshape(dataset.cue_cr[trials], [-1])*3 #+ 5 * ((np.array(trials)//50)%2)

# y = []
# for i in range(len(trials)):
#     for j in range(tpsd.shape[0]):
#         y.append(dataset.cue_cr[trials[i]]*3)

tpsd[np.isnan(tpsd)] = 0
y = []
for i in range(len(trials)):
    for j in range(tpsd.shape[0]):
        y.append((i*tpsd.shape[0] + j)%15)


y = np.array(y).reshape(([-1]))
x = tpsd[:, 9:16, 2:7, trials].reshape([-1, len(trials)*tpsd.shape[0]]).transpose()

# Connect.time_tsne_cluster(data=tpsd[:, 10:16, 3:7, :], y=yl, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD",
#                           name="TtSNE3DGC", ee=15, method="exact")

X = Learning.tsne_cluster(X=x, Y=y, components=dim, perplx=5,
                                    learning_rate=25, visualize=True,
                                    iterations=1000, tit="tSNE-it6000-px180-lr100",
                                    save=True, name="plot", ee=10, init='pca')#, method="exact")
    
X = Learning.pca_cluster(X=x, Y=y, components=dim, visualize=True, tit="PFC-PSD-PCA"
            , save=True, name="pcapfcpsd")

##############################################################################