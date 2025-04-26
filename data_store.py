data_records = []

def store_data(data):
    """Store a data record."""
    data_records.append(data)

def get_all_data():
    """Retrieve all stored data."""
    return data_records

def get_average_temperature():
    """Calculate average temperature."""
    if not data_records:
        return None
    total_temp = sum(record['temperature'] for record in data_records)
    return round(total_temp / len(data_records), 2)

def check_alert():
    """Return True if any temperature > 40°C."""
    return any(record['temperature'] > 40 for record in data_records)