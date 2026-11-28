# Lotka–Volterra Predator–Prey Model

A Python simulation of the Lotka–Volterra equations, the classic model of two interacting species: one predator, one prey.

## The model

The Lotka–Volterra equations are a pair of first-order, nonlinear differential equations. They are often used to describe biological systems in which one species hunts another. The two populations change over time according to:

$$
\frac{dx}{dt} = \alpha x - \beta x y
$$

$$
\frac{dy}{dt} = \delta x y - \gamma y
$$

where

| Symbol | Meaning |
|---|---|
| $x$ | Prey population density (e.g. rabbits per km²) |
| $y$ | Predator population density (e.g. foxes per km²) |
| $t$ | Time |
| $dx/dt$, $dy/dt$ | Instantaneous growth rates of the two populations |
| $\alpha$ | Maximum per-capita growth rate of the prey |
| $\beta$ | Effect of predators on the prey death rate |
| $\gamma$ | Per-capita death rate of the predators |
| $\delta$ | Effect of prey on the predator growth rate |

All parameters are positive real numbers.

### What to expect

- **Without predators** ($y = 0$), prey grow exponentially at rate $\alpha$.
- **Without prey** ($x = 0$), predators die out exponentially at rate $\gamma$.
- **With both**, the populations oscillate. Prey grow, predators feed and multiply, prey decline, predators starve, and the cycle repeats. Predator peaks lag behind prey peaks.
- **Equilibrium:** the populations stay constant at $x^* = \gamma / \delta$ and $y^* = \alpha / \beta$. Any other starting point traces a closed orbit around this equilibrium in the phase plane.

For the maths behind these results (equilibria, stability, the conserved quantity and the oscillation period), see [docs/theory.md](docs/theory.md).

### Key assumptions and limits

- **Assumptions:** unlimited food for the prey, a constant environment, and interaction rates proportional to both populations. [[1](https://sail.usc.edu/~lgoldste/ArtPhon/Slides/lotka-volterramodel.pdf), [2](https://www.sciencedirect.com/science/article/pii/S2352914817301879)]
- **Limitations:** ignores carrying capacity, spatial structure and realistic extinction thresholds. Later extensions add carrying capacity (such as Rosenzweig–MacArthur models), fear effects or Allee effects. [[1](https://arxiv.org/html/2501.16860v1), [2](https://kkms.org/index.php/kjm/article/view/1694), [3](https://www.slideshare.net/slideshow/lotka-volterra-model-157062109/157062109), [4](https://sail.usc.edu/~lgoldste/ArtPhon/Slides/lotka-volterramodel.pdf)]

## What it does

- Defines the Lotka–Volterra system as a Python function
- Solves it numerically with `scipy.integrate.solve_ivp`
- Plots both populations over time
- Plots the phase portrait (predators vs. prey)
- Saves each run to `results/`, with every parameter and initial condition in the file name

## Project structure

```
PredatorPrey/
├── src/
│   ├── model.py        # entry point: sets parameters, runs the solver, plots and saves
│   ├── solver.py       # the equations and the solve() wrapper around solve_ivp
│   ├── vis.py          # plot_results(): time series and phase portrait
│   └── utils.py        # make_filename(): builds result file names from the run settings
├── tests/              # unit tests (pytest)
├── results/            # saved plots (generated, not tracked by git)
├── docs/
│   ├── theory.md       # equilibria, stability, conserved quantity, period
│   └── architecture.md # how the modules fit together and how to extend them
├── pyproject.toml      # project metadata and dependencies
├── uv.lock             # locked dependency versions
└── README.md
```

## Quick start

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
git clone https://github.com/KosmicByte/PredatorPrey.git
cd PredatorPrey
uv sync                 # creates .venv and installs dependencies
uv run src/model.py     # runs the simulation, shows the plots and saves them to results/
uv run pytest           # runs the tests
```

### Changing the parameters

Edit the conditions in `src/model.py`:

```python
params = {"alpha": 1, "beta": 0.1, "delta": 0.075, "gamma": 1.5}
initial_state = [10, 5]           # initial prey, initial predators
t_span = (0, 50)                  # start and end time
```

### Output

Each run saves a PNG to `results/`. The file name records every setting, so different runs never overwrite each other:

```
results/lv_a1_b0.1_d0.075_g1.5_x10_y5_t50.png
          α   β     δ      γ    x₀  y₀  t_end
```

The `results/` folder is listed in `.gitignore`. It is created automatically on the first run.

## Dependencies

- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)
- [Matplotlib](https://matplotlib.org/)
- [pytest](https://docs.pytest.org/) (dev)

## References

- Lotka, A. J. (1925). *Elements of Physical Biology*. Williams & Wilkins.
- Volterra, V. (1926). Fluctuations in the abundance of a species considered mathematically. *Nature*, 118, 558–560.
- [Lotka–Volterra equations, Wikipedia](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)
