from datetime import datetime, timezone, timedelta
import pandas as pd

####
## Reference time, in our time zone
now = datetime.now()
date_format = '%Y-%m-%d %H:%M:%S'
timezone = datetime.now().astimezone().tzinfo
due_date = 'due'# ({})'.format(timezone)

## Grace period
grace = timedelta(days=5)

def is_unsubmitted(x):
    return x['Status'] == 'Missing' or x['Total Score'] is None or x['Total Score'] < x['Max Points'] / 2.0 

def is_overdue(x, due):
    if not pd.isnull(x[due_date]):
        due = x[due_date]
    return is_unsubmitted(x) and due < now + grace

def is_near_due(x, due):
    if not pd.isnull(x[due_date]):
        due = x[due_date]

    return is_unsubmitted(x) and (due - now) < timedelta(days = 2) and not is_overdue(x, due)# now < due + timedelta(days=5)

def is_submitted(x: pd.Series):
    return x['Status'] != 'Missing'

def is_below_mean(x: pd.Series, mean: float, total = None):
    if total is None:
        total = 'Total Score'
    return x[total] < mean

def is_far_below_mean(x: pd.Series, mean: float, total = None):
    if total is None:
        total = 'Total Score'
    print (x[total], mean)
    return x[total] < mean / 2

def is_far_above_mean(x: pd.Series, max, mean: float, total = None):
    if total is None:
        total = 'Total Score'
    return x[total] >= max * 0.9

def row_test(row: pd.Series, due: datetime, mean: float, median: int, min: int, max: int, stdev: float, row_test_fn: callable) -> str:
    return row_test_fn(row)