# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 08:46:40 2021

@author: mahsa
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


eeg = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/15-#P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr', 
                                  preload=True)
eeg.info['bads']=['ECG']
eeg.load_data()
print(eeg.ch_names)
ch_names=['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T7', 'T8', 'P7', 'P8', 'Fz', 'Cz', 'Pz', 'Oz', 'FC1', 'FC2', 'CP1', 'CP2', 'FC5', 'FC6', 'CP5', 'CP6', 'TP9', 'TP10', 'POz', 'F1', 'F2', 'C1', 'C2', 'P1', 'P2', 'AF3', 'AF4', 'FC3', 'FC4', 'CP3', 'CP4', 'PO3', 'PO4', 'F5', 'F6', 'C5', 'C6', 'P5', 'P6', 'AF7', 'AF8', 'FT7', 'FT8', 'TP7', 'TP8', 'PO7', 'PO8', 'FT9', 'FT10', 'Fpz', 'CPz']
picks=mne.pick_channels(ch_names, include=[], exclude=['bads'], ordered=False)

eeg.filter(l_freq=0.01, h_freq=0.1)  # low-pass filter 
eeg.plot(duration=10.0, start=0.0, n_channels=len(picks),show_scrollbars=True,clipping=1)
print(eeg.info)





