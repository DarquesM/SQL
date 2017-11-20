# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:57:10 2017

@author: mdarq
"""

import numpy as np
#from matplotlib import pyplot as plt
import seaborn as sns

r = np.array([np.random.rand() for i in range(10000)])
beta = (r*0.09) + 0.9
#beta = 1-10**(-r-1)
#beta = 1-10**(-r+1)
beta = r*0.9+0.09
sns.distplot(beta)