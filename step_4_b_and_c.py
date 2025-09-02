# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:29:58 2021

@author: Mahsa
"""

import mne as mne
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, ifft2, fftfreq, fft2, fftshift,fftn, ifftn
import os
import mne
import numpy as np
import matplotlib.pyplot as plt


raw = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr', 
                                  preload=True)
raw.load_data()

subjects_dir = r'C:\Users\Mahsa\Desktop\Tasks\#####15-P3119-16 Tir\subxp210\subjects\bst_resting\mri\T1.PNG'
# raw.apply_gradient_compensation(3)
cov = mne.compute_raw_covariance(raw,tmin=0, tmax=5)  # compute before band-pass of interest

raw.filter(8, 13)
raw = raw.resample(1)
events = mne.make_fixed_length_events(raw, duration=5.)
epochs = mne.Epochs(raw, events=events, tmin=0, tmax=5.,
                    baseline=None,  preload=True)

# This source space is really far too coarse, but we do this for speed
# considerations here
pos = 15.  # 1.5 cm is very broad, done here for speed!
src = mne.setup_volume_source_space()
fwd = mne.make_forward_solution(epochs.info, src)
data_cov = mne.compute_covariance(epochs)
filters = make_lcmv(epochs.info, fwd, data_cov, 0.05, cov,
                    pick_ori='max-power', weight_norm='nai')

epochs.apply_hilbert()  # faster to do in sensor space
stcs = apply_lcmv_epochs(epochs, filters, return_generator=True)
corr = envelope_correlation(stcs, verbose=True)

degree = mne.connectivity.degree(corr, 0.15)
stc = mne.VolSourceEstimate(degree, [src[0]['vertno']], 0, 1, 'bst_resting')
brain = stc.plot(
    src, clim=dict(kind='percent', lims=[75, 85, 95]), colormap='gnuplot',
    subjects_dir=subjects_dir, mode='glass_brain')