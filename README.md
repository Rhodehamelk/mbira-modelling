# mbira-modelling
Mbira is a family of instruments that originated in Zimbabwe over 500 years ago.
The music is characterized by melodic and complex rhythmic variations on a theme, akin to European classical music (but with a greater historical emphasis on night-long parties and trance-induced spirit medium possession).

[![external mbira video](https://img.youtube.com/vi/tKbfUEhjuH4/0.jpg)](https://www.youtube.com/watch?v=tKbfUEhjuH4)

Click the above image to be linked to a beautiful youtube video.


## About the project

- Objective 1 is to define a differential equation that describes the dampened sinusoidal motion of a struck mbira tine, and graph the oscillation.

- Objective 2 is to determine the modes with which a given tine oscillates.

- Objective 3 is to give consideration to the timbre of the instrument. Ideas are: to use FM synthesis to simulate the rasp of a thumb sliding off of a displaced tine; and to use resonance to simulate, well, the resonance of the soundboard.

- Objective 4 is to create a digital structure that replicates the complex layout of tines on an mbira.

- Objective 5 is to write a program that will play an input score.

- Objective 6, if time affords it, will be to implement a FFT to deconstruct a recorded mbira performance into a score.


## Project Progress

- Objective 1 is complete. [Mathematics.md](mathematics.mc) describes a mathematical model of a tine, and demonstrates preservation of the octave relationship between tines of length $l$ and $2l$. [Tine.c](tine.c) programmatically implements the mathematics.

- Objective 2 see [Modality.md](modality.md) for progress.


## Todo
- Record the sound of a single tine being struck such that it can be decomposed into a set of modes.

- Implement the simplified tine wavetable as an array of complex doubles. Then DFT decomposition becomes feasible. Possibly requires the general solution of the ODE to be restructured.
