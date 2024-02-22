"""
uncategorized
| where TIMESTAMP > ago(7d) and
        tailed_path == "/var/log/service/headroom.log" and
        (fqcn contains "inkshield")
| extend data = parse_json(log_line)
| extend metric = tostring(data["metric"])
| extend cluster = tostring(data["cluster"])
| extend value = toreal(data["value"])
| extend table = tostring(data["table"])
| extend tableType = iif(table == "users", "Users", "Other")
| extend dbserver = case(
    fqcn contains "altair", "messages",
    fqcn contains "inkshield", "hdb",
    "unknown"
)
//| where table == 'users'//or table == 'messages'
| extend io_impact = case(
    metric in ("seq_scan", "idx_scan", "n_tup_ins", "n_tup_upd", "n_tup_del", "vacuum_count", "indexsize", "tableTotalSize", "n_dead_tup"), "High",
    metric in ("seq_tup_read", "idx_tup_read", "idx_tup_fetch", "n_mod_since_analyze", "n_live_tup", "autovacuum_count", "autoanalyze_count", "analyze_count"), "Medium",
    "Low"
)
| where io_impact == "High"
| project TIMESTAMP, cluster, dbserver, table, metric, value, io_impact, tableType
| extend day = format_datetime(TIMESTAMP, 'yyyy-MM-dd')
| summarize TotalHighImpactValue = sum(value) by day, tableType
| order by day
| render linechart

2024-02-21	Other	24310414332168.0
2024-02-21	Users	18386581134625.0
2024-02-20	Other	202407260335558.0
2024-02-20	Users	153186811267947.0
2024-02-19	Other	137456827868459.0
2024-02-19	Users	104138394902569.0
2024-02-18	Other	145362789522313.0
2024-02-18	Users	110244843171442.0
2024-02-17	Other	290589817418502.0
2024-02-17	Users	220468632256357.0
2024-02-16	Other	241804902932030.0
2024-02-16	Users	183596131855785.0
2024-02-15	Other	48306814531780.0
2024-02-15	Users	36702977203678.0
2024-02-14	Other	144816514033324.0
2024-02-14	Users	110087909186747.0
"""
# Given data for comparison of servers "hdb" and "messages"

import pandas as pd
import matplotlib.pyplot as plt

# Data for plotting
data = {
    'Date': [
        "2024-02-21", "2024-02-21",
        "2024-02-20", "2024-02-20",
        "2024-02-19", "2024-02-19",
        "2024-02-18", "2024-02-18",
        "2024-02-17", "2024-02-17",
        "2024-02-16", "2024-02-16",
        "2024-02-15", "2024-02-15",
        "2024-02-14", "2024-02-14"
    ],
    'Table': [
        "Other", "Users",
        "Other", "Users",
        "Other", "Users",
        "Other", "Users",
        "Other", "Users",
        "Other", "Users",
        "Other", "Users",
        "Other", "Users"
    ],
    'IO': [
        24310414332168.0, 18386581134625.0,
        202407260335558.0, 153186811267947.0,
        137456827868459.0, 104138394902569.0,
        145362789522313.0, 110244843171442.0,
        290589817418502.0, 220468632256357.0,
        241804902932030.0, 183596131855785.0,
        48306814531780.0, 36702977203678.0,
        144816514033324.0, 110087909186747.0
    ]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Convert 'Date' string to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plotting setup
plt.figure(figsize=(14, 9))

# Color mapping for each table
colors = {'Users': 'blue', 'Other': 'red'}

# Plotting each series with annotations
for table in df['Table'].unique():
    subset = df[df['Table'] == table]
    plt.plot(subset['Date'], subset['IO'], marker='o', label=table, color=colors[table])
    # Annotating each point with its IO value
    for i, row in subset.iterrows():
        plt.text(row['Date'], row['IO'], f"{row['IO']:,.0f}", color=colors[table], fontsize=9, rotation=45, ha='right')

# Final plot adjustments
plt.title('HDB Server Overall vs Users Table IO with Point Labels')
plt.xlabel('Date')
plt.ylabel('IO Usage (in billions)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
