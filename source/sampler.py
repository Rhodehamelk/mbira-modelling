import os
import soundfile as sf
import sounddevice as sd
import itertools

# this is the most rudimentary form of Karigamombe, traditional mbira dzavadzimu repertoire
notes = [('L1', 'R2'), ('L2', 'R2'), ('L5', 'R1'), ('L5', 'R1'), ('L2', 'R3'), ('L2', 'R3'),
         ('L1', 'R2'), ('L2', 'R2'), ('L5', 'R1'), ('L5', 'R1'), ('L4', 'R1'), ('L4', 'R1'),
         ('L1', 'R2'), ('L2', 'R2'), ('L3', 'R2'), ('L3', 'R2'), ('L4', 'R1'), ('L4', 'R1'),
         ('B7', 'R3'), ('L4', 'R3'), ('L3', 'R2'), ('L3', 'R2'), ('L4', 'R1'), ('L4', 'R1')]

# Loop infinitely through the tune
for pair in itertools.cycle(notes):
    # Readaudio files
    data1, samplerate1 = sf.read(os.path.join('samples', pair[0]+'.wav'))
    data2, samplerate2 = sf.read(os.path.join('samples', pair[1]+'.wav'))

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
