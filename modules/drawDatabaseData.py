import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict, List


# def draw_database_data(category_property, value_property, operation_type, query_records):
def draw_database_data(category_property: str, value_property: str, operation_type: str,
                       query_records: List[Dict]) -> None:
    # if not isinstance(record, dict):
    #     print("Non-dictionary record found:", record)
    #     continue  # Skip non-dictionary records

    filter_records = [record for record in query_records if record['operation_type'].lower() == operation_type.lower()]

    category_values = {}
    for record in filter_records:
        # the category property we are interested in eg class.
        category = record[category_property]
        # Convert value to the appropriate numeric type based on the value_property
        if value_property == 'calls':
            value = int(record[value_property])  # Convert to int if dealing with calls
        elif value_property == 'total_time':
            value = float(record[value_property])  # Convert to float if dealing with total_time
        else:
            continue  # Skip if value_property is neither 'calls' nor 'total_time'

        # Sum the values in the category
        if category in category_values:
            category_values[category] += value
        else:
            category_values[category] = value

    labels = list(category_values.keys())
    values = list(category_values.values())
    plt.tight_layout()
    plt.figure(figsize=(10, 8))
    #plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Plot of " + operation_type + " vs " + value_property)
    plt.show()
