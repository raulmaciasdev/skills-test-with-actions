# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
# Asegúrate de que la estructura de carpetas sea /src y /tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

# --- TESTS PARA AREA_OF_CIRCLE ---

def test_area_of_circle_positive_radius():
    """Test con radio positivo. Usamos pytest.approx para evitar errores de precisión."""
    radius = 1
    result = area_of_circle(radius)
    # math.pi es más preciso que 3.14159, por eso usamos approx
    assert result == pytest.approx(3.1415926535, rel=1e-5)

def test_area_of_circle_zero_radius():
    """Test con radio cero."""
    assert area_of_circle(0) == 0

def test_area_of_circle_negative_radius():
    """CRITICO PARA COVERAGE: Test de excepción para radio negativo."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-1)

# --- TESTS PARA FIBONACCI ---

def test_get_nth_fibonacci_zero():
    """Test n=0."""
    assert get_nth_fibonacci(0) == 0

def test_get_nth_fibonacci_one():
    """Test n=1."""
    assert get_nth_fibonacci(1) == 1

def test_get_nth_fibonacci_ten():
    """Test n=10."""
    assert get_nth_fibonacci(10) == 55

def test_get_nth_fibonacci_negative():
    """CRITICO PARA COVERAGE: Test de excepción para n negativo."""
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-1)