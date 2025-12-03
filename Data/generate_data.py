import pandas as pd
import random
from datetime import datetime, timedelta

authors = ['alice', 'bob', 'charlie']
statuses = ['success', 'failed', 'cancelled']
data = []

start_date = datetime(2025, 1, 1)

for i in range(1, 501):
    run_time = start_date + timedelta(hours=i*2)
    duration = random.randint(100, 300)
    status = random.choices(statuses, weights=[0.7, 0.25, 0.05])[0]
    author = random.choice(authors)
    data.append([i, status, duration, run_time, author])

df = pd.DataFrame(data, columns=['build_id', 'status', 'duration_seconds', 'trigger_time', 'author'])
df.to_csv("pipeline_data.csv", index=False)