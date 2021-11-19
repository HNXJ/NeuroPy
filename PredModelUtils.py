import Datasets
import Methods
import Connect
import Viewer

import Learning
import Representational
# from flask import Flask

import numpy as np
import pandas as pd
import warnings


##############################################################################

warnings.filterwarnings("ignore")

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]

##############################################################################

# sample_inds = []
# for i in range(6):
#     sample_inds.append([])

# for i in trials:
#     if dataset.cue_s[i] == 1 and dataset.cues[i] == 0: # pred & A
#         sample_inds[0].append(i)
#     if dataset.cue_s[i] == 2 and dataset.cues[i] == 0: # pred & B
#         sample_inds[1].append(i)
        
#     if dataset.cue_s[i] == 3 and dataset.cues[i] == 0: # pred & C
#         sample_inds[2].append(i)
#     if dataset.cue_s[i] == 1 and dataset.cues[i] == 1: # unpred & A
#         sample_inds[3].append(i)
        
#     if dataset.cue_s[i] == 2 and dataset.cues[i] == 1: # unpred & B
#         sample_inds[4].append(i)
#     if dataset.cue_s[i] == 3 and dataset.cues[i] == 1: # unpred & C
#         sample_inds[5].append(i)
     
         
### RSA/RDM test 2X3 -> 6 class 

trials = [i for i in range(0, 100, 1)]
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-p7a.txt")
# [tsc] = Datasets.load_list("Data/1-600-tsc-500ms.txt")
# # [tgc, times] = Datasets.load_list("Data/1-600-tgc-250ms.txt")

# # xt_array = tpsd

# # xt = np.zeros([xt_array.shape[0], xt_array.shape[1], xt_array.shape[2], 6])
# # for i in range(len(sample_inds)):
# #     xt[:, :, :, i] = np.mean(xt_array[:, :, :, sample_inds[i]], 3)

# # Datasets.save_list(xt, "xt.txt")
# xt = Datasets.load_list("xt.txt")

# rdm_ = Representational.time_rdm(x=xt, p_dim=3, t_dim=0, trials=[i for i in range(6)])

# ctl = ["A-Pred", "B-Pred", "C-Pred", "A-Unpred", "B-Unpred", "C-Unpred"]

# app = Representational.time_rdm_plot(rdm_, title="RDM, average across temp-spect-coherence categories, Each time frame"
#                                , dlabel="Modes", times=times, cat_labels=ctl)

# app.run_server()

###############################################################################

trials = [i for i in range(0, 100, 1)]

# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4500,
#                                   time_base=-1500, fmin=3, fmax=247)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f3-f247-pfc.txt")
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-pfc.txt")
y = (np.array(trials)//50)%2

tpsd[np.isnan(tpsd)] = 0
a = Datasets.compactor(x=tpsd, dim=1, inds=[[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15]])

# app = Viewer.heatmap(data=a, fqs=freqs, title="PSD in time, pfc area ", bands=True
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=trials)
app = Connect.time_tsne_cluster(data=a, y=y, trials=trials,
                          dim=3, perplx=20, learning_rate=25, 
                          n_iter=6000, times=times, title="tSNE in time for PSD, v4, 8Hz-24-Hz",
                            name="TtSNE3DGC", ee=15, method="exact")

app.run_server()

###############################################################################

