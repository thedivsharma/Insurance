import mysql.connector
import json
from insurance_claim.llm.properties import MYSQL_CONFIG, get_field_properties

def insert_into_mysql(data: dict):
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()

        # basically getting fields from schema
        field_props = get_field_properties()
        field_names = list(field_props.keys())

        # adjusting column names to match the field
        column_names = [field.lower().replace(" ", "_") for field in field_names]
        placeholders = ', '.join(['%s'] * len(field_names))
        columns = ', '.join(column_names)

        values = [data.get(field) for field in field_names]

        # here you add raw_json column separately
        columns += ", raw_json"
        placeholders += ", %s"
        values.append(json.dumps(data))

        # the final query
        query = f"""
        INSERT INTO claims ({columns})
        VALUES ({placeholders})
        """
        cursor.execute(query, values)
        conn.commit()

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
