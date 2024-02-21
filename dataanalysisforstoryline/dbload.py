"""

// mix
uncategorized
| where TIMESTAMP > ago(7d) and
        tailed_path == "/var/log/service/headroom.log" and
        fqcn contains "inkshield"  // Uncomment and adjust logic if needed for "hdb"
        or fqcn contains "altair" // current messages primary VM
| extend data =parse_json(log_line)
| extend metric=tostring(data["metric"])
| extend cluster=tostring(data["cluster"])
| extend value=toreal(data["value"])
| extend dbserver = case(
    fqcn contains "altair", "messages",
    fqcn contains "inkshield", "hdb",
    "unknown" // Fallback value
)
| project TIMESTAMP, cluster, metric, value, dbserver // Include dbserver in the projection
| extend day = format_datetime(TIMESTAMP, 'yyyy-MM-dd')
| where metric == "xact_commit"
| summarize TotalHighImpactValue = sum(value) by day, dbserver
| order by day

2024-02-21	messages	140339871260
2024-02-21	hdb	908974065862
2024-02-20	messages	1680676100925
2024-02-20	hdb	11351146323491.0
2024-02-19	messages	1675746440930
2024-02-19	hdb	7707565832986
2024-02-18	messages	1671872718683
2024-02-18	hdb	8149330267635
2024-02-17	hdb	16287007870092.0
2024-02-17	messages	1669596464541
2024-02-16	hdb	13547222882240.0
2024-02-16	messages	1665855058725
2024-02-15	messages	1661305754913
2024-02-15	hdb	2705886434836
2024-02-14	hdb	8111060863502
2024-02-14	messages	138272818285

"""
# Given data for comparison of servers "hdb" and "messages"

import pandas as pd
import matplotlib.pyplot as plt
server_data = {
    "day": [
        "2024-02-21", "2024-02-21", "2024-02-20", "2024-02-20",
        "2024-02-19", "2024-02-19", "2024-02-18", "2024-02-18",
        "2024-02-17", "2024-02-17", "2024-02-16", "2024-02-16",
        "2024-02-15", "2024-02-15", "2024-02-14", "2024-02-14"
    ],
    "dbserver": [
        "messages", "hdb", "messages", "hdb",
        "messages", "hdb", "messages", "hdb",
        "hdb", "messages", "hdb", "messages",
        "messages", "hdb", "hdb", "messages"
    ],
    "TotalHighImpactValue": [
        140339871260, 908974065862, 1680676100925, 11351146323491.0,
        1675746440930, 7707565832986, 1671872718683, 8149330267635,
        16287007870092.0, 1669596464541, 13547222882240.0, 1665855058725,
        1661305754913, 2705886434836, 8111060863502, 138272818285
    ]
}

# Convert to DataFrame
server_df = pd.DataFrame(server_data)
server_df['day'] = pd.to_datetime(server_df['day'])  # Convert 'day' to datetime
server_df.sort_values(by='day', inplace=True)  # Sort by day for chronological plotting

# Plot settings
plt.figure(figsize=(14, 8))
server_colors = {"hdb": "blue", "messages": "orange"}  # Color assignments for each server

for dbserver in server_df['dbserver'].unique():
    dbserver_df = server_df[server_df['dbserver'] == dbserver]
    plt.plot(dbserver_df['day'], dbserver_df['TotalHighImpactValue'], marker='o', label=dbserver, color=server_colors[dbserver])
    for i, point in dbserver_df.iterrows():
        plt.text(point['day'], point['TotalHighImpactValue'], f"{point['TotalHighImpactValue']:,.0f}",
                 fontsize=8, rotation=45, ha='right', va='bottom', color=server_colors[dbserver])

plt.title("Server IO Load Comparison: HDB vs Messages")
plt.xlabel("Day")
plt.ylabel("Total High Impact IO Value")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

