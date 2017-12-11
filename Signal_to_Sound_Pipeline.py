import pyaudio
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import PyAstronomy as PyA
from astropy.io import ascii
from numpy import fft



p = pyaudio.PyAudio()

volume = 0.007    # range [0.0, 1.0]
fs = 5000       # sampling rate, Hz, must be integer
duration = 100.0   # in seconds, may be float
f = 550.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
other=np.random.normal(0,0.2,10000)
drift=ascii.read('/Users/iraf1/Desktop/n3_5.txt') #Best drift scan 
scan_1=np.abs(drift['5352'][0:100000]-5)
f=np.fft.fft(scan_1[0:100000])

print other
print samples 
# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*f)





stream.stop_stream()
stream.close()

p.terminate()

p.terminate()