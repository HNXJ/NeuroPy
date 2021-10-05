import os.path as op

import numpy as np
import matplotlib.pyplot as plt

import mne
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
from mne.datasets import somato


mne.time_frequency.psd_multitaper(inst, fmin=0, fmax=inf, tmin=None, tmax=None, bandwidth=None, adaptive=False, low_bias=True, normalization='length', picks=None, proj=False, n_jobs=1, reject_by_annotation=False, verbose=None)