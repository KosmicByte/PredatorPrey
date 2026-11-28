# Math reference

Background maths for the Lotka–Volterra model in this repo. The equations and symbols are defined in the [README](../README.md#the-model).

$$
\frac{dx}{dt} = \alpha x - \beta x y, \qquad
\frac{dy}{dt} = \delta x y - \gamma y
$$

## 1. Equilibria

Set both derivatives to zero:

$$
x(\alpha - \beta y) = 0, \qquad y(\delta x - \gamma) = 0
$$

This gives two fixed points:

| Point | Coordinates | Meaning |
|---|---|---|
| Extinction | $(0,\ 0)$ | Both species absent |
| Coexistence | $\left(\dfrac{\gamma}{\delta},\ \dfrac{\alpha}{\beta}\right)$ | Populations hold steady |

With the default parameters ($\alpha = 1$, $\beta = 0.1$, $\delta = 0.075$, $\gamma = 1.5$), the coexistence point is $(x^*, y^*) = (20,\ 10)$.

The prey equilibrium depends only on the **predator** parameters ($\gamma / \delta$), and the predator equilibrium depends only on the **prey** parameters ($\alpha / \beta$).

## 2. Stability (linearisation)

The Jacobian of the system is

$$
J(x, y) =
\begin{pmatrix}
\alpha - \beta y & -\beta x \\
\delta y & \delta x - \gamma
\end{pmatrix}
$$

**At the origin:**

$$
J(0, 0) =
\begin{pmatrix}
\alpha & 0 \\
0 & -\gamma
\end{pmatrix}
$$

The eigenvalues are $\alpha > 0$ and $-\gamma < 0$, so the origin is a **saddle point**. A small prey population grows away from it, and a predator-only population decays towards it. Joint extinction is unstable.

**At the coexistence point:**

$$
J\left(\tfrac{\gamma}{\delta}, \tfrac{\alpha}{\beta}\right) =
\begin{pmatrix}
0 & -\dfrac{\beta\gamma}{\delta} \\
\dfrac{\alpha\delta}{\beta} & 0
\end{pmatrix}
$$

The eigenvalues are purely imaginary, $\lambda = \pm i\sqrt{\alpha\gamma}$. Linearisation alone cannot decide stability here. The conserved quantity below shows the point is a **centre**: nearby trajectories circle it forever, neither spiralling in nor out.

## 3. Conserved quantity

Dividing the two equations and separating variables gives a function that stays constant along every trajectory:

$$
V(x, y) = \delta x - \gamma \ln x + \beta y - \alpha \ln y
$$

You can check this by differentiating:

$$
\frac{dV}{dt} = \left(\delta - \frac{\gamma}{x}\right)\dot{x} + \left(\beta - \frac{\alpha}{y}\right)\dot{y} = 0
$$

Consequences:

- Each starting point lies on one level curve of $V$, and the trajectory stays on that curve. This is why the phase portrait shows **closed orbits** instead of spirals.
- $V$ has its minimum at the coexistence point, so orbits further from the equilibrium correspond to larger values of $V$.
- The model has no damping. A perturbation never dies out; it just moves the system onto a different orbit.

## 4. Period of oscillation

For orbits close to the equilibrium, the populations oscillate with angular frequency $\sqrt{\alpha\gamma}$. The period is therefore

$$
T \approx \frac{2\pi}{\sqrt{\alpha\gamma}}
$$

With the default parameters, $T \approx 2\pi / \sqrt{1.5} \approx 5.13$ time units. Larger orbits, further from the equilibrium, take longer to complete.

## 5. Time averages

Over one full cycle, the average populations equal the equilibrium values, whatever the starting point:

$$
\bar{x} = \frac{\gamma}{\delta}, \qquad \bar{y} = \frac{\alpha}{\beta}
$$

To see this, divide the prey equation by $x$ and integrate over one period $T$. The left side, $\ln x(T) - \ln x(0)$, is zero because the orbit is closed. That leaves $\alpha T - \beta \int_0^T y\,dt = 0$. The predator equation gives the matching result for $\bar{x}$.

## 6. Numerical notes

- The code uses `solve_ivp` with its default method (RK45) and `max_step=0.05`. RK45 does not preserve $V$ exactly, so over very long runs the orbit can drift slowly outward or inward. A smaller `max_step`, tighter `rtol`/`atol`, or a symplectic-style integrator reduces this.
- Tracking $V(x(t), y(t))$ over a run is a simple accuracy check. Its relative change should stay small. This also makes a good unit test.
- Populations are continuous, so they can get extremely close to zero without ever reaching it. Real populations would go extinct at that point, which is one of the model's limitations.
