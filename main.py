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


# TODO tSNE

### PSD in time windows
tpsd, freqs, times = Connect.time_power_spectrum_density(data=dataset.signals['pfc']
                                , save=True, bands=True
                                , time_window_size=500, time_overlap=50
                                , trials=trials, bw=50, tl=0, tr=4000, time_base=-1500)
