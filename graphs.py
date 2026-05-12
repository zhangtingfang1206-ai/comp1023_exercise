import numpy as np
import matplotlib.pyplot as plt

def generate_heart_shape(num_points=200):
    """Generates a closed continuous curve (a heart) for testing."""
    t = np.linspace(0, 2*np.pi, num_points, endpoint=False)
    # Parametric equations for a heart
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

def compute_coefficients(z_points, max_order=200):
    """Computes exact complex Fourier coefficients analytically."""
    N = len(z_points) - 1 # z_0 is duplicated at the end as z_N
    c = {}
    
    # Calculate t_k values
    t_vals = np.array([2 * np.pi * k / N for k in range(N + 1)])
    
    # Pre-calculate differences (z_k - z_{k-1})
    dz = np.diff(z_points)
    
    for n in range(-max_order, max_order + 1):
        if n == 0:
            c[n] = np.mean(z_points[:-1])
        else:
            # Exact formula derived via integration by parts
            term1 = np.exp(-1j * n * t_vals[1:])
            term2 = np.exp(-1j * n * t_vals[:-1])
            summation = np.sum(dz * (term1 - term2))
            c[n] = -N / (4 * np.pi**2 * n**2) * summation
            
    return c

def evaluate_fourier_series(c, t_array, order):
    """Evaluates the Fourier partial sum S_N(t) for a given order."""
    S = np.zeros(len(t_array), dtype=complex)
    for n in range(-order, order + 1):
        S += c[n] * np.exp(1j * n * t_array)
    return S

# 1. Setup coordinates (Parts a & b)
x_coords, y_coords = generate_heart_shape(200)
# Close the curve by making z_N = z_0
z = np.append(x_coords + 1j * y_coords, x_coords[0] + 1j * y_coords[0])

# 2. Compute coefficients up to order 200 (Part c)
max_order = 200
coefficients = compute_coefficients(z, max_order)

# 3. Plotting the results (Part d)
t_plot = np.linspace(0, 2*np.pi, 1000)
orders_to_plot = [2, 5, 10, 50, 200]

plt.figure(figsize=(15, 10))

# Plot the original shape for reference
plt.subplot(2, 3, 1)
plt.plot(np.real(z), np.imag(z), 'k--', label="Original")
plt.title("Original Curve")
plt.axis('equal')
plt.legend()

# Plot parametric partial sums S_N(t)
for i, N_order in enumerate(orders_to_plot):
    plt.subplot(2, 3, i + 2)
    S_N = evaluate_fourier_series(coefficients, t_plot, N_order)
    
    x_t = np.real(S_N)
    y_t = np.imag(S_N)
    
    plt.plot(x_t, y_t, color='blue', label=f'S_{N_order}(t)')
    plt.title(f'Fourier Series: N = {N_order}')
    plt.axis('equal')
    plt.legend()

plt.tight_layout()
plt.show()