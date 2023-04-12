import math
import numpy as np
import pyaudio
import sys

SAMPLE_RATE = 44100

DENSITY = 0.0075
RIGIDITY = 52500000.0
DAMPER = 0.0006

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

# output audio using PyAudio
def output(p, t):
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=SAMPLE_RATE,
                    output=True)

    stream.write(t.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()

# main
# runs as script of two parameters: tine displacement (mm) and length (mm)
# e.g. $ python3 tine.py 0.4 128
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 tine.py displacement length")
        sys.exit()
    
    x = float(sys.argv[1])

    l = float(sys.argv[2])
    w = l * 0.05
    d = 2.5
    
    v = volume(l, w, d)
    
    m = mass(v, DENSITY)
    K = k(RIGIDITY, v, l)
    
    a = alpha(m, DAMPER)
    b = beta(m, DAMPER, K)

    p = pyaudio.PyAudio()

    t = np.arange(SAMPLE_RATE*6)
    f = lambda s : x*math.exp(a*s)*math.sin(b*s)

    output(p, np.array(list(map(f, t))))

    p.terminate()
