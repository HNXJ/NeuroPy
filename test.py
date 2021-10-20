from matplotlib import pyplot as plt 

import scipy.io as sio
from Methods import *
from Granger import *

# ### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# cues = sio.loadmat('cues.mat') # Example data's cue tye array
# cues = cues['c']
# print_all_content(data)

# ### Trial ID decomposition
# t_exp = get_trials(cues, mode='block', l=0, r=100)
# t_unx = get_trials(cues, mode='trial', l=0, r=100)

# psd, freqs = power_spectrum_density(data=data, key='pfc', save=True, t1=2000, t2=4500, fmin=0,
#             fmax=100, normalize_w=False, bw=45, k=0, trials=[i for i in range(100)])

# psd_ratio_plotter(psd=psd[:, :, 10], freqs=freqs, title="Ratios, trial. 01")
psd_ratio_plotter(psd=psd[:, :, 40], freqs=freqs, title="Ratios, trial. 40")
# psd_ratio_plotter(psd=psd[:, :, 70], freqs=freqs, title="Ratios, trial. 70")

# plt.figure(figsize=(19, 10))
# plt.subplot(1, 1, 1)
# plt.imshow(c)
# # plt.plot(freqs, psd[13, :, 75])
# plt.show()
