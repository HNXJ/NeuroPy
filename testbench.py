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


### TODO: RSA/RDM test 2X3 -> 6 class 

trials = [i for i in range(0, 100, 1)]
[tpsd, freqs, times] = Datasets.load_list("Data/1-600-tpsd-1000ms.txt")
[tsc] = Datasets.load_list("Data/1-600-tsc-1000ms.txt")
[tgc, times] = Datasets.load_list("Data/1-600-tgc-250ms.txt")

rdm_ = Representational.time_rdm(x=tsc, p_dim=3, t_dim=0, trials=trials)

Representational.time_rdm_plot(rdm_, title="RDM", dlabel="Trials", times=times)

###############################################################################