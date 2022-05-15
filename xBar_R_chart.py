#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = [2,3,4,5,6,7,8,9,10,11,12]
A2 = pd.Series([1.88,1.023,0.729,0.577,0.483,0.419,0.373,0.337,0.308,0.285,0.266],index=n)
D3 = pd.Series([0,0,0,0,0,0.076,0.136,0.184,0.223,0.256,0.283],index=n)
D4 = pd.Series([3.267,2.574,2.282,2.114,2.004,1.924,1.864,1.816,1.777,1.744,1.717],index=n)

factors = pd.DataFrame(index=n, data={'A2': A2, 'D3': D3, 'D4':D4})

def diff(x):
    maxx=np.max(x,1)
    minn=np.min(x,1)
    return maxx-minn

# parameter x is the data set of individual measurements
# each row represents the measurements of any period 

def x_bar_R_chart(x):
    nn=x.shape[1]
    x_bar=np.mean(xx,1)
    x_bar_bar = np.mean(xx)
    R = diff(x)
    R_bar = np.mean(diff(x))
    data_x={
        'X_vals': x_bar,
        'UCL_x': x_bar_bar + (R_bar * factors.iloc[nn]['A2']),
        'CEN_x': x_bar_bar ,
        'LCL_x': x_bar_bar - (R_bar * factors.iloc[nn]['A2']),
        'R_vals': R,
        'UCL_R': R_bar * factors.iloc[nn]['D4'],
        'CEN_R': R_bar ,
        'LCL_R': R_bar * factors.iloc[nn]['D3']}
    result = pd.DataFrame(index=range(30),data=data_x)
    return result

# 5 measurements at each of 30 intervals
result = x_bar_R_chart(np.random.randn(30,5))

plt.plot(result['X_vals'],color='blue')
plt.plot(result['UCL_x'],color='red')
plt.plot(result['CEN_x'],color='green')
plt.plot(result['LCL_x'],color='red')

plt.plot(result['R_vals'],color='blue')
plt.plot(result['UCL_R'],color='red')
plt.plot(result['CEN_R'],color='green')
plt.plot(result['LCL_R'],color='red')

