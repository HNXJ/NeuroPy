import Datasets
import Methods
import Connect
import Viewer
import Learning

import numpy as np
import pandas as pd
import warnings


warnings.filterwarnings("ignore")

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]

##############################################################################


trials = [i for i in range(100, 200)]

# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=250, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)
# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-250ms.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd.txt")

# trials = [i for i in range(30, 70, 1)]

tpsd[np.isnan(tpsd)] = 0
for i in range(600):
    tpsd[:, :, :, i] -= np.min(np.min(np.min(tpsd[:, :, :, i])))
    tpsd[:, :, :, i] /= np.mean(np.mean(np.mean(tpsd[:, :, :, i])))
    
y = (np.array(trials)//50)%2


# Connect.time_pca_cluster(data=tpsd, y=y, trials=trials, dim=3, times=times, title="TPCA3D", name="TPCA3D")
Connect.time_tsne_cluster(data=tpsd[:, 3:15, 2:6, :], y=y, trials=trials, dim=3, perplx=70, learning_rate=100, 
                      n_iter=5000, times=times, title="tSNE in time", name="TtSNE3D")





