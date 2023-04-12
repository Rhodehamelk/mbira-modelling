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

For some $F$ = force, $l$ = length, $\sigma$ = cross-sectional area, and $∆x$ = transverse displacement, the Shear Modulus of Rigidity, $G = \frac{lF}{\sigma∆x}$, determines the rigidity of a metal tine subject to transverse forces. It was determined that iron has a $G = 52.5Gpa = 52.5\*10^6 \frac{N}{mm^2}$[^3].

To isolate $F = \frac{\sigma∆xG}{l}$ allows Hooke's Law, $F = -k∆x$, to relate directly to $G$, such that $-k∆x = \frac{G∆x\sigma}{l}$. Thus $k = \frac{G\sigma}{l}$ (but why does the negative disappear?). With $G = 52.5\*10^6 \frac{N}{mm^2}$ and $\sigma = \frac{100}{15}mm^2$ under the simplified tine model, $k$ is reduced to a function of $l$ as $k(l) = \frac{350,000,000}{l} \frac{N}{mm}$

## The General Solution to the Differential Equation

For $b^2 < 4mk$, the roots of the auxillary equation $mr^2 + br + k = 0$ are the two complex conjugates $\alpha ± i\beta = \frac{-b}{2m} ± i\frac{\sqrt{4mk - b^2}}{2m}$.[^4] 

It follows that the general solution to the DE is $x(t) = Ae^{αt}sin(βt)$, where $Ae^{αt} = Ae^{\frac{-b}{2m}t}$ is a product of the amplitude and damping factor.

## The preservation of the octave

Let $l_1 = 128 \Rightarrow m(l_1) = 6.4 \land k(l_1) = 2,734,375$

$\Rightarrow \alpha_1 = \frac{-b}{2m(l_1)} = \frac{-0.0003}{12.8} = -0.0000234375 \land \beta_1 = \frac{\sqrt{4m(l_1)k(l_1) - b^2}}{2m(l_1)} \approx \frac{\sqrt{70,000,000}}{12.8} \approx 653.64$

$\Rightarrow T_1 = \frac{2\pi}{\beta_1} = 0.0096126 \land f = \frac{1}{T} \Rightarrow f_1 \approx 104.03 Hz$, which is a precise approximation of the true pitch, if not necessarily accurate.

Let $l_2 = 64 \Rightarrow m(l_2) = 3.2 \land k(l_2) = 5,468,750$

$\Rightarrow \alpha_2 = \frac{-b}{2m(l_2)} = \frac{-0.0003}{6.4} = -0.000046875 \land \beta_1 = \frac{\sqrt{4m(l_2)k(l_2) - b^2}}{2m(l_2)} ≈ \frac{\sqrt{70,000,000}}{6.4} \approx 1,307.28$

$\Rightarrow T_2 = \frac{2\pi}{\beta_2} = 0.00011734 \land f = \frac{1}{T} \Rightarrow f_2 \approx 208.01 Hz$

$\therefore f(l_2) \approx  2f(l_1) \Rightarrow$ the octave relationship holds.

## An aside on assumptions

A nontrivial approximation might account for the fan-shaped tine with the definition of the cross-sectional area as $\int_{0}^{L}f(l)dl$, where $f(l)$ is a function that determines the cross-sectional area of a slice of the tine as defined by a curved shape in 3 dimensional space. That being said, such a consideration is well out-of-scope for the moment and possibly incorrect.

[^1]: Material Densities, https://spectro.in/Densities-of-Materials.html
[^2]: Damping Constants, https://help.solidworks.com/2016/english/solidworks/cworks/r_viscous_damping_ratios.htm
[^3]: Modulus of Rigidity & some values https://sciencenotes.org/shear-modulus-formula-and-definition/
[^4]: Observe that $4m(l)k(l) = 4\frac{l}{20}\frac{350,000,000}{l} = 70,000,000$ is independent of $l$, and also that, for small enough values of $b$, it's subtraction is negligible. Therefore the discriminant can be approximated as a constant.
