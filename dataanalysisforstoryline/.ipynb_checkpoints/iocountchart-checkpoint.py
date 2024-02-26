
import matplotlib.pyplot as plt

# Data setup
time_points = ['Current', 'Teams Storyline Release', 'After 10% Growth']
users_table_records = [665115216, 935920549, 1029512604]  # Users table record count over the three points
messages_table_records = [1562916598, 1719208258, 1891128084]  # Messages table record count over the three points

# Server load IO for HDB and Messages servers
hdb_io_load = [825925.485, 908518.034, 999369.837]  # Original IO load on HDB server
messages_io_load = [1305478.38, 1436026.218, 1579628.84]  # Original IO load on Messages server
new_hdb_io_load = [1319168.185, 1451085.003, 1596193.503]  # New IO load on HDB server
new_messages_io_load = [1377591.724, 1555812.854, 1737591.724]  # New IO load on Messages server

# Plotting Operation Count for Users and Messages tables
plt.figure(figsize=(14, 7))
plt.plot(time_points, users_table_records, 'g-', label='Users Table Records', marker='o')
plt.plot(time_points, messages_table_records, 'r-', label='Messages Table Records', marker='o')

# Annotating the data points
for i, txt in enumerate(users_table_records):
    plt.annotate(txt, (time_points[i], users_table_records[i]), textcoords="offset points", xytext=(0,10), ha='center', color='green')
for i, txt in enumerate(messages_table_records):
    plt.annotate(txt, (time_points[i], messages_table_records[i]), textcoords="offset points", xytext=(0,10), ha='center', color='red')

plt.title('Record Count Over Time for Users and Messages Tables')
plt.xlabel('Time Point')
plt.ylabel('Record Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting IO Load for HDB and Messages servers
plt.figure(figsize=(14, 7))
plt.plot(time_points, hdb_io_load, 'g--', label='HDB Server IO Load', marker='o')
plt.plot(time_points, messages_io_load, 'r--', label='Messages Server IO Load', marker='o')
plt.plot(time_points, new_hdb_io_load, 'b-.', label='New HDB Server IO Load', marker='o', linewidth=2)
plt.plot(time_points, new_messages_io_load, 'm-.', label='New Messages Server IO Load', marker='o', linewidth=2)

# Annotating the data points for IO load
for i, txt in enumerate(hdb_io_load):
    plt.annotate(f"{txt:.2f}", (time_points[i], hdb_io_load[i]), textcoords="offset points", xytext=(0,10), ha='center', color='green')
for i, txt in enumerate(messages_io_load):
    plt.annotate(f"{txt:.2f}", (time_points[i], messages_io_load[i]), textcoords="offset points", xytext=(0,10), ha='center', color='red')
for i, txt in enumerate(new_hdb_io_load):
    plt.annotate(f"{txt:.2f}", (time_points[i], new_hdb_io_load[i]), textcoords="offset points", xytext=(0,10), ha='center', color='blue')
for i, txt in enumerate(new_messages_io_load):
    plt.annotate(f"{txt:.2f}", (time_points[i], new_messages_io_load[i]), textcoords="offset points", xytext=(0,10), ha='center', color='magenta')

plt.title('Server IO Load Over Time')
plt.xlabel('Time Point')
plt.ylabel('IO Load')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()