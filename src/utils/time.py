import pandas as pd
import uuid
import random
from datetime import datetime, timedelta

def random_timestamp(start_year = 2020, end_year =2026):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12,31)

    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return (start + timedelta(seconds = random_seconds)).isoformat() + "Z"