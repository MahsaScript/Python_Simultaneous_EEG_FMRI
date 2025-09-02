# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 08:52:42 2021

@author: Mahsa
"""

import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)
import matplotlib.pyplot as plt
import numpy as np

raw = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)
#
ica = ICA(n_components=20, max_iter='auto', random_state=97)

filt_raw = raw.copy()
filt_raw.load_data().filter(l_freq=8, h_freq=13)
filt_raw.set_montage('standard_1020',on_missing='ignore')


raw_downsampled = filt_raw.resample(sfreq=1)

# for data, title in zip([filt_raw, raw_downsampled], ['Original', 'Downsampled']):
#     fig = data.plot_psd(average=True)
#     fig.subplots_adjust(top=0.9)
#     fig.suptitle(title)
#     plt.setp(fig.axes, xlim=(0, 300))
    
# ica.fit(filt_raw)


# ica.plot_properties(filt_raw, picks=[0, 1]) # It is possible [0, 1, 2, ...., 18, 19]

 
#Smoothing and Recitify 
# ica.plot_properties(filt_raw, picks=[0, 1],  psd_args={'fmin':8 ,'fmax': 13.},
#                      image_args={'sigma': 1.}) # It is possible [0, 1, 2, ...., 18, 19]

ica.plot_properties(raw_downsampled, picks=[0])