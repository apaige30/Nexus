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

def generate_assignment(users, experiments):

    assignments =[]



    for experiment in experiments:

        start = parse_time(experiment["start_at"])
        end = parse_time(experiment["end_at"])

        if end is None:
            end = datetime.now(timezone.utc)

        if start is None or end <= start:
            continue


        for user in users:
            if experiment["target_population"] == "premium_users":
                if user["subscription_tier"] !="Premium":
                    continue
                     
            elif experiment["target_population"] == "mobile_only":           
                if user["device_type"] not in ("iOS", "Android"):
                    continue
                
            elif experiment["target_population"] == "all_users":
                pass
            else:
                continue

            duration = (end -start).total_seconds()
            assigned = start +timedelta(seconds=random.uniform(0,duration))
            
            assignment = {
                "assignment_id": f"asn_{len(assignments) +1}",
                "experiment_id": experiment["experiment_id"],
                "user_id": user["user_id"],
                "variant": random.choice(experiment["variants"]),
                "assigned_at": assigned.isoformat()

            }

            assignments.append(assignment)
    return assignments

user_path = Path("data/raw/users.json")
experiment_path = Path("data/raw/experiments.json")
users = load_records(user_path)
experiment = load_records(experiment_path)

exp_assignments = generate_assignment(users,experiment)

output_path = Path("data/raw/assignments.json")
output_path.parent.mkdir(parents = True, exist_ok = True)


with output_path.open("w", encoding= "utf-8") as f:
    json.dump(exp_assignments, f, indent= 2)