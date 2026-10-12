from datetime import timedelta, datetime,timezone
import json
import argparse
from pathlib import Path
import random


def load_records(path):

    with Path(path).open(encoding = "utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError(f"Expected a JSON array in {path}")
    return records

def parse_time(value):
    if not value:
        return None
    if len(value) == 10:
        value  += "T00:00:00+00:00"
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        result = result.replace(tzinfo=timezone.utc)
    return result.astimezone(timezone.utc)


return[
    {
        "assignment_id":
        "experiment_id":
        "user_id": 
        "variant":
        "assigned_at"



    }
]