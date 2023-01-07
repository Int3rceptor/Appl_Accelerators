# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:09:01 2023

@author: Janina Hohnholz
"""

import numpy as np 
import matplotlib.pyplot as plt

data=np.loadtxt('2016-07-11_ipm_data.txt')
maximum=max(data)
position=np.where(data==maximum)
fig=plt.figure()
plt.plot(data,'b')
plt.plot(position,maximum,'ro')
plt.rc('grid', linestyle="-", color='black')
plt.grid()
plt.title('Data from an ionisation beam profile monitor (IPM)')
plt.show()
fig.savefig('IPM_out.png', dpi=fig.dpi)