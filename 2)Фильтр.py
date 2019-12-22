#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Обращаемся к библиотекам
import scipy.io as sio
import math
import matplotlib.pyplot as plot
import numpy as np
from scipy import signal
from numpy.fft import fft, fftfreq, fftshift

mat_contents = sio.loadmat('30303MHG_Isat_09.mat')# Считываем файл
T = mat_contents['tb']# Задаем масив
A = mat_contents['sig']
Fs = 1.0/(T[0,1]-T[0,0])# Задаем частоту дискретизации 
print (T,A)
print (Fs)

plot.figure(1,figsize=(8,6)) # Строим график сигнала
plot.plot(T[0,:],A[:,0])

b, a = signal.butter(2,3, fs=Fs)# Задаем параметры фильтра, порядок и верхнюю границу частот
fgust = signal.filtfilt(b, a, A[:,0], method="gust")# Используем метод Густавсона. 
plot.figure(2,figsize=(8,6))#Строим отфильтрованный график сигнала
plot.plot(T[0,:],fgust)
plot.figure(3,figsize=(8,6))#Строим на одном графике сигнал и отфильтрованный сигнал
plot.plot(T[0,:],A[:,0], 'r-')
plot.plot(T[0,:],fgust, 'b-', linewidth=2)

f, t, Sxx = signal.spectrogram(A[:,0], fs=Fs) # Строим спектрограмму сигнала
Sxx = np.log(Sxx)
plot.figure(4)
plot.pcolormesh(t, f, Sxx)

f, t, Sxx = signal.spectrogram(fgust, fs=Fs) # Строим спектрограмму отфильтрованного сигнала
Sxx = np.log(Sxx)
plot.figure(5)
plot.pcolormesh(t, f, Sxx)

#n= A.size
#t=1/Fs
# yf = fft( A[:,0])
#xf = fftfreq(n, t)
#xf = fftshift(xf)
#yplot = fftshift(yf)
#plot.plot(xf, 1.0/n * np.abs(yplot))
#plot.grid()
# n= A.size
# t = np.linspace(0, 1/Fs, n/2)
# X = fft(A[:,0])

# t[1] - t[0] = sample rate
# 1/(t[1] - t[0]) = frequency
# freq = np.linspace(0, 1 / (t[1] - t[0]), n/2)[: (n // 2)]

# 1 / N is a normalization factor
# X_amp = (1/n) * np.abs(X)[: (n // 2)]

# plot.figure
# plot.plot(freq, X_amp)
#spectrum = fft(A[:,0])
#plot.figure(6)
#plot.plot(spectrum)


# In[ ]:




