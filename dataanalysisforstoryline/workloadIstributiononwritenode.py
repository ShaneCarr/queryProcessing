""""

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
| where table == 'users'
| project TIMESTAMP, cluster, dbserver, table, metric, value, io_impact
| extend day = format_datetime(TIMESTAMP, 'yyyy-MM-dd')
| summarize TotalHighImpactValue = sum(value) by metric, table, day//, table
| order by day



metric	day	TotalHighImpactValue
n_tup_upd	2024-02-21	2947655040
idx_scan	2024-02-21	14314824762732.0
indexsize	2024-02-21	4807517372416
tableTotalSize	2024-02-21	5389832486912
vacuum_count	2024-02-21	0
n_dead_tup	2024-02-21	43450067
n_tup_del	2024-02-21	0
seq_scan	2024-02-21	228
n_tup_ins	2024-02-21	348684448
idx_scan	2024-02-20	89464142778859.0
n_tup_ins	2024-02-20	2171307741
n_tup_upd	2024-02-20	18345522468
n_tup_del	2024-02-20	0
indexsize	2024-02-20	30031121219584.0
seq_scan	2024-02-20	1425
n_dead_tup	2024-02-20	451819502
vacuum_count	2024-02-20	0
tableTotalSize	2024-02-20	33670578618368.0
idx_scan	2024-02-19	60832140013689.0
tableTotalSize	2024-02-19	22883488964608.0
indexsize	2024-02-19	20408664653824.0
seq_scan	2024-02-19	969
n_tup_ins	2024-02-19	1468919307
n_tup_upd	2024-02-19	12400649142
n_tup_del	2024-02-19	0
n_dead_tup	2024-02-19	231701030
vacuum_count	2024-02-19	0
tableTotalSize	2024-02-18	24221377724416.0
indexsize	2024-02-18	21600975634432.0
seq_scan	2024-02-18	1026
n_tup_ins	2024-02-18	1548487813
idx_scan	2024-02-18	64407714378074.0
n_tup_del	2024-02-18	0
n_dead_tup	2024-02-18	170464160
vacuum_count	2024-02-18	0
n_tup_upd	2024-02-18	13056481521
seq_scan	2024-02-17	2052
indexsize	2024-02-17	43193128861696.0
tableTotalSize	2024-02-17	48432692846592.0
idx_scan	2024-02-17	128813313578607.0
n_tup_ins	2024-02-17	3089701907
n_tup_upd	2024-02-17	26040787943
n_tup_del	2024-02-17	0
n_dead_tup	2024-02-17	366477560
vacuum_count	2024-02-17	0
tableTotalSize	2024-02-16	40293054545920.0
vacuum_count	2024-02-16	0
n_dead_tup	2024-02-16	470937437
n_tup_del	2024-02-16	0
n_tup_upd	2024-02-16	21527115151
n_tup_ins	2024-02-16	2554258456
idx_scan	2024-02-16	107338394713591.0
indexsize	2024-02-16	35940130283520.0
seq_scan	2024-02-16	1710
tableTotalSize	2024-02-15	8050917523456
idx_scan	2024-02-15	21466781813119.0
indexsize	2024-02-15	7180412444672
vacuum_count	2024-02-15	0
n_dead_tup	2024-02-15	72705538
n_tup_del	2024-02-15	0
n_tup_upd	2024-02-15	4284274269
n_tup_ins	2024-02-15	508442282
seq_scan	2024-02-15	342
indexsize	2024-02-14	21531581857792.0
n_tup_ins	2024-02-14	1521180904
seq_scan	2024-02-14	1026
idx_scan	2024-02-14	64398720978906.0
n_tup_upd	2024-02-14	12811729759
n_tup_del	2024-02-14	0
n_dead_tup	2024-02-14	176327832
vacuum_count	2024-02-14	0
tableTotalSize	2024-02-14	24143097110528.0
"""