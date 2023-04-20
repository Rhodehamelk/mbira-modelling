# mbira-modelling
Mbira is a family of instruments that originated in Zimbabwe over 500 years ago.
The music is characterized by melodic and complex rhythmic variations on a theme, akin to European classical music (but with a greater historical emphasis on night-long parties and trance-induced spirit medium possession).

[![external mbira video](https://img.youtube.com/vi/tKbfUEhjuH4/0.jpg)](https://www.youtube.com/watch?v=tKbfUEhjuH4)

Click the above image to be linked to a beautiful youtube video.


## Project Objectives

- Objective 1 is to define a differential equation that describes the dampened sinusoidal motion of a struck mbira tine.

- Objective 2 is to write a program that will loop a set of (tine, displacement) instructions in real time.

- Objective 3 is to extend the simplified tine model to include modal resonance, initially based off the first 4 modes of the harmonic series. Perhaps from this extends the resonance of the soundboard.

- Objective 4 is to give consideration to the timbre of the instrument. Ideas are: to use FM synthesis to simulate the rasp of a thumb sliding off of a displaced tine, and/or synthesis rattles and buzzes.


## Project Progress

- Objective 1 is complete. [Mathematics.md](reference/mathematics.md) describes a mathematical model of a tine, and demonstrates preservation of the octave relationship between tines of length $l$ and $2l$. [Tine.c](source/tine.c) programmatically implements the mathematics.

- Objective 2: [Tine.py](source/tine.py) extends the implementation towards the goal of looping a set of tine pairs, akin to a traditional mbira tune. The frameworks appear to be correct in the additive synthesis approach, but specific PyAudio and NumPy format standards have proved difficult to work with (namely, numpy does not support 24-bit PCM). Aside from that, the program seems to work correctly. 

- Objective 3: The frequency spectrum of sampled mbira tines inform the choices to be made about modal resonances, though the project did not advance far enough to implement such considerations.

- Objective 4: did not happen.


## Project Milestones
### Worst Case Scenario
A disjointed digital instrument that does not give consideration to modality, sympathetic resonance, or timbre.

### Expected
A capable digital instrument that is able to loop a set of pitches in some kind of melodic order, and considers modality and timbre.

### Stretch
As expected, but also with consideration to sympathetic resonance.

## Project Roles

Robert drafted the outline, objectives, mathematics, and initial source code.
Kes analyzed samples, added CLI functionality, and implemented the sample-based sequencer.
