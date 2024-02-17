import csv


def convert_to_csv(records, filepath='records.csv'):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['query', 'calls', 'total_time', 'class', 'operation_type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for record in records:
            writer.writerow(record)
