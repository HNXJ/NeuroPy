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

x = dataset.signals['pfc'][:, 1, 1]
y = dataset.signals['pfc'][:, 2, 1]
f, c = Connect.coherence(x, y, fs=1000)
Methods.customlineplot(f, c)
# TSNE and PCA


# TODO


