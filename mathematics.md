# The General Idea

An mbira is an instrument made of a set of metal tines that are fixed at one end and free to vibrate. The sound space of an mbira is approximated by a set of frequencies, defined by a linear distribution of dampened sinusoids that depend on a length, sum of forces, and initial displacement.

## The Differential Equation

The forces that act on an mbira tine in motion are determined to be Newton’s second law, a damping force, and a restoring force. External forces are assumed to be negligible, which therefore gives that $m\frac{d^2x}{dt^2} +b\frac{dx}{dt} +kx = 0$ with the variables defined as follows.

### Time *t*

Time, as measured discretely by a sample rate.

### Displacement *x*

How far the tine is displaced from equilibrium at $x=0$ (measured in mm). The resultant amplitude is dependent on the initial $∆x$.

### Mass *m = VD*

Mass, $m$, as a product of volume $V = mm^3$ and density $D = \frac{g}{mm^3}$, relies on the assumption of constant tine width and depth. To assume a width $w = \frac{100}{15}mm$ and depth of $d = 1mm$, we can estimate the volume of a tine to be $lwd = l \frac{100}{15}mm^3$. The density $D$ of wrought iron is $D = 7750\frac{kg}{m^3} = 0.0075\frac{g}{mm^3}$[^1], so the mass in grams of a tine can be approximated as a function of length in mm: $m(l) = \frac{l}{20}$.

### Damping constant *b = 0.0003*[^2] 

### Spring constant *k*

The Shear Modulus, or Modulus of Rigidity, $G = Gpa = 10^6 \frac{N}{mm^2}$[^3], applies to this model. $G$ measures how much a material can flex before it shears, and online resources have determined iron to have a $G = 52.5Gpa = 52.5\*10^6 \frac{N}{mm^2}$[^3].

Online resources determine that $G = \frac{FL}{A∆x}$, where $F$ = force, $L$ = length, $A$ = cross-sectional area, and $∆x$ = transverse displacement. To solve for $F$ allows Hooke's Law to relate directly to $G$, such that $k$ is solved for. Thus $k = \frac{GA}{L}$. With $G = 52.5\*10^6 \frac{N}{mm^2}$ and $A = \frac{100}{15}mm^2$ under the simplified tine model, $k$ is reduced to a function of $l$ as $k(l) = -\frac{350,000,000}{l} \frac{N}{mm}$

## The General Solution to the Differential Equation

For $b^2 < 4mk$, the roots of the auxillary equation $mr^2 + br + k = 0$ are the two complex conjugates $\alpha ± i\beta = \frac{-b}{2m} ± i\frac{\sqrt{b^2 - 4mk}}{2m}$. It holds, then, that $\alpha = \frac{-b}{2m}$ and $\beta = \frac{\sqrt{4mk - b^2}}{2m}$.

It follows that the general solution to the DE is $x(t) = Ae^{αt}sin(βt)$, where $Ae^{αt} = Ae^{\frac{-b}{2m}t}$ is a product of the amplitude and damping factor.

If the above statements are relevant and true, then the solution only applies to a single tine. This approximation may need to be extended to account for multiple tines being played together.

## An initial calculation

For $l = 128$, it is determined that $m(128) = 6.4$ and $k(128) = 2,734,375$.

$4m(128)k(128) ≈ 70,000,000$, which is much larger than $b^2 = 0.0003^2 = 0.00000009$ which confirms a negative discriminant and complex root.

$\alpha_1 = \frac{-b}{2m} = \frac{-0.0003}{2m(128)} = -0.0000234375$

$\beta_1 = \frac{\sqrt{4mk - b^2}}{2m} ≈ \frac{\sqrt{70,000,000}}{12.8} ≈ 653.64$

The sine factor has a period of $T = \frac{2\pi}{\beta} = 0.0096126$ and it follows that the frequency $f = \frac{1}{T} ≈ 104.03 Hz$

This is a relatively accurate estimation. Next, to see if $f(\frac{l}{2})$ will approximate $2f(l)$:

$4m(64)k(64) ≈ 70,000,000$. What is surprisingly obvious with hindsight is that the dependency on length is eliminated for this term.

$\alpha_2 = -0.000046875$ and $\beta_2 = 1,307.28$ so $T = 0.00011734$ thus $f ≈ 208.015 Hz$

So it is the case that the octave relationship holds between tines of length $l$ and $2l$.

## An aside on assumptions

A nontrivial approximation might account for the fan-shaped tine with the definition of the cross-sectional area as $\int_{0}^{L}f(l)dl$, where $f(l)$ is a function that determines the cross-sectional area of a slice of the tine as defined by a curved shape in 3 dimensional space. That being said, such a consideration is well out-of-scope for the moment and possibly incorrect.

[^1]: Material Densities, https://spectro.in/Densities-of-Materials.html
[^2]: Damping Constants, https://help.solidworks.com/2016/english/solidworks/cworks/r_viscous_damping_ratios.htm
[^3]: Modulus of Rigidity & some values https://sciencenotes.org/shear-modulus-formula-and-definition/
