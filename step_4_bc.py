# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:30:20 2021

@author: Mahsa
"""
import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)
import matplotlib.pyplot as plt
import numpy as np

#
raw_fname = data_path + '/MEG/sample/1.fif'
event_fname = data_path + '/MEG/sample/2.fif'
fname_fwd = data_path + '/MEG/sample/3.fif'
# Get epochs
event_id, tmin, tmax = [1, 2], -0.2, 0.5

# Read forward model
forward = mne.read_forward_solution(fname_fwd)

# Setup for reading the raw data
raw = mne.io.read_raw_fif(raw_fname, preload=True)
raw.info['bads'] = ['ECG']  # 2 bads channels
events = mne.read_events(event_fname)

# Pick the channels of interest
raw.pick(['Fp1'])

# Read epochs
proj = False  # already applied
epochs = mne.Epochs(raw, events, event_id, tmin, tmax,
                    baseline=(None, 0), preload=True, proj=proj,
                    )
evoked = epochs.average()

# Visualize sensor space data
evoked.plot_joint()


noise_cov = mne.compute_covariance(epochs, tmin=tmin, tmax=0, method='shrunk',
                                   rank=None)
data_cov = mne.compute_covariance(epochs, tmin=0.04, tmax=0.15,
                                  method='shrunk', rank=None)


filters = make_lcmv(evoked.info, forward, data_cov, reg=0.05,
                    noise_cov=noise_cov, pick_ori='max-power',
                    weight_norm='nai', rank=None)
print(filters)

stc = apply_lcmv(evoked, filters, max_ori_out='signed')

clim = dict(kind='value', pos_lims=[0.3, 0.6, 0.9])
stc.plot(src=forward['src'], subject='sample', subjects_dir=subjects_dir,
         clim=clim)