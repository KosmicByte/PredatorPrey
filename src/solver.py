from scipy.integrate import solve_ivp


# define the LVPP function & pass the params

def predatorprey(t, state, alpha=1, beta=0.1, delta=0.075, gamma=1.5):
    x, y = state
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return dxdt, dydt


# solve by using solve_ivp - Initial Value problem

def solve(params, initial_state, t_span, max_step=0.05):
    sol = solve_ivp(
        predatorprey,
        t_span,
        initial_state,
        args=(params["alpha"], params["beta"], params["delta"], params["gamma"]),
        dense_output=True,
        max_step=max_step
    )
    # results
    x, y = sol.y  # x = prey, y = predators
    t = sol.t
    return t, x, y
