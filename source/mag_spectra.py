import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import signal
from scipy.signal import stft

#time domain plot
###################################################
# Load audio file
audio_file = 'C:\\...file_location\\samples_B1.wav'
signal, sr = librosa.load(audio_file)

plt.figure(figsize=(14, 5))
librosa.display.waveshow(signal, sr=sr)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Time-domain waveform")
plt.show()
#magnitude spectrum
####################################################
sample_rate, audio_data = wavfile.read("C:\\...file_location...\\samples_B1.wav")

fft = np.fft.fft(audio_data)
magnitude_spectrum = np.abs(fft)
freq_axis = np.linspace(0, sample_rate, len(magnitude_spectrum))

plt.plot(freq_axis, magnitude_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum')
plt.show()
#sepctrogram - dB scaling
####################################################
data, sr = librosa.load(audio_file)
stft = librosa.stft(data)
spec = librosa.magphase(stft)[0]

librosa.display.specshow(librosa.amplitude_to_db(spec, ref=np.max), y_axis='linear', x_axis='time', sr=sr)
plt.colorbar(format='%+2.0f dB')
plt.title('Magnitude spectrogram')
plt.show()
