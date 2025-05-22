# -*- coding: utf-8 -*-
"""
Created on Thu May 22 10:40:27 2025

@author: s_kusz21
"""

import math
import numpy as np

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

x_log = []
for wert in x:
    x_log.append(math.log10(wert))
    
print(x_log)

logs_vec = np.log10(x)

print(logs_vec)