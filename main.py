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


# TODO tSNE

# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=50
#                                 , trials=trials, bw=50, tl=0, tr=4000, time_base=-1500)
# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd.txt")
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd.txt")

trials = [i for i in range(40, 60, 1)]
x = tpsd[4:6, :, :, ].reshape([-1, 20]).transpose()
y = (np.array(trials)//50)%2

X = Learning.tsne_cluster(X=x, Y=y[40:60], components=3, visualize=True
                          , iterations=10000, tit="3D-PFC-PSD-tSNE"
                          , save=True, name="3dpfctsne")

# Learning.pca_cluster(X=x, Y=y[40:60], components=2, visualize=True, tit="PFC-PSD-PCA"
#             , save=True, name="pcapfcpsd")



