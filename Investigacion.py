
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import wave as wav
from scipy.io import wavfile
from scipy import signal


# In[ ]:


def graph_Spectrogram():

    sample_rate, samples = wavfile.read('gamecubemono.wav') # Obtains sample rate and samples from wav file 
    samples = np.fromstring(samples, "Int16") #Converts the samples into a an array that the funtion specgram can read 
    plt.specgram(x = samples, Fs = sample_rate, sides = "onesided", NFFT = 512) #This fuction plots a spectrogram with the given parameters
    plt.show()


graph_Spectrogram()


# In[21]:


def Real_graph_Spectrogram():
    sample_rate, samples = wavfile.read('/home/uva/Desktop/UPRRP/Investigacion/gamecubemono.wav') # Obtains sample rate and samples from wav file 
    samples = np.fromstring(samples, "Int16") #Converts the samples into a an 
                                              #array that the funtion specgram can read 
    spec, f, t, im = plt.specgram(x = samples, Fs =sample_rate, sides = "onesided", NFFT = 512) #This fuction plots a spectrogram with the given parameters
    return spec, f, t
    



# In[27]:


def Clip(time, freq, start, stop, low, hi):
    Stime = np.clip(time, start, stop, out = time)#These two take the data we need to plot a specific point in the Spectrogram
    Sfreq = np.clip(freq, low, hi, out = freq)
    return Stime, Sfreq



# In[22]:


spec, freq, time = Real_graph_Spectrogram()
Stime, Sfreq = Clip(time, freq, 0, 5, 0, 7800)




# In[23]:


plt.pcolormesh(Stime, Sfreq, 10 * np.log10(spec))

