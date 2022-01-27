import Datasets
import Methods
import Connect
import Viewer

import Learning
import Representational

import numpy as np
import pandas as pd
import warnings


##############################################################################

warnings.filterwarnings("ignore")

##############################################################################
### Load and initialization

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]

##############################################################################
### Preprocessing

# ### PSD in time windows
# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f8-f24-pfc.txt")

# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['p7a']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f8-f24-p7a.txt")

# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['v4']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)

# Dataset s.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f8-f24-v4.txt")

##############################################################################
# PFC

# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-pfc.txt")
# trials = [i for i in range(130, 270)]

# dim = 3
# y = (np.array(trials)//50)%2
# yl = []
# y = np.reshape(dataset.cue_s[trials], [-1]) #+ 5 * ((np.array(trials)//50)%2)

# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("Trial(unpredictable)")
#     elif y[i] == 0:
#         yl.append("Block(predictable)")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("cor")
#     elif y[i] == 0:
#         yl.append("err")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("A")
#     elif y[i] == 2:
#         yl.append("B")
#     elif y[i] == 3:
#         yl.append("C")

# x = tpsd[:, 9:16, 2:7, trials].reshape([-1, len(trials)]).transpose()

# app = Connect.time_tsne_cluster(data=tpsd[:, 9:16, 3:7, :], y=y, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, pfc-deep-10-16",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app = Connect.time_tsne_cluster(data=tpsd[:, 2:10, 3:7, :], y=y, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, pfc-superficial-4-9",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app.run_server()

##############################################################################
# P7A

# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-p7a.txt")
# trials = [i for i in range(130, 270)]

# dim = 3
# y = (np.array(trials)//50)%2
# yl = []
# y = np.reshape(dataset.cue_s[trials], [-1]) #+ 5 * ((np.array(trials)//50)%2)
# y = np.reshape(dataset.cue_cr[trials], [-1])

# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("Trial(unpredictable)")
#     elif y[i] == 0:
#         yl.append("Block(predictable)")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("cor")
#     elif y[i] == 0:
#         yl.append("err")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("A")
#     elif y[i] == 2:
#         yl.append("B")
#     elif y[i] == 3:
#         yl.append("C")

# app1 = Connect.time_tsne_cluster(data=tpsd[:, 9:16, 3:, :], y=yl, trials=trials,
#                           dim=3, perplx=7, learning_rate=50, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, p7a-deep-10-16",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app2 = Connect.time_tsne_cluster(data=tpsd[:, 2:10, 3:, :], y=yl, trials=trials,
#                           dim=3, perplx=7, learning_rate=50, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, p7a-superficial-4-9",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app1.run_server()

##############################################################################
# V4

# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-v4.txt")
# trials = [i for i in range(130, 270)]

# dim = 3
# y = (np.array(trials)//50)%2
# yl = []
# y = np.reshape(dataset.cue_s[trials], [-1]) #+ 5 * ((np.array(trials)//50)%2)
# y = np.reshape(dataset.cue_cr[trials], [-1])

# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("Trial(unpredictable)")
#     elif y[i] == 0:
#         yl.append("Block(predictable)")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("cor")
#     elif y[i] == 0:
#         yl.append("err")
        
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("A")
#     elif y[i] == 2:
#         yl.append("B")
#     elif y[i] == 3:
#         yl.append("C")

# x = tpsd[:, 9:16, 2:7, trials].reshape([-1, len(trials)]).transpose()

# app1 = Connect.time_tsne_cluster(data=tpsd[:, 9:16, 5:, :], y=yl, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, v4-deep-10-16",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app2 = Connect.time_tsne_cluster(data=tpsd[:, 2:10, 5:, :], y=yl, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, v4-superficial-4-9",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app2.run_server()

##############################################################################
# All regions, separated


# [tpsd1, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-pfc.txt")
# [tpsd2, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-p7a.txt")
# [tpsd3, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-v4.txt")

# tpsd = np.zeros([7, 16, 12, 1800])
# tpsd[:, :, :, :600] = tpsd1
# tpsd[:, :, :, 600:1200] = tpsd2
# tpsd[:, :, :, 1200:1800] = tpsd3

# trials = [i for i in range(0, 1800, 5)]
# trialsf = [i for i in range(0, 600, 5)]

# dim = 3
# yl = []
# y0 = (np.array(trials)//50)%2
# y1 = np.reshape([dataset.cue_s[trialsf], dataset.cue_s[trialsf], dataset.cue_s[trialsf]], [-1])-1
# y2 = np.reshape([dataset.cue_cr[trialsf], dataset.cue_cr[trialsf], dataset.cue_cr[trialsf]], [-1])

