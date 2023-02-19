# mbira-modelling

Mbira is a family of instruments that originated in Zimbabwe over 500 years ago.
The music is characterized by melodic and complex rhythmic variations on a theme, akin to improvized Euro-Classical music.

[![external mbira video](https://img.youtube.com/vi/tKbfUEhjuH4/0.jpg)](https://www.youtube.com/watch?v=tKbfUEhjuH4)

I am motivated to explore physical modelling techniques on a variety of levels:

- Basic: generate tones with a differential equation that describes the motion of a tine of a certain dimension, struck with a specific velocity.

- Intermediate: synthesize a differential equation that decribes the resonance of the wooden soundboard, and combine.

- Advanced: consider FM synthesis techniques to add noise and buzzing to generated tones.


It would not be difficult to write score files and MIDI capabilities with a functional basic implementation.
At that point, we would determine the applicability of real-time wave calculation versus a wavetable stored in memory.

My current thoughts are that, due to the small count of tines (n < 30), the wavetable approach makes more sense.
However, that may not afford variable velocity — in which case, I think real-time tone generation makes more sense.

I have considered Rust as the language of choice, though I am not attached to that approach and open to alternatives.
