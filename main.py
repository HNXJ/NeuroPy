import Datasets
import Methods
import Connect
import Viewer
import Learning

import numpy as np
import pandas as pd


# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]

##############################################################################


# trials = [i for i in range(600)]

# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=100, time_overlap=10
#                                 , trials=trials, bw=50, tl=0, tr=4000, time_base=-1500)
# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-100ms.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-100ms.txt")

dim = 3
trials = [i for i in range(30, 70, 1)]
x = tpsd[4:5, :, :, trials].reshape([-1, len(trials)]).transpose()
y = (np.array(trials)//50)%2
X = np.zeros([tpsd.shape[0], len(trials), dim])

for i in range(tpsd.shape[0]):    
    x = tpsd[i, :, :, trials].reshape([-1, len(trials)]).transpose()
    X[i, :, :] = Learning.pca_cluster(X=x, Y=y, components=dim, visualize=False, tit="PFC-PSD-PCA"
                , save=True, name="pcapfcpsd")

# X = Learning.tsne_cluster(X=x, Y=y, components=3, perplx=3, learning_rate=10, visualize=True
#                           , iterations=10000, tit="3D-PFC-PSD-tSNE"
#                           , save=True, name="3dpfctsne")

Viewer.scatter(data=X, y=y, dim=dim, frames=8, title="PCA cluster 2d in time", xlabel="", ylabel=""
        ,fr=None, tr=None, bands=False)





