import data_store

def test_store_and_retrieve_data():
    data_store.data_records.clear()
    sample_data = {'temperature': 25, 'humidity': 55, 'pressure': 1000}
    data_store.store_data(sample_data)
    stored = data_store.get_all_data()
    assert len(stored) == 1
    assert stored[0]['temperature'] == 25
    assert stored[0]['humidity'] == 55
    assert stored[0]['pressure'] == 1000