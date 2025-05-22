# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""

import matplotlib.pyplot as plt

def buchstabe_häufigkeit(x):
    
    mein_d = {}
    
    x_lower = x.lower()
    
    for b in x_lower:
        
        if b.isalpha():
            
            if b in mein_d:
                
                mein_d[b] += 1
                
            else:
                
                mein_d[b] = 1
                
    mein_d_sorted = dict(sorted(mein_d.items()))
    
    return mein_d_sorted


bh_dict = buchstabe_häufigkeit(x = "123banana!!!")

plt.bar(bh_dict.keys(), bh_dict.values())
