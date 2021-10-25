from plotly.offline import download_plotlyjs, init_notebook_mode, plot
from matplotlib import pyplot as plt 

import scipy.io as sio
from Methods import *
from Connect import *

# ### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# cues = sio.loadmat('cues.mat') # Example data's cue tye array
# cues = cues['c']
# print_all_content(data)

# ### Trial ID decomposition
# t_exp = get_trials(cues, mode='block', l=0, r=100)
# t_unx = get_trials(cues, mode='trial', l=0, r=100)

    