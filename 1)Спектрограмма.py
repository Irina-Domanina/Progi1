#!/usr/bin/env python
# coding: utf-8

# In[6]:


#подключение нужных библиотек
import matplotlib.pyplot as plot            #Для построения графика
import numpy as np                          #Для массивов и операций с ними
import random                               #Для случайных чисел


minf=random.randint(10,1000)
print(minf)
maxf=random.randint(minf,10000)
print(maxf)
amount=20
frequencies = np.random.randint(minf,maxf, amount)


samplingFrequency   = maxf*2                                #Для разбиения

s1 = np.empty([0]) # For samples                            #Создаем два пустых массива для записи данных
s2 = np.empty([0]) # For signal

start   = 1
stop    = samplingFrequency+1

for frequency in frequencies:
    sub1 = np.arange(start, stop, 1)                                                     #Массив в диапазоне от start до stop
                                                                                         #с единичным шагом (время?)
        
    sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)+np.random.randn(len(sub1))
    #Cигнал  - синус аргумента 2*время*(частота/дискретизацию)+шум(массив длины sub1 из нормального распределения(0,1))
    
    s1      = np.append(s1, sub1) #добавляем элементы в массивы
    s2      = np.append(s2, sub2)

    start   = stop+1                  #сдвигаем диапазон времен
    stop    = start+samplingFrequency
    

plot.subplot(211)              #Cтроим сигнал, subplot для постройки в одном окне
plot.plot(s1,s2)               
plot.xlabel('Sample')
plot.ylabel('Амплитуда')

plot.subplot(212)              #Строим спектр
powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s2, Fs=samplingFrequency)
plot.ylabel('Frequency')

 

plot.show()


# In[ ]:





# In[ ]:




