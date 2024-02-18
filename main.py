from modules.convert_to_csv import convert_to_csv
from modules.drawDatabaseData import draw_database_data
from modules.parse_record_from_file import parse_record
import json
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    with open('data/input.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        records = parse_record(data)
    json_formatted = json.dumps(records, ensure_ascii=False, indent=4)
    print(json_formatted)

    draw_database_data('class', 'calls', 'select', records)
    draw_database_data('class', 'total_time', 'select', records)
    draw_database_data('class', 'calls', 'update', records)
    draw_database_data('class', 'total_time', 'update', records)
    convert_to_csv(records, 'data/output.csv')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
