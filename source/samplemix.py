import os
import soundfile as sf
import sounddevice as sd

# Define file pairs
#NOTE: change file location to what is needed
file_pairs = [(os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_L1.wav'), 
               os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_R2.wav')),
              (os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_L2.wav'), 
               os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_R2.wav')),
              (os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_L5.wav'), 
               os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_R1.wav')),
              (os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_L5.wav'), 
               os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_R1.wav')),
              (os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_L2.wav'), 
               os.path.join('C:\\', 'Users', 'Documents', 'uvic', 'csc484d', 'samples', 'samples_R3.wav'))]

# Loop through each pair
for file_pair in file_pairs:
    # Readaudio files
    data1, samplerate1 = sf.read(file_pair[0])
    data2, samplerate2 = sf.read(file_pair[1])

    # audio files must have same sample rate
    if samplerate1 != samplerate2:
        raise ValueError("Error: Files have different sample rates")

    # Truncate the longer audio to match the shorter audio
    min_length = min(len(data1), len(data2))
    data1 = data1[:min_length]
    data2 = data2[:min_length]

    # Mix the audio
    mixed_data = (data1 + data2) / 2

    # Play
    sd.play(mixed_data, samplerate1, blocking=True)
