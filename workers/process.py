import os

DIR = './xgpg2'

for filename in os.listdir(DIR):
    with open(os.path.join(DIR, filename), 'r') as f:
        kept = ['timestamp, utilization.gpu [%], memory.used [MiB]\n']
        for line in f.readlines():
            if line == 'timestamp, utilization.gpu [%], memory.used [MiB]\n':
                continue
            kept.append(line)
        with open(os.path.join(DIR, filename+'.csv'), 'w') as wf:
            wf.writelines(kept)
