import sensor

def test_collect_temperature_accuracy():
    data = sensor.collect_data()
    assert -10 <= data['temperature'] <= 40, "Temperature out of expected range"