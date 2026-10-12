import uuid
from utils.time import random_timestamp
import random
from datetime import datetime, timedelta, timezone


target_pop = ["US Users", "New Users", "Mobile Only", "TV Only", "Premium Users", "High Engagement Users", "All Users"]
metrics = ["click_through_rate","watch_time", "session_length","buffering_rate","conversion_rate"]

experiments = [
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

    status = experiments["status"]
    now = datetime.now(timezone.utc)

    if status == "draft":
        start_at = now + timedelta(days =7).date().isoformat()
        end_at = None

    elif status == "running":
        start_at = now - timedelta(days =14).date().isoformat()
        end_at = None

    elif status == "completed":
        end_at = now - timedelta(days=1).date().isoformat()
        start_at = end_at - timedelta(days=30).date().isoformat()

    else:
        raise ValueError(f"Invalid status: {status}")


    return { 

        "experiment_id": experiments["experiment_id"],
        "experiment_name": experiments["experiment_name"],
        "status": status,
        "start_at": start_at,
        "end_at": end_at,
        "variants": ["Control", "Treatment"],
        "primary_metric": experiments["primary_metric"],
        "target_population": experiments["target_population"]

        }

experiments = []

for seed in experiments:
    experiments.append(generate_experiments(seed))
    