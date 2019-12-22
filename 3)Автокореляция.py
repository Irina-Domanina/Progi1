#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Обращаемся к библиотекам
import scipy.io as sio
import math
import matplotlib.pyplot as plot
import numpy as np
from scipy import signal
from numpy.fft import fft


mat_contents = sio.loadmat('33484K-HFS.mat')# Считываем файл
T = mat_contents['tbKH']# Задаем масив
A = mat_contents['sigKH']
Fs = 1.0/(T[0,1]-T[0,0])# Задаем частоту дискретизации
#print (T,A)
print (1/Fs)
print (T.size)
print (T.max())
#print (A)
# a = 6.0000005/(0.05)
# b = 12000002/a
# print(a,b)

A1 = A[0:100000,0]
T1 = T[0,0:100000]
plot.figure(1,figsize=(8,6)) # Строим график сигнала диапазоном в 50 мс
plot.plot(T1,A1)

CORR = signal.correlate(A1, A1)[0:100000]
N = len(CORR)
half = CORR[N//2:]
plot.figure(2,figsize=(8,6)) # Строим график автокорреляции
plot.plot(half)
plot.xlim(0, 10000)

# cr = (3000*5e-7)*3e8
# print ('cr =', cr)

