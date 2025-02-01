import math
import pytest


from main import assignment_1

def test_fixed_point_iteration():
    tol = 1e-6
    p0 = 1.5
    result = assignment_1.fixed_point_iteration(p0, tol, max_iter=100)
    expected = math.sqrt(2)
    assert math.isclose(result, expected, rel_tol=tol), f"Expected {expected}, got {result}"

def test_bisection():
    tol = 1e-6
    left = 1
    right = 2
    result = assignment_1.bisection(left, right, tol)
    expected = math.sqrt(2)
    assert math.isclose(result, expected, rel_tol=tol), f"Expected {expected}, got {result}"

def test_newton_raphson():
    tol = 1e-6
    p0 = 1.0
    result = assignment_1.newton_raphson(p0, tol, max_iter=100)
    expected = 0.7390851332151607  # approximate root of cos(x) - x = 0
    assert math.isclose(result, expected, rel_tol=tol), f"Expected {expected}, got {result}"

def test_approximation_method(capsys):
    tol = 1e-6
    x0 = 1.5
    assignment_1.approximation_method(x0, tol)
    captured = capsys.readouterr().out
    assert "Convergence after" in captured, "The convergence message was not found in the output"
