import re
import json

# ###
# #Example input
# #-[ RECORD 1 ]----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# # query      | UPDATE "users" SET "updated_at" = ?, "last_date_accessed" = ? WHERE "users"."id" = ? /*application:Workfeed,origin_host:d8c3138d13a7,worker:TouchUserWorker,line:/lib/sharding/transaction_enforcer/ar_base.rb:40:in `transaction',hostname:82cbd7001d7e,pid:547
# # 2*/
# # calls      | 1262
# # total_time | 8155.886
# ####

def get_operation_type(query):
    # Regular expression to match the beginning of the query with SQL operation keywords
    match = re.match(r'^(SELECT|UPDATE|INSERT INTO|DELETE)', query, re.IGNORECASE)
    if match:
        return match.group(1).upper()  # Returns the matched SQL operation in uppercase
    else:
        return "UNKNOWN"  # Return a default value if the operation type can't be determined

def parse_record(input_text):
    records = input_text.strip().split('-[ RECORD')

    # Define regex patterns for parsing
    query_re = re.compile(r'query\s+\|\s+([^/*]+)')  # Modified to exclude comments
    calls_re = re.compile(r'calls\s+\|\s+(\d+)')
    total_time_re = re.compile(r'total_time\s+\|\s+([\d.]+)')
    class_re = re.compile(r'/\*.*?(?:controller_with_namespace:|worker:)([^,]+),?')

    # create list
    parsed_data = []

    for record in records:
        query_match = query_re.search(record)
        calls_match = calls_re.search(record)
        total_time_match = total_time_re.search(record)
        class_match = class_re.search(record)

        if query_match and calls_match and total_time_match and class_match:
            query = query_match.group(1).strip()
            operation_type = get_operation_type(query)
            data = {
                "query": query,
                "calls": calls_match.group(1).strip(),
                "total_time": total_time_match.group(1),
                "class": class_match.group(1).strip(),
                "operation_type":  operation_type
            }

            parsed_data.append(data)

    return parsed_data

