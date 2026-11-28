from pathlib import Path
from solver import solve
from vis import plot_results
from utils import make_filename

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)
# set initial conditions

params = {"alpha": 100, "beta": 2, "delta": 0.75, "gamma": 3.5}
# Define the time range over which we want to simulate the system.
# t_span = (start_time, end_time), so we simulate from t = 0 to t = 50
initial_state = [20,5]
t_span = (0,100)

if __name__ == "__main__":
    t, x, y = solve(params, initial_state, t_span)

    filename = make_filename(params, initial_state, t_span)
    plot_results(t, x, y, params, initial_state, t_span,
                 save_path=RESULTS_DIR / filename)