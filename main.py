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
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd.txt")

dim = 3
title = "PCA-PSD" + str(dim)
trials = [i for i in range(30, 70, 1)]
y = (np.array(trials)//50)%2



Connect.time_pca_cluster(data=tpsd, y=y, trials=trials, dim=3, times=times, title="TPCA3D", name="TPCA3D")
# Connect.time_tsne_cluster(data=tpsd, y=y, trials=trials, dim=3, perplx=5, learning_rate=10, 
#                       n_iter=1000, trials=None, times=None, title="tSNE in time", name="TtSNE3D")





