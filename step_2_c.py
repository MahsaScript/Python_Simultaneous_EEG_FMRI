# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 07:15:55 2021

@author: Mahsa
"""


import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)
import numpy as np

raw = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)
#
ica = ICA(n_components=20, max_iter='auto', random_state=97)

# filt_raw = raw.copy()
# filt_raw.load_data().filter(l_freq=1., h_freq=None)
raw.set_montage('standard_1020',on_missing='ignore')

ica.fit(raw)
ica.plot_components()