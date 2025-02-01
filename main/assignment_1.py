import math
# Initial parameters
x0 = 1.5
tol = 1e-6  # Tolerance for convergence

# Function for iterative approximation (Approximation Algorithm)
def approximation_method(x, tolerance):
    iteration = 0
    diff = x

    print(f"{iteration} : {x}")

    while diff >= tolerance:
        iteration += 1
        prev_x = x
        x = (x / 2) + (1 / x)  # Approximation formula
        print(f"{iteration} : {x}")
        diff = abs(x - prev_x)

    print(f"Convergence after {iteration} iterations")

# Function used for root-finding methods
def f(x):
    return x**2 - 2  # Function whose root is sqrt(2)

def h(x):
    return 0.5 * (x + 2 / x)  # Fixed-point iteration function

# Bisection method implementation
def bisection(left, right, tolerance):
    max_iter = 1000  # Limit iterations
    iteration = 0

    while abs(right - left) > tolerance and iteration < max_iter:
        iteration += 1
        midpoint = (left + right) / 2

        # Determine in which subinterval the sign change occurs
        if f(left) * f(midpoint) < 0:
            right = midpoint
        else:
            left = midpoint

    return (left + right) / 2  # Return final approximation

# Fixed-Point Iteration method
def fixed_point_iteration(p0, tolerance, max_iter):
    iteration = 1
    while iteration <= max_iter:
        p = h(p0)  # Apply iteration function
        if abs(p - p0) < tolerance:
            return p  # Convergence achieved
        p0 = p
        iteration += 1

    raise ValueError("Fixed-Point method did not converge")

# Newton-Raphson method for solving cos(x) - x = 0:
def g(x):
    return math.cos(x) - x

def gprime(x):
    return -math.sin(x) - 1

# Newton-Raphson method implementation
def newton_raphson(p0, tolerance, max_iter):
    iteration = 1
    while iteration <= max_iter:
        if gprime(p0) == 0:
            print("Derivative is zero, cannot proceed.")
            return None

        p1 = p0 - g(p0) / gprime(p0)  # Newton's formula

        if abs(p1 - p0) < tolerance:
            return p1  # Convergence achieved

        p0 = p1
        iteration += 1

    print("Newton-Raphson did not converge in given iterations.")
    return None

# Main execution block
if __name__ == '__main__':
    # Execute and print results for each method
    fp = fixed_point_iteration(1, tol, 100)
    print(f"Fixed-Point Iteration result: {fp}")

    bis = bisection(1, 2, tol)
    print(f"Bisection method result: {bis}")

    print("Approximation Algorithm:")
    approximation_method(x0, tol)

    root = newton_raphson(p0=1.0, tolerance=tol, max_iter=100)
    print(f"Newton-Raphson result: {root}")
