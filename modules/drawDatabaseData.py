import matplotlib.pyplot as plt
import numpy as np
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

    total = sum(category_values.values())

    # magnitude of items
    # create a bucket 5% of items to store
    # all the ones not worth optimizing.
    other_threadshold = total * .05

    other_value = 0
    main_categories = {}

    # the totals and the categories (eg the class)
    for category, value in category_values.items():
        if value < other_threadshold:
            other_value += value
        else:
            main_categories[category] = value

    if other_value > 0:
        main_categories['Other'] = other_value

    labels = list(main_categories.keys())
    values = list(main_categories.values())

    # Use legend to label slices, placed outside the chart
    # plt.legend(wedges, labels, title="Categories", loc="center left", bbox_to_anchor=(1, 0.5))

    # Improve legibility
    plt.setp(autotexts, size=8, weight="bold")


    explode = [0.1 if value < (sum(values) * 0.05) else 0 for value in values]
    plt.close('all')

    fig, ax = plt.subplots(figsize=(8, 11))
    colors = generate_pastel_colors(len(category_values))
    ax.axis('equal')  # Ensures the pie chart is circular
    ax.axis('off')  # This turns off the axis lines and labels
    plt.ylabel(None)
    plt.xlabel(None)
    wedges, texts, autotexts = ax.pie(values,labels=labels, autopct='%1.1f%%',startangle=140,colors=colors)
    plt.title("Plot of " + operation_type + " vs " + value_property)
    ax.set_axis_off()
    plt.show()


def generate_pastel_colors(n):
    colors = []

    # repeat this block n times
    # don't care about n.
    for _ in range(n):
        base_color = np.array([np.random.uniform(.5, 1) for _ in range(3)])
        white = np.array([1, 1, 1])
        color = (base_color + white) / 2
        colors.append(color)
    return colors
