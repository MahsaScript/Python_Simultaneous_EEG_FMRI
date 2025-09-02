# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 01:05:20 2021

@author: Mahsa
"""

import os
import nibabel as nib
from nibabel.testing import data_path
import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)

inputfile = r'C:\Users\User\Desktop\Tasks\#####15-P3119-16 Tir\github_repo (3)\python\nii\sub-xp222_func_sub-xp222_task-2dNF_run-02_bold.nii'
outputfile = r'C:\Users\User\Desktop\Tasks\#####15-P3119-16 Tir\github_repo (3)\python\nii\bold'

img_fname = os.path.join(data_path, 'example4d.nii.gz')

def aff_mni2tal(inpoint):
    Tfrm = [[0.88, 0, 0, -0.8], [0, 0.97, 0, -3.32], [0, 0.05, 0.88, -0.44],[0, 0, 0, 1]]
    tmp = Tfrm * np.transpose([inpoint, 1])
    outpoint =np.transpose( tmp[1:3])
    
    mni2tal( [10, 12, 14] )

raw = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp22/sub-xp222_task-2dNF_run-02_eeg.vhdr', misc='auto', scale=1.0, preload=True, verbose=None)  # load data  
raw.load_data()
raw.info['bads'] = ['ECG']  # mark bad channels  
raw.filter(l_freq=None, h_freq=1.0)  # low-pass filter 

raw_epochs = mne.preprocessing.find_ecg_events(raw)
raw_epochs.plot_image(combine='mean')
 
events = mne.find_events(raw, 'STI014')  # extract events and epoch data 
epochs = mne.Epochs(raw, events, event_id=1, tmin=-0.2, tmax=0.5,  
                    reject=dict(grad=4000e-13, mag=4e-12))  
evoked_1 = epochs.average()  # compute evoked  

raw = mne.io.read_raw_brainvision('C:/Users/Mahsa/Desktop/Tasks/#####15-P3119-16 Tir/subxp222/sub-xp222_task-2dNF_run-02_eeg.vhdr', misc='auto', scale=1.0, preload=True, verbose=None)  # load data  
raw.load_data()
raw.info['bads'] = ['ECG']  # mark bad channels  
raw.filter(l_freq=None, h_freq=1.0)  # low-pass filter 

Tn=[ [0.99,  0,     0,      0],
    [ 0,   0.9688,  0.042,  0],
    [ 0,   -0.0485, 0.839,  0],
    [ 0,    0,       0,     1]]
    
  
Tn=[ [0.99,  0,     0,      0],
    [ 0,   0.9688,  0.046,  0],
    [ 0,   -0.0485, 0.9189,  0],
    [ 0,    0,       0,     1]]

    
raw_epochs = mne.preprocessing.find_ecg_events(raw)
raw_epochs.plot_image(combine='mean')
 
events = mne.find_events(raw, 'STI014')  # extract events and epoch data 
epochs = mne.Epochs(raw, events, event_id=1, tmin=-0.2, tmax=0.5,  
                    reject=dict(grad=4000e-13, mag=4e-12))  
evoked_2 = epochs.average()  # compute evoked  

aud_minus_vis = mne.combine_evoked([evoked_1, evoked_2], weights=[1, -1])
aud_minus_vis.plot_joint()
grand_average = mne.grand_average([evoked_1, evoked_2])
print(grand_average)















