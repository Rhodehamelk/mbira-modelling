# The General Idea

An mbira is approximated by a set of frequencies, defined by a linear distribution of dampened sinusoids that depend on a length, sum of forces, and initial displacement. Each fundamental frequency corresponds to a tine of a length and material (assumed to be wrought iron).

## The Differential Equation

The forces that act on an mbira tine in motion are determined to be Newton’s second law, a damping force, and a restoring force. External forces are assumed to be negligible, which therefore gives that $m\frac{d^2x}{dt^2} +b\frac{dx}{dt} +kx = 0$ with the variables defined as follows.

### Displacement *x*

How far the tine is displaced from it's equilibrium position at $x=0$. This variable controls the amplitude of the resultant oscillation.

### Mass *m = VD*

Mass, $m$ as a product of volume $V$ and density $d$, relies on the assumption of constant tine width and depth. To assume a width $w = \frac{1}{150}m$ and depth of $d = \frac{1}{600}m$, we can estimate the volume of a tine to be $lwd = l \frac{1}{90000}m^3$. Wrought iron has a density $D = 7750\frac{kg}{m^3}$[^1], so the mass in kilograms of a tine can be approximated as a function of length: $m(l) = l\frac{31}{360}$.

### Damping constant *b = 0.0003*[^2] 

### Spring constant *k*

The Young’s Modulus $Y$ of a material predicts the elongation or compression of a material before its elastic limit is reached[^3]. Young's Modulus gives that $F = \frac{YA∆x}{L}$ for $Y$, $A$ = cross sectional area, $∆x$ = displacement, and $L$ = length. Hooke’s Law states that $F = -k∆x$ for	$k$ = spring constant, and	$∆x$ = displacement.

To set Young’s modulus equal to Hooke’s Law and solve for $k$ gives that $k = \frac{YA}{L}$

$A = wd = \frac{1}{90000}$ under the assumption of a simple tine, and for a $Y ≈ 200$[^4], $k$ is approximated as a function of $l$: $k(l) = \frac{1}{450l}$

## The Solution

For $b^2 < 4mk$, the root of the auxillary equation $mr^2 + br + k = 0$ is the complex value $\frac{-b}{2m} ± i\frac{\sqrt{b^2 - 4mk}}{2m} = α ± iβ$.

In this case, the general solution is $x(t) = Ae^{αt}sin(βt+ø)$, where $Ae^{αt} = Ae^{\frac{-b}{2m}t}$ is the damping factor

## An aside on assumptions

$A$ is assumed to be the area of a simple rectangle of constant width and depth in this initial approximation. Thereby $k$ is reduced to a function of $l$ alone. However, a nontrivial approximation might account for the fan-shaped tine by approximating the cross-sectional area as $A = \int_{0}^{L}f(l)dl$, where $f(l)$ is a function that determines the cross-sectional area of a slice of the tine as defined by a curved shape in 3 dimensional space. That being said, such a consideration is well out-of-scope for the moment and possibly incorrect.

[^1]: Material Densities, https://spectro.in/Densities-of-Materials.html
[^2]: Damping Constants, https://help.solidworks.com/2016/english/solidworks/cworks/r_viscous_damping_ratios.htm
[^3]: Hooke's Law and Young's Modulus, http://labman.phys.utk.edu/phys221core/modules/m3/Hooke%27s%20law.html
[^4]: Values of Young's Modulus, https://www.engineeringtoolbox.com/young-modulus-d_417.html
