import math
import numpy as np
import pyaudio
import sys

SAMPLE_RATE = 44100

DENSITY1 = 0.0300
DENSITY2 = 0.0090

RIGIDITY1 = 52500000.0
RIGIDITY2 = 52500000.0
DAMPER = 0.0003

# time
def linspace(duration):
    L = duration+1
    l = 0
    d = 1.0

    t = np.linspace(l, d, L)
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
d = 1.0

v = volume(l, w, d)

#added variability for Density and Rigidity 

m1 = mass(v, DENSITY1)
m2 = mass(v, DENSITY2)

K1 = k(RIGIDITY1, v, l)
K2 = k(RIGIDITY2, v, l)

a1 = alpha(m1, DAMPER)
b1 = beta(m1, DAMPER, K1)

a2 = alpha(m2, DAMPER)
b2 = beta(m2, DAMPER, K2)

# command line arguments for amplitude and time length
#example: python3 tine_python.py 0.5 4
if len(sys.argv) != 3:
    print("Usage: python3 script_name.py amplitude time_length")
    sys.exit()

# convert command line arguments to float
A = float(sys.argv[1])
seconds = float(sys.argv[2])
duration = int(seconds*SAMPLE_RATE)

#two tine outputs 
t1 = np.zeros(duration+1)
t2 = np.zeros(duration+1)

t = linspace(duration)
for n in range(duration+1):
    t1[n] = A*math.exp(a1*n)*math.sin(b1*n)
    t2[n] = A*math.exp(a2*n)*math.sin(b2*n)

t = t1 + t2

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
