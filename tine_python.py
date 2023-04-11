import math
import numpy as np
import pyaudio

SAMPLE_RATE = 44100

DENSITY = 0.0075
RIGIDITY = 52500000.0
DAMPER = 0.0003

# time
def linspace(duration):
    L = duration+1
    l = 0
    d = 1.0

    t = np.zeros(L)
    step = (d - l) / (L - 1)
    for n in range(L):
        t[n] = l + (n*step)
    return t

# volume
def volume(length, width, depth):
    return length*width*depth

# mass
def mass(volume, density):
    return volume*density

# spring constant
def k(G, volume, length):
    u = G*volume
    v = length**2

    return u/v

# root 1
def alpha(m, b):
    return -b/(2.0*m)

# root 2
def beta(m, b, k):
    discriminant = math.sqrt((4*m*k - b**2))
    return discriminant/(2.0*m)

# period
def period(b):
    return (2.0*math.pi)/b

# frequency
def frequency(T):
    return 1.0/T

l = 128
w = 100.0/15.0
d = 1.0

v = volume(l, w, d)

m = mass(v, DENSITY)
K = k(RIGIDITY, v, l)

a = alpha(m, DAMPER)
b = beta(m, DAMPER, K)

#TODO: parameterize amplitude with displacement (in mm)
A = 1

#TODO: move this to its own function
seconds = 4
duration = seconds*SAMPLE_RATE

t = linspace(duration)
for n in range(duration+1):
    t[n] = A*math.exp(a*n)*math.sin(b*n)

# output audio using PyAudio
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLE_RATE,
                output=True)

stream.write(t.astype(np.float32).tobytes())

stream.stop_stream()
stream.close()

p.terminate()
