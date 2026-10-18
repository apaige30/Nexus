from datetime import timedelta, datetime

import pandas as pd
import uuid
import json
from pathlib import Path
import random
from datetime import datetime, timedelta,timezone
from src.utils.time import random_timestamp




def load_records(path):

    with Path(path).open(encoding = "utf-8")  as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON array {path}")
    return data

def parse_time(time):

    if not time:
        return None
    if isinstance(time, str) and len (time) == 10:
        time += ("T00:00:00+00:00")
    dt = datetime.fromisoformat(time.replace("Z","00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)



user_path = Path("/data/raw/users.json")
content_path = Path("data/raw/content.json")
event_type_path = Path("data/raw/event_types.json")
experiment_path = ("data/raw/experiments.json")
assignment_path = ("data/raw/assignment.json")

users = load_records(user_path)
content = load_records(content_path)
event_types = load_records(event_type_path)
experiments = load_records(experiment_path)
assignments = load_records(assignment_path)



def generate_events(user, content, experiments, assignments,event_types, seed = 42
                    ):




return [
    
{
    "event_id":
    "timestamp":
    "user_id":
    "event_type":
    "content_id":
    "session_id":
    "experiment_id":
    "variant":
    "source":
    "device_type":
    "watch_seconds"
    "position"
}
]


