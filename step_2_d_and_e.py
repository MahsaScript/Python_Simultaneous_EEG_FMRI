# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 08:01:38 2021

@author: mahsa
"""


import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)
import numpy as np

raw = mne.io.read_raw_brainvision('C:/Users/User/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)
#
ica = ICA(n_components=20, max_iter='auto', random_state=97)

filt_raw = raw.copy()
filt_raw.load_data().filter(l_freq=8, h_freq=13)
filt_raw.set_montage('standard_1020',on_missing='ignore')

ica.fit(filt_raw)
# ica.plot_components()

# ica.plot_properties(filt_raw, picks=[0, 1]) # It is possible [0, 1, 2, ...., 18, 19]

 # psd_args={'fmax': 35.},
 #                    image_args={'sigma': 1.}
 
#Smoothing and Recitify 
ica.plot_properties(filt_raw, picks=[0, 1],  psd_args={'fmin':8 ,'fmax': 13.},
                     image_args={'sigma': 1.}) # It is possible [0, 1, 2, ...., 18, 19]
