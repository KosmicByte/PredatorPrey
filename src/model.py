import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt



# define the LVPP function & pass the params

def  predatorprey(t, state, alpha = 1, beta= 0.1, delta= 0.075, gamma= 1.5):
    x,y = state
    dxdt = alpha * x - beta*x*y
    dydt = delta * x * y - gamma * y
    return dxdt, dydt

# set initial conditions

alpha, beta, delta, gamma = 1, 0.1, 0.075, 1.5
# Define the time range over which we want to simulate the system.
# t_span = (start_time, end_time), so we simulate from t = 0 to t = 50
t_span = (0,50)
initial_state = [10,5]

# solve

sol = solve_ivp(predatorprey, t_span, initial_state, dense_output=True, max_step=0.05)

# results
x, y = sol.y      # x = prey, y = predators
t = sol.t


# Text describing the run
conditions = (
    f"α = {alpha}, β = {beta}, δ = {delta}, γ = {gamma}   |   "
    f"x₀ = {initial_state[0]}, y₀ = {initial_state[1]}   |   "
    f"t = {t_span[0]}–{t_span[1]}"
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5), layout="constrained")

# Left: populations over time
ax1.plot(t, x, label="Prey", color="tab:blue")
ax1.plot(t, y, label="Predators", color="tab:red")
ax1.set_title("Populations over time")
ax1.set_xlabel("Time")
ax1.set_ylabel("Population")
ax1.legend()

# Right: phase portrait (predators vs prey)
ax2.plot(x, y, lw=0.8, color="tab:purple")
ax2.plot(x[0], y[0], "o", color="black", label=f"Start ({x[0]:g}, {y[0]:g})")
ax2.set_title("Phase portrait")
ax2.set_xlabel("Prey (x)")
ax2.set_ylabel("Predators (y)")
ax2.legend()

fig.suptitle("Lotka–Volterra Predator–Prey Model")
ax2.text(0.98, 0.02,
         f"α={alpha}, β={beta}\nδ={delta}, γ={gamma}\n"
         f"x₀={initial_state[0]}, y₀={initial_state[1]}\nt∈{t_span}",
         transform=ax2.transAxes, ha="right", va="bottom", fontsize=9,
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

##plt.savefig(f"src/tests/lv_a{alpha}_g{gamma}_x{initial_state[0]}.png", dpi=150)
plt.show()


'''
# plotting the model

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left: populations over time
ax1.plot(t, x, label="Prey", color="tab:blue")
ax1.plot(t, y, label="Predators", color="tab:red")
ax1.set_title("Populations over time")
ax1.set_xlabel("Time")
ax1.set_ylabel("Population")
ax1.legend()

# Right: phase portrait (predators vs prey)
ax2.plot(x, y, lw=0.8, color="tab:purple")
ax2.plot(x[0], y[0], "o", color="black", label="Start")
ax2.set_title("Phase portrait")
ax2.set_xlabel("Prey (x)")
ax2.set_ylabel("Predators (y)")
ax2.legend()

fig.suptitle("Lotka–Volterra Predator–Prey Model")
plt.tight_layout()
plt.show()
'''

