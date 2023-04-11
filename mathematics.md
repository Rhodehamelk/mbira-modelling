# The General Idea

An mbira is an instrument made of a set of metal tines that are fixed at one end and free to vibrate. The sound space of an mbira is approximated by a set of frequencies, defined by a linear distribution of dampened sinusoids that depend on a length, sum of forces, and initial displacement.

## The Differential Equation

The forces that act on an mbira tine in motion are determined to be Newton’s second law, a damping force, and a restoring force. External forces are assumed to be negligible, which therefore gives that $m\frac{d^2x}{dt^2} +b\frac{dx}{dt} +kx = 0$ with the variables defined as follows.

### Time *t*

Time, as measured discretely by a sample rate.

### Displacement *x*

How far the tine is displaced from equilibrium at $x=0$ (measured in mm). The resultant amplitude is dependent on the initial $∆x$.

### Mass *m = VD*

Mass, $m$, as a product of volume $V = mm^3$ and density $D = \frac{g}{mm^3}$, relies on the assumption of constant tine width and depth. To assume a width $w = \frac{100}{15}mm$ and depth of $d = \frac{10}{6}mm$, we can estimate the volume of a tine to be $lwd = l \frac{100}{9}mm^3$. The density $D$ of wrought iron is $D = 7750\frac{kg}{m^3} = 0.0075\frac{g}{mm^3}$[^1], so the mass in grams of a tine can be approximated as a function of length in mm: $m(l) = l\frac{31}{360}$.

### Damping constant *b = 0.0003*[^2] 

### Spring constant *k*

The Shear Modulus, or Modulus of Rigidity, $G = Gpa = 10^6 \frac{N}{mm^2}$[^3], applies to this model. $G$ measures how much a material can flex before it shears, and online resources have determined iron to have a $G = 52.5Gpa = 52.5\*10^6 \frac{N}{mm^2}$[^3].

Online resources determine that $G = \frac{FL}{A∆x}$, where $F$ = force, $L$ = length, $A$ = cross-sectional area, and $∆x$ = transverse displacement. To solve for $F$ allows Hooke's Law to relate directly to $G$, such that $k$ is solved for. Thus $k = \frac{GA}{L}$. With $G = 52.5\*10^6 \frac{N}{mm^2}$ and $A = \frac{100}{9}mm^2$ under the simplified tine model, $k$ is reduced to a function of $l$ as $k(l) = -\frac{583,333,333}{l} \frac{N}{mm}$

## The General Solution to the Differential Equation

For $b^2 < 4mk$, the roots of the auxillary equation $mr^2 + br + k = 0$ are the two complex conjugates $\alpha ± i\beta = \frac{-b}{2m} ± i\frac{\sqrt{b^2 - 4mk}}{2m}$. It holds, then, that $\alpha = \frac{-b}{2m}$ and $\beta = \frac{\sqrt{4mk - b^2}}{2m}$.

It follows that the general solution to the DE is $x(t) = Ae^{αt}sin(βt)$, where $Ae^{αt} = Ae^{\frac{-b}{2m}t}$ is a product of the amplitude and damping factor.

If the above statements are relevant and true, then the solution only applies to a single tine. This approximation may need to be extended to account for multiple tines being played together.

## An initial calculation

For $l = 128$, it is determined that $m(128) = 1,486$ and $k(128) = 4,557,291$.

$4m(128)k(128)$ ≈ 27 billion, which is much larger than $b^2 = 0.0003^2 = 0.00000009$ which confirms a negative discriminant and complex root.

$\alpha = \frac{-b}{2m} = \frac{-0.0003}{2m(128)} = -0.000000100911458$

$\beta = \frac{\sqrt{4mk - b^2}}{2m} ≈ \frac{\sqrt{27,088,537,704}}{2972} ≈ 9,114,528$

The sine factor has a period of $T = \frac{2\pi}{\beta} ≈ 0.000000689355298$ and it follows that the frequency $f = \frac{1}{T} = 1,450,630 Hz

This seems waaaaay too high and leads me to believe that there is an inaccuracy.


## An aside on assumptions

A nontrivial approximation might account for the fan-shaped tine with the definition of the cross-sectional area as $\int_{0}^{L}f(l)dl$, where $f(l)$ is a function that determines the cross-sectional area of a slice of the tine as defined by a curved shape in 3 dimensional space. That being said, such a consideration is well out-of-scope for the moment and possibly incorrect.

[^1]: Material Densities, https://spectro.in/Densities-of-Materials.html
[^2]: Damping Constants, https://help.solidworks.com/2016/english/solidworks/cworks/r_viscous_damping_ratios.htm
[^3]: Modulus of Rigidity & some values https://sciencenotes.org/shear-modulus-formula-and-definition/
