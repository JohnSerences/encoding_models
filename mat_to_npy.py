#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:32:37 2019

@author: johnserences
"""

import numpy as np
import scipy.io as sio

# mary's fmri data 
mat_data = sio.loadmat("s03_data.mat")

# loop over all keys pairs in the dictionary
# prompt user to decide to keep each entry...
# this isn't very effecient for a dictionary with lots of entries...
# with each user answer either keep or remove the key from a list, then
# use that to grab out the relevant values in the origianl dictionary (this
# won't require a copy of the entire dict)
k = list(mat_data.keys())
nKey = len(mat_data.keys())

# loop over keys to prompt user to decide what to keep...
for i in range(0,nKey):
    keep_key = input('Do you want to save this key/value to the npy file [y/n]? ' + k[i] + ': ')
    asking = True
    
    # start a loop - just a way to make sure that we get a valid entry of 
    # y or n
    while asking:
        if keep_key=='y':
            asking = False
        elif keep_key=='n':
            k.remove(k[i])
            asking = False
        else:
            keep_key = input('Do you want to save this key/value to the npy file [y/n]? ')

print(k)
# data = tmp["eeg_data"]
# time_x = np.squeeze(tmp["time_x"].T)
# trial_codes = np.squeeze(tmp["trial_codes"])
# srate = np.squeeze(tmp["srate"])

# # The .npz file format is a zipped archive of files named after the variables they contain.
# np.savez("eeg_data01.npz", data=data, tx=time_x, trial_codes=trial_codes, sr=srate)
