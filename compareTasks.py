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

# dataset = Datasets.Dataset()
# dataset.load_laminar_data(path="Data/")
# dataset.print_all_content()
# trials_block = dataset.get_trials(key='block', l=0, r=600)
# trials_trial = dataset.get_trials(key='trial', l=0, r=600)
# trials = [i for i in range(0, 600, 1)]


##############################################################################

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

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f8-f24-pfc.txt")

# tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['v4']
#                                 , save=True, bands=True
#                                 , time_window_size=500, time_overlap=0
#                                 , trials=trials, bw=50, tl=0, tr=4000,
#                                   time_base=-1500)

# Datasets.save_list([tpsd, freqs, times], "Data/1-600-tpsd-500ms-f8-f24-pfc.txt")
# [tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-500ms-f8-f24-pfc.txt")
