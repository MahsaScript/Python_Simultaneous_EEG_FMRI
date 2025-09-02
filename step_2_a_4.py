# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 07:02:59 2021

@author: mahsa
"""
import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)
import numpy as np

raw = mne.io.read_raw_brainvision('C:/Users/User/Desktop/Tasks/#####15-P3119-16 Tir/subxp210/sub-xp210_task-2dNF_run-02_eeg.vhdr',preload=True)

raw_epochs = mne.preprocessing.find_ecg_events(raw)
raw_epochs.plot_image(combine='mean')