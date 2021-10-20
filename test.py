import scipy.io as sio
from Methods import *
from Granger import *

### Load data and show content of it
# data = sio.loadmat('data.mat') # Example data, private access
# cues = sio.loadmat('cues.mat') # Example data's cue tye array
# cues = cues['c']
# print_all_content(data)

# ### Trial ID decomposition
# t_exp = get_trials(cues, mode='block', l=0, r=100)
# t_unx = get_trials(cues, mode='trial', l=0, r=100)

psd, freqs = power_spectrum_density(data=data, key='pfc', save=True, t1=2500, t2=4500, fmin=0,
            fmax=100, normalize_w=True, bw=45, k=0, trials=t_exp)


pink_noise_inverse_filter(x=, w=5)