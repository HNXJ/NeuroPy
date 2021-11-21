import Datasets
import Methods
import Connect
import Viewer

import Learning
import Representational
from flask import Flask

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
trials = [i for i in range(0, 600, 1)]

##############################################################################

### Gradient layer detection

# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-pfc.txt")
# tpsd1 = tpsd[:, :15, :, :]
# tpsd2 = tpsd[:, 1:, :, :]

# gradient_tpsd = tpsd
# mean_grad_tpsd = np.mean(gradient_tpsd, 3).reshape([8, 16, 12, 1])
# mean_grad_tpsd[np.isnan(mean_grad_tpsd)] = 0
# # mean_grad_tpsd = np.mean(mean_grad_tpsd, 2).reshape([8, 15, 1, 1])
# # mean_grad_tpsd[np.isnan(mean_grad_tpsd)] = 0
# mean_grad_tpsd = Datasets.scale(mean_grad_tpsd, 0, 1)

# app = Viewer.heatmap(data=mean_grad_tpsd, fqs=freqs, title="PSD in time, pfc area ", bands=True
#             , xlabel="Frequency", ylabel="Channel", fr=times, tr=[0])

# app.run_server()

##############################################################################

sample_inds = []
for i in range(6):
    sample_inds.append([])

for i in trials:
    if dataset.cue_s[i] == 1 and dataset.cues[i] == 0: # pred & A
        sample_inds[0].append(i)
    if dataset.cue_s[i] == 2 and dataset.cues[i] == 0: # pred & B
        sample_inds[1].append(i)
        
    if dataset.cue_s[i] == 3 and dataset.cues[i] == 0: # pred & C
        sample_inds[2].append(i)
    if dataset.cue_s[i] == 1 and dataset.cues[i] == 1: # unpred & A
        sample_inds[3].append(i)
        
    if dataset.cue_s[i] == 2 and dataset.cues[i] == 1: # unpred & B
        sample_inds[4].append(i)
    if dataset.cue_s[i] == 3 and dataset.cues[i] == 1: # unpred & C
        sample_inds[5].append(i)
     
         
### RSA/RDM test 2X3 -> 6 class 

# trials = [i for i in range(0, 100, 1)]
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-pfc.txt")
# tpsd[np.isnan(tpsd)] = 0
# xt_array = tpsd

# k = 12
# xt = np.zeros([xt_array.shape[0], xt_array.shape[1], xt_array.shape[2], 6*k])
# for i in range(len(sample_inds)):
#     xt[:, :, :, i*k:(i+1)*k] = xt_array[:, :, :, sample_inds[i][:k]]

# # Datasets.save_list(xt, "xt.txt")
# xt = Datasets.load_list("xt.txt")
# xt = Datasets.compactor(xt, dim=1, inds=[[1, 2, 3], [4, 5, 6], [7, 8], [9, 10, 11, 12], [13, 14, 15]])

# rdm_ = Representational.time_rdm(x=xt[:, :, :, :], p_dim=3, t_dim=0, trials=[i for i in range(6*k)])

# ctl_l = ["A-Pred", "B-Pred", "C-Pred", "A-Unpred", "B-Unpred", "C-Unpred"]
# ctl = []
# for i in range(len(ctl_l)):
#     for j in range(k):
#         ctl.append(ctl_l[i] + str(j))
        
# app = Representational.time_rdm_plot(rdm_, title="RDM, average across temp-spect-coherence categories, Each time frame"
#                                 , dlabel="Modes", times=times, cat_labels=ctl)

# app.run_server()


# server = Flask(__name__)
# @server.route("/dash")
# def app_():
    # return app.index()

###############################################################################

trials = [i for i in range(0, 600)]

### PSD in time windows till tSNE
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4500,
#                                   time_base=-1500, fmin=3, fmax=247)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f3-f247-pfc.txt")
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-pfc.txt")

# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['p7a']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4500,
#                                   time_base=-1500, fmin=3, fmax=247)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f3-f247-p7a.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-p7a.txt")

# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['v4']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4500,
#                                   time_base=-1500, fmin=3, fmax=247)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f3-f247-v4.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f3-f247-v4.txt")

# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-v4.txt")

# for i in range(tpsd.shape[0]):
#     for j in range(tpsd.shape[3]):
#         tpsd[i, :, :, j] /= np.max(np.max(tpsd[i, :, :, j])) + 0.0001
#         tpsd[i, :, :, j] = np.sqrt(tpsd[i, :, :, j])

trials = [i for i in range(130, 270)]

dim = 3
# y = (np.array(trials)//50)%2
yl = []
y = np.reshape(dataset.cue_s[trials], [-1]) #+ 5 * ((np.array(trials)//50)%2)

for i in range(len(trials)):
    if y[i] == 1:
        yl.append("Trial(unpredictable)")
    elif y[i] == 0:
        yl.append("Block(predictable)")
        
for i in range(len(trials)):
    if y[i] == 1:
        yl.append("cor")
    elif y[i] == 0:
        yl.append("err")
        
for i in range(len(trials)):
    if y[i] == 1:
        yl.append("A")
    elif y[i] == 2:
        yl.append("B")
    elif y[i] == 3:
        yl.append("C")

x = tpsd[:, 9:16, 2:7, trials].reshape([-1, len(trials)]).transpose()

app = Connect.time_tsne_cluster(data=tpsd[:, :, 9:12, :], y=y, trials=trials,
                          dim=3, perplx=20, learning_rate=25, 
                          n_iter=6000, times=times, title="tSNE in time for PSD, v4, 8Hz-240-Hz",
                            name="TtSNE3DGC", ee=15, method="exact")

app.run_server()
