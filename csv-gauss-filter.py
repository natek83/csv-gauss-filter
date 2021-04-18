#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 00:16:04 2021

@author: nate

"""

# This filter will smooth out local variations between cells due to long term
# trim noise but can't be used to interpolate or form regression lines to 
# follow overall trends/patterns, using a wide radius will tend to bring all
# cells towards a global average and would then have to be trimmed out again

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import os
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter

#Filter parameters, keep radius small, adjust strength to keep changes reasonable
strength = 3
radius = .5

#Import fuel.csv from same directory as script, file must contain only values to be 
#smoothed. Will smooth any 1D or 2D table such as base fuel or ve
fname = os.path.join("fuel.csv")
fuel = np.loadtxt(fname, delimiter = ",")

#Apply gaussian filter, 'nearest' mode helps the edges not be as strongly affected
smoothed = np.round((strength*gaussian_filter(fuel, sigma=radius, mode='nearest')+(1-strength)*fuel), 3)

#Calculates the cell percent changes for easily sanity checking parameter values
changes = np.round((fuel/smoothed-1)*100,1)
np.set_printoptions(suppress=True)
print(changes)

#Saves the smoothed table as a .csv file to open in excel and copy back to tuning software
df = pd.DataFrame(smoothed)
df.to_csv('fuel-smoothed.csv',index=True)
