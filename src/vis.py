import matplotlib.pyplot as plt


# Define plotting function to be called in model.py
def plot_results(t, x, y, params, initial_state, t_span, save_path=None, dpi=150):
    a,b,d,g = params["alpha"], params["beta"], params["delta"], params["gamma"]


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
             f"α={a}, β={b}\nδ={d}, γ={g}\n"
             f"x₀={initial_state[0]}, y₀={initial_state[1]}\nt∈{t_span}",
             transform=ax2.transAxes, ha="right", va="bottom", fontsize=9,
             bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

    if save_path:
        fig.savefig(save_path, dpi=150)
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
