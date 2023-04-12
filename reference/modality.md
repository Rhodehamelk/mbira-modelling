# modality

How will the modes of a tine be determined? Perhaps the DFT deconstruction of a sample of a single tine (e.g. the largest) would determine which modes are present.

[GTzan's Modal Synthesis notebook](https://github.com/gtzan/synthesizers_cs_perspective/blob/main/src/notebooks/modal_synthesis.ipynb) appears to be a useful resource to understand modal approximations, however, some of the code snippets are difficult to decipher. `[In 58]` seems to be the most relevant to an extension of the simplified tine model.

The set of modes for the system must be determined first, either by estimated listening or by frequency-domain analysis (i.e. a DFT). It is hoped that the analysis of one tine will lead to recognition of a set of modes that apply to all tines. 

Let it be noted that an accurate decomposition of a recorded tine may be difficult to acquire, based on how notoriously difficult it is to record mbira. In lieu of this, perhaps a decent modal approximation will be with respect to the harmonic series, such that frequencies of 2, 3, and 4 times the fundamental are present in the oscillations of a single tine, at exponentially smaller amplitudes. For instance, $M = \set{1.0, 2.0, 3.0, 4.00} \land A = \set{1.0, 0.5, 0.25, 0.125}$, where $M$ is a set of modes and $A$ is a set of amplitudes scalars that operate on the displacement, $\Delta x$.
