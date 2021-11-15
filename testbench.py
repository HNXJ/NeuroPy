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

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
trials = [i for i in range(0, 600, 1)]

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
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-1000ms.txt")
[tsc] = Datasets.load_list("Data/1-600-tsc-1000ms.txt")
[tgc, times] = Datasets.load_list("Data/1-600-tgc-250ms.txt")

xt_array = tsc
xt = np.zeros([xt_array.shape[0], xt_array.shape[1], xt_array.shape[2], 6])
for i in range(len(sample_inds)):
    xt[:, :, :, i] = np.mean(tsc[:, :, :, sample_inds[i]], 3)

rdm_ = Representational.time_rdm(x=xt, p_dim=3, t_dim=0, trials=[i for i in range(6)])

ctl = ["A-Pred", "B-Pred", "C-Pred", "A-Unpred", "B-Unpred", "C-Unpred"]

Representational.time_rdm_plot(rdm_, title="RDM, average across temp-spect-coherence categories, Each time frame"
                               , dlabel="Modes", times=times, cat_labels=ctl)

###############################################################################