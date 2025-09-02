# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 02:51:05 2021

@author: mahsa
"""

import mne as mne
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, ifft2, fftfreq, fft2, fftshift,fftn, ifftn

eeg = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)

eeg.load_data()
# eegdata = eeg.load_data()
eeg.info['bads'] = ['ECG']
eeg.filter(l_freq=None, h_freq=15)  # low-pass filter 
eeg.plot(n_channels=1,clipping=1.)