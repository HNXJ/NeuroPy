import Datasets
import Methods
import Connect
import Viewer

import numpy as np


dataset = Datasets.Dataset()
dataset.load_laminar_data(filename="Data/data.mat")
dataset.print_all_content()
trials_block = dataset.get_trials(key='block', l=0, r=600)
trials_trial = dataset.get_trials(key='trial', l=0, r=600)
trials = [i for i in range(0, 600, 1)]

##############################################################################

# TSNE and PCA


# TODO


