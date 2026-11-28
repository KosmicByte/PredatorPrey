# Code architecture

How the code in `src/` is organised and how the pieces fit together.

## Modules

| File | Responsibility | Depends on |
|---|---|---|
| `model.py` | Entry point. Holds the run settings, calls the solver and the plotter, decides where results go | `solver`, `vis`, `utils` |
| `solver.py` | The maths: the right-hand side of the ODEs and a `solve()` wrapper | SciPy |
| `vis.py` | Plotting only: time series and phase portrait, optional saving | Matplotlib |
| `utils.py` | Small helpers, currently the result file name builder | — |

Each module has one job. `solver.py` knows nothing about plotting, and `vis.py` knows nothing about how the data was produced. This makes it easy to swap either side, for example to try a different integrator or add a new plot.

## Data flow

```
model.py
  │  params, initial_state, t_span
  ▼
solver.solve()  ──►  t, x, y  (NumPy arrays)
  │
  ▼
utils.make_filename()  ──►  "lv_a1_b0.1_d0.075_g1.5_x10_y5_t50.png"
  │
  ▼
vis.plot_results()  ──►  figure on screen + PNG in results/
```

## Functions

### `solver.predatorprey(t, state, alpha, beta, delta, gamma)`

The right-hand side of the system, in the form `solve_ivp` expects. Returns `(dx/dt, dy/dt)`. `t` is unused because the system is autonomous, but `solve_ivp` always passes it.

### `solver.solve(params, initial_state, t_span, max_step=0.05)`

Runs `solve_ivp` and returns `(t, x, y)`.

- `params`: dict with keys `"alpha"`, `"beta"`, `"delta"`, `"gamma"`. The values are passed to `predatorprey` through `args=`, so the dict is the single source of truth for each run.
- `max_step`: largest step the integrator may take. Smaller values give smoother, more accurate orbits at the cost of run time.

### `vis.plot_results(t, x, y, params, initial_state, t_span, save_path=None, dpi=150)`

Draws two side-by-side panels:

1. Prey and predator populations against time
2. Phase portrait (predators against prey), with the starting point marked and the run settings in a text box

If `save_path` is given, the figure is saved there at the given `dpi` before being shown.

### `utils.make_filename(params, initial_state, t_span, prefix="lv", ext="png")`

Builds a file name from the run settings, in this order: each parameter (first letter + value), then `x₀`, `y₀` and the end time. Numbers are formatted with `:g`, so `1.0` becomes `1`.

Parameters are labelled by their first letter. If you add a parameter whose name starts with the same letter as an existing one, switch to an explicit label mapping to avoid ambiguous names.

## Paths

`model.py` locates `results/` relative to its own file:

```python
RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)
```

This works regardless of the working directory, whether the script is run from the project root, from `src/`, or from the IDE.

## Extending

- **Parameter sweep:** loop over values in `model.py` and call `solve()` and `plot_results()` once per value. The file names keep each run separate.
- **New model:** for example a Lotka–Volterra variant with carrying capacity. Add a new right-hand-side function in `solver.py` (or a new solver module). `vis.py` and `utils.py` can be reused unchanged as long as the solver still returns `t, x, y`.
- **Tests:** test `solver.py` directly, without plotting. Useful checks are that the equilibrium point stays fixed, and that the conserved quantity $V$ (see [theory.md](theory.md#3-conserved-quantity)) barely changes over a run.
