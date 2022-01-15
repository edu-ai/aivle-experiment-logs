import os
from datetime import datetime

WEB_LOG_NAME = 'debug.log.5'

logs = {}

earliest_task_start_time = None
latest_submit_time = None
latest_finish_time = None

with open(WEB_LOG_NAME, 'r') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        if "job task started" in line:
            splits = line.split(' ')
            ts_string = splits[1] + ' ' + splits[2]
            dt_object = datetime.strptime(ts_string, '%Y-%m-%d %H:%M:%S,%f')
            uid = splits[6]
            node = splits[-1].rstrip('\n')
            logs[uid] = {'started': (node, dt_object)}
            if earliest_task_start_time is None or dt_object < earliest_task_start_time:
                earliest_task_start_time = dt_object
    for line in lines:
        if "is submitted" in line:
            splits = line.split(' ')
            ts_string = splits[1] + ' ' + splits[2]
            dt_object = datetime.strptime(ts_string, '%Y-%m-%d %H:%M:%S,%f')
            uid = splits[5]
            logs[uid]['submitted'] = (dt_object)
            if latest_submit_time is None or dt_object > latest_submit_time:
                latest_submit_time = dt_object
    for line in lines:
        if "finished" in line:
            splits = line.split(' ')
            ts_string = splits[1] + ' ' + splits[2]
            dt_object = datetime.strptime(ts_string, '%Y-%m-%d %H:%M:%S,%f')
            uid = splits[6]
            node = splits[-1].rstrip('\n')
            logs[uid]['finished'] = (node, dt_object)
            if latest_finish_time is None or dt_object > latest_finish_time:
                latest_finish_time = dt_object

# the start time is defined to be the earlier of {last submitted time, first start task time}
start_time = latest_submit_time
if earliest_task_start_time < start_time:
    start_time = earliest_task_start_time
# total time is defined to be the difference between the start time and the latest task finish time
total_time = latest_finish_time - start_time
print(total_time)

count = {}

for uid in logs:
    log = logs[uid]
    # check if tasks are distributed evenly
    if log['started'][0] in count.keys():
        count[log['started'][0]] += 1
    else:
        count[log['started'][0]] = 1
    # calculate total time (from submission to )
print(count)