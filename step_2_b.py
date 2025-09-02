# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 06:16:38 2021

@author: mahsa
"""

import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)
import numpy as np

raw = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)
events=mne.events_from_annotations(raw)
print(mne.events_from_annotations(raw))

reject = dict(grad=4000e-13,  # unit: T / m (gradiometers) Gradient Remove
              mag=4e-12,      # unit: T (magnetometers)
              eeg=40e-6,      # unit: V (EEG channels)
              eog=250e-6      # unit: V (EOG channels)
              )

epochs = mne.Epochs(raw, events[0],  tmin=-0.2, tmax=0.5,  
                     reject_by_annotation=True) 
evoked = epochs.average()  # compute evoked  
evoked.plot()  # butterfly plot the evoked data 
















# picks_meg = mne.pick_types(raw.info, meg=True, eeg=False, eog=True,
#                            stim=False, exclude='bads')
# eog_average = create_eog_epochs(raw, reject=dict(mag=5e-12, grad=4000e-13),
#                                 picks=picks_meg).average()
# raw = mne.io.read_raw_fif(sample_data_raw_file)
# raw.crop(tmax=60.)

# Visualizing the artifacts
# pick some channels that clearly show heartbeats and blinks
# regexp = r'(ECG)'
# artifact_picks = mne.pick_channels_regexp(raw.ch_names, regexp=regexp)
# raw.plot( n_channels=len(artifact_picks),
#          show_scrollbars=False)
# raw.plot_psd(tmax=np.inf, fmax=250)


# eog_evoked =  create_ecg_epochs(raw).average()
# eog_evoked.apply_baseline(baseline=(None, -0.2))
# eog_evoked.plot_joint()