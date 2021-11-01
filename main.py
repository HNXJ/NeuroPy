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

# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-250ms.txt")

# dim = 3
# y = (np.array(trials)//50)%2
# x = tpsd[7:9, 3:15, 2:6, trials].reshape([-1, len(trials)]).transpose()
# X = Learning.tsne_cluster(X=x, Y=y, components=dim, perplx=10,
#                                    learning_rate=200, visualize=True,
#                                    iterations=6000, tit="tSNE-it6000-px180-lr100",
#                                    save=True, name="plot")
    
# Viewer.scatter(data=X, y=y, dim=dim, frames=1, title="TSNE cluster in time",
#                xlabel="", ylabel="", fr=times, trials=trials, bands=False)

# trials = [i for i in range(600)]

# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=250, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)
# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-250ms.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-250ms.txt")
# tsc = Connect.time_spectral_correlation(data=tpsd, trials=trials, ts=times)
# Datasets.save_list([tsc], "Data/1-600-tsc-250ms.txt")
# trials = [i for i in range(100, 300, 1)]

### GC is time windows
tgc, times = Connect.time_granger_causality(data=dataset.signals['pfc'],
                                        time_window_size=250, time_overlap=0,
                                        trials=trials, bw=50, tl=0, tr=4000,
                                        time_base=-1500)

Methods.save_list([tgc, times], "Data/1-600-tgc-250ms.txt")

# tpsd[np.isnan(tpsd)] = 0
# for i in range(600):
#     tpsd[:, :, :, i] -= np.min(np.min(np.min(tpsd[:, :, :, i])))
#     tpsd[:, :, :, i] /= np.mean(np.mean(np.mean(tpsd[:, :, :, i])))
    
# y = (np.array(trials)//50)%2


# [tgc, times] = Datasets.load_list("Data/1-600-tgc.txt")
# Connect.time_tsne_cluster(data=tpsd[:, 3:16, 3:16, :], y=y, trials=trials, dim=3, perplx=120, learning_rate=70, 
#                       n_iter=5000, times=times, title="tSNE in time", name="TtSNE3D")

### Best tSNE/PCAs
# Connect.time_pca_cluster(data=tpsd, y=y, trials=trials, dim=3, times=times, title="TPCA3D", name="TPCA3D")
# Connect.time_tsne_cluster(data=tpsd[:, 3:15, 2:6, :], y=y, trials=trials, dim=3, perplx=70, learning_rate=10, 
#                       n_iter=5000, times=times, title="tSNE in time", name="TtSNE3D")


