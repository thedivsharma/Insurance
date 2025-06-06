def get_field_properties() -> dict:
    return {
        "Patient Name": {"type": "string"},
        "Hospital Name": {"type": "string"},
        "Admission Date": {"type": "string", "format": "date"},
        "Discharge Date": {"type": "string", "format": "date"},
        "Diagnosis": {"type": "string"},
        "Total Amount": {"type": "number"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1}
    }

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "thedivsharma",
    "password": "div@1704",
    "database": "insurance_data"
}