import uuid
from src.utils.time import random_timestamp
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path
import json


target_pop = ["US Users", "New Users", "Mobile Only", "TV Only", "Premium Users", "High Engagement Users", "All Users"]
metrics = ["click_through_rate","watch_time", "session_length","buffering_rate","conversion_rate"]

experiment_info = [
    {   
        "experiment_id":"exp_001",
        "experiment_name":"Homepage Layout Optimization",
        "primary_metric": "click_through_rate",
        "status": "completed",
        "target_population": "all_users"    
    },
    {   
        "experiment_id":"exp_002",
        "experiment_name":"Recommendation",
        "primary_metric": "watch_time",
        "status": "running",
        "target_population": "premium_users"    
    },
    {
        "experiment_id":"exp_003",
        "experiment_name":"Notification",
        "primary_metric": "sessions_per_user",
        "status": "draft",
        "target_population": "mobile_only"        
    }
    ]

def generate_experiments(seed):

    status = seed["status"]
    now = datetime.now(timezone.utc)

    if status == "draft":
        start_at = (now + timedelta(days =7)).isoformat()
        end_at = None

    elif status == "running":
        start_at = (now - timedelta(days =14)).isoformat()
        end_at = None

    elif status == "completed":
        end = now - timedelta(days=1)
        start = end - timedelta(days =30)
        start_at = start.isoformat()
        end_at = end.isoformat()

    else:
        raise ValueError(f"Invalid status: {status}")


    return { 

        "experiment_id": seed["experiment_id"],
        "experiment_name": seed["experiment_name"],
        "status": status,
        "start_at": start_at,
        "end_at": end_at,
        "variants": ["Control", "Treatment"],
        "primary_metric": seed["primary_metric"],
        "target_population": seed["target_population"]

        }

experiments = []

for experiment_seed in experiment_info:
    experiments.append(generate_experiments(experiment_seed))

output_path = Path("data/raw/experiments.json")
output_path.parent.mkdir(parents =True, exist_ok = True)

with output_path.open("w", encoding = "utf-8") as f:
    json.dump(experiments,f, indent =2)
    