# y = y0*6 + y1 + y2*3
# # y = y0

# # Block vs Trial
# # for i in range(len(trials)):
# #     if y[i] == 1:
# #         yl.append("Trial(unpredictable)")
# #     elif y[i] == 0:
# #         yl.append("Block(predictable)")
        
# # Correct vs Error
# # for i in range(len(trials)):
# #     if y[i] == 1:
# #         yl.append("cor")
# #     elif y[i] == 0:
# #         yl.append("err")
        
# # Type of cue
# # for i in range(len(trials)):
# #     if y[i] == 1:
# #         yl.append("A")
# #     elif y[i] == 2:
# #         yl.append("B")
# #     elif y[i] == 3:
# #         yl.append("C")

# yl_key = ['Block_A_err', 'Block_B_err', 'Block_C_err', 'Block_A_cor', 'Block_B_cor', 'Block_C_cor'
#           ,'Trial_A_err', 'Trial_B_err', 'Trial_C_err', 'Trial_A_cor', 'Trial_B_cor', 'Trial_C_cor']

# # Mixed category
# for i in range(len(trials)):
#     yl.append(yl_key[y[i]])
    
# # yl = y0    

# app1 = Connect.time_tsne_cluster(data=tpsd[:, 9:16, 6:, :], y=yl, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, all-regions-deep-10-16",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app2 = Connect.time_tsne_cluster(data=tpsd[:, 2:10, 2:9, :], y=yl, trials=trials,
#                           dim=3, perplx=20, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, all-regions-superficial-4-9",
#                             name="TtSNE3DGC", ee=15, method="exact")


# app1.run_server()
# app2.run_server()

# ###

# # import pickle


# # f = open('app1.pckl', 'wb')
# # pickle.dump(app1, f)
# # f.close()

##############################################################################
# All regions, concatenated


[tpsd1, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-pfc.txt")
[tpsd2, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-p7a.txt")
[tpsd3, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-v4.txt")

tpsd = np.zeros([7, 16, 36, 600])
tpsd[:, :, :12, :] = tpsd1
tpsd[:, :, 12:24, :] = tpsd2
tpsd[:, :, 24:36, :] = tpsd3

trials = [i for i in range(0, 600, 5)]
trialsf = [i for i in range(0, 600, 5)]

dim = 3
yl = []
y0 = np.reshape((np.array(trials)//50)%2, [-1])
y1 = np.reshape(dataset.cue_s[trialsf] - 1, [-1])
y2 = np.reshape(dataset.cue_cr[trialsf], [-1])

y = y0*6 + y1 + y2*3
# y = y0

# Block vs Trial
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("Trial(unpredictable)")
#     elif y[i] == 0:
#         yl.append("Block(predictable)")
        
# Correct vs Error
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("cor")
#     elif y[i] == 0:
#         yl.append("err")
        
# Type of cue
# for i in range(len(trials)):
#     if y[i] == 1:
#         yl.append("A")
#     elif y[i] == 2:
#         yl.append("B")
#     elif y[i] == 3:
#         yl.append("C")

yl_key = ['Block_A_err', 'Block_B_err', 'Block_C_err', 'Block_A_cor', 'Block_B_cor', 'Block_C_cor'
          ,'Trial_A_err', 'Trial_B_err', 'Trial_C_err', 'Trial_A_cor', 'Trial_B_cor', 'Trial_C_cor']

# Mixed category
for i in range(len(trials)):
    yl.append(yl_key[y[i]])
    
# yl = y0    

# app1 = Connect.time_tsne_cluster(data=tpsd[:, 9:16, :, :], y=yl, trials=trials,
#                           dim=3, perplx=10, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, all-regions-deep-10-16",
#                             name="TtSNE3DGC", ee=15, method="exact")

# app2 = Connect.time_tsne_cluster(data=tpsd[:, 2:10, :, :], y=yl, trials=trials,
#                           dim=3, perplx=10, learning_rate=25, 
#                           n_iter=6000, times=times, title="tSNE in time for PSD, all-regions-superficial-4-9",
#                             name="TtSNE3DGC", ee=15, method="exact")


app1.run_server()
# app2.run_server()

# ###

# # import pickle


# # f = open('app1.pckl', 'wb')
# # pickle.dump(app1, f)
# # f.close()
