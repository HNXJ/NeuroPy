import Datasets
import Methods
import Connect
import Viewer

import numpy as np


# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]

##############################################################################

t = 51
s = dataset.signals['pfc']
k = s.shape[1]
c = np.zeros([k, k])
for i in range(s.shape[1]):
    for j in range(s.shape[1]):
        
        f, ch = Connect.coherence(s[:, i, t], s[:, j, t], fs=1000)
        r = np.sum(f < 100)
        l = np.sum(f < 7)
        c[i, j] = np.mean(ch[l:r])

# TODO


