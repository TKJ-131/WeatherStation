import random

def collect_data():
    """Simulate collecting weather data."""
    return {
        'temperature': round(random.uniform(-10, 40), 2),
        'humidity': round(random.uniform(20, 100), 2),
        'pressure': round(random.uniform(950, 1050), 2)
    }