import numpy as np

# N_t er en mindre enn totalt antall punkter

def differentiate(u, dt):
    N_t = len(u) - 1
    deriv = np.zeros(N_t + 1)
    for n in range(1, N_t):
        deriv[n] = (u[n + 1] - u[n - 1]) / (2 * dt)
    deriv[0] = (u[1] - u[0]) / dt
    deriv[N_t] = (u[N_t] - u[N_t - 1]) / dt
    return deriv

def differentiate_vector(u, dt):
    N_t = len(u) - 1
    deriv = np.zeros(N_t + 1)
    deriv[1:N_t] = (1 / (2 * dt)) * (u[2:N_t + 1] - u[0:N_t - 1])
    deriv[0] = (u[1] - u[0]) / dt
    deriv[N_t] = (u[N_t] - u[N_t - 1]) / dt
    return deriv

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    