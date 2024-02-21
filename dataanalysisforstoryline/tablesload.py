"""

uncategorized
| where TIMESTAMP > ago(7d) and
        tailed_path == "/var/log/service/headroom.log" and
        (fqcn contains "inkshield" or fqcn contains "altair")
| extend data = parse_json(log_line)
| extend metric = tostring(data["metric"])
| extend cluster = tostring(data["cluster"])
| extend value = toreal(data["value"])
| extend table = tostring(data["table"])
| extend dbserver = case(
    fqcn contains "altair", "messages",
    fqcn contains "inkshield", "hdb",
    "unknown"
)
| where table == 'users' or table == 'messages'
| extend io_impact = case(
    metric in ("seq_scan", "idx_scan", "n_tup_ins", "n_tup_upd", "n_tup_del", "vacuum_count", "indexsize", "tableTotalSize", "n_dead_tup"), "High",
    metric in ("seq_tup_read", "idx_tup_read", "idx_tup_fetch", "n_mod_since_analyze", "n_live_tup", "autovacuum_count", "autoanalyze_count", "analyze_count"), "Medium",
    "Low"
)
| where io_impact == "High"
| project TIMESTAMP, cluster, dbserver, table, metric, value, io_impact
| extend day = format_datetime(TIMESTAMP, 'yyyy-MM-dd')
| summarize TotalHighImpactValue = sum(value) by day, table
| order by day


"""
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "day": [
        "2024-02-21", "2024-02-20", "2024-02-20", "2024-02-19", "2024-02-19",
        "2024-02-18", "2024-02-18", "2024-02-17", "2024-02-17", "2024-02-16",
        "2024-02-16", "2024-02-15", "2024-02-15", "2024-02-14", "2024-02-14"
    ],
    "table": [
        "users", "messages", "users", "messages", "users",
        "messages", "users", "users", "messages", "messages",
        "users", "users", "messages", "messages", "users"
    ],
    "TotalHighImpactValue": [
        6128814194901, 97439606342100.0, 153186811267947.0, 97389495205014.0, 104138394902569.0,
        97339993739146.0, 110244843171442.0, 220468632256357.0, 97307903344847.0, 97262815437860.0,
        183596131855785.0, 36702977203678.0, 97229339529514.0, 8101056055471, 110087909186747.0
    ]
}

df = pd.DataFrame(data)
df['day'] = pd.to_datetime(df['day'])  # Convert 'day' to datetime
df.sort_values(by='day', inplace=True)  # Sort by day for chronological plotting

# Plot settings
plt.figure(figsize=(14, 8))
colors = {"users": "green", "messages": "red"}  # Color assignments for each table

for table in df['table'].unique():
    table_df = df[df['table'] == table]
    plt.plot(table_df['day'], table_df['TotalHighImpactValue'], marker='o', label=table, color=colors[table])
    for i, point in table_df.iterrows():
        plt.text(point['day'], point['TotalHighImpactValue'], f"{point['TotalHighImpactValue']:,.0f}",
                 fontsize=8, rotation=45, ha='right', va='bottom', color=colors[table])

plt.title("IO Load Comparison: Users vs Messages tables")
plt.xlabel("Day")
plt.ylabel("Total High Impact IO Value")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


