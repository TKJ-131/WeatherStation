import data_store

def test_temperature_alert():
    data_store.data_records.clear()
    data_store.store_data({'temperature': 41, 'humidity': 60, 'pressure': 1002})
    assert data_store.check_alert() == True