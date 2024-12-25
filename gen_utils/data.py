from typing import Literal
import numpy as np
from .types import Float1D, Float2D

from scipy.integrate import solve_ivp

def lorenz_ode(t: float, input: Literal[3], params: Literal[3]) -> Literal[3]:
    x, y, z = input
    sigma, rho, beta = params
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return np.array([x_dot, y_dot, z_dot])


def generate_lorenz_data(
    t_lin: Float1D, initial_cond: Float1D, ode_method: str = "LSODA"
) -> Float2D:
    sigma = 10
    rho = 28
    beta = 8 / 3

    def chaotic_lorenz(t, input):
        return lorenz_ode(t, input, params=(sigma, rho, beta))

    return solve_ivp(
        fun=chaotic_lorenz,
        t_span=[t_lin[0], t_lin[-1]],
        y0=initial_cond,
        t_eval=t_lin,
        method=ode_method,
    )