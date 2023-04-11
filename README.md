# mbira-modelling
Mbira is a family of instruments that originated in Zimbabwe over 500 years ago.
The music is characterized by melodic and complex rhythmic variations on a theme, akin to European classical music (but with a greater historical emphasis on night-long parties and trance-induced spirit medium possession).

[![external mbira video](https://img.youtube.com/vi/tKbfUEhjuH4/0.jpg)](https://www.youtube.com/watch?v=tKbfUEhjuH4)

Click the above image to be linked to a beautiful youtube video.


## About the project

- Objective 1 is to define a differential equation that describes the dampened sinusoidal motion of a struck mbira tine, and graph the oscillation.

- Objective 2 is to give consideration to the timbre of the instrument. Ideas are: to use FM synthesis to simulate the rasp of a thumb sliding off of a displaced tine; and to use resonance to simulate, well, the resonance of the soundboard.

- Objective 3 is to create a digital structure that replicates the complex layout of tines on an mbira.

- Objective 4 is to write a program that will play an input score.

- Objective 5, if time affords it, will be to implement a FFT to deconstruct a recorded mbira performance into a score.


## Project Progress

- Objective 1 is complete. [Mathematics.md](mathematics.md) demonstrates a mathematical model of a tine that preserves the octave relationship. [Tine.c](tine.c) lays the foundation for a discrete-time solution to the differential equation.

## Todo
Expand tine.c into the time domain.
Consider the value of a type(complex double) implementation and consider the solution as a (sine, cosine) pair. Then plot a damped sinusoid. 
