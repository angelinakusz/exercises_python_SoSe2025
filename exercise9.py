# -*- coding: utf-8 -*-
"""
Created on Thu May 22 10:15:18 2025

@author: s_kusz21
"""

import numpy as np

a = np.arange(1, 13)

print(a)

a_reshaped = a.reshape(3, 2, 2)

print(a_reshaped)

print(a_reshaped.ndim)
print(a_reshaped.size)
print(a_reshaped.shape)
print(a_reshaped.dtype)
