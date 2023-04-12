# structure

The tines of an mbira dzavadzimu are laid out accordingly:

![mbira org-octave-chart](https://user-images.githubusercontent.com/125773761/231325679-ff703020-5514-493d-ac6c-2b9349e2e3b4.jpg)

Hence it makes sense to structure the digital approximation of an mbira in the same way.

Let $B$ be the set of tines in the lower left register, $L$ be the set of tines in the middle left register, and $R$ be the set of tines in the right register. The tines are then numbered in increasing order from the lowest pitch, such that the upper right tine (in red) is $R_9$ and the upper left tine (also in red) is $L_6$ (zero-indexed).

Paul Berliner's "The Soul of Mbira" (1978) compares the tunings of five different instruments observed in Zimbabwe. One such tuning, that of a certain John Gondo's mbira, is described by the sets of frequencies that follow:

$B = \set{122, 147, 161, 177, 197, 215, 263} \land L = \set{241, 363, 325, 393, 432, 480} \land R = \set{293, 485, 538, 616, 660, 733, 800, 878, 981}$

The [mathematics](mathematics.md) describe a solution to a differential equation with respect to time that depends on length and displacement.

To restrict displacement to a set of three values — e.g. $B_{\Delta x} = 0.4, L_{\Delta x} = 0.2, R_{\Delta x} = 0.05$ — is to reduce the domain of the problem to two dimensions and simplify future progress.

Suppose there exists a program that listens on standard input. When the program encounters correct input, it create a new audio stream, generate a damped sinusoid, and write it to that stream. This may offload the summation of signals to pyAudio. An alternative mechanism is to have one stream for each tine, though this may prove inefficient.

[^1]: May as well work to embrace functional programming with a language like Python.
