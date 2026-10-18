import pandas as pd
import uuid
import json
from pathlib import Path
import random
from datetime import datetime, timedelta
from src.utils.time import random_timestamp

country =  ['US','MX','CA','GB','JP','UK']
device_type = ['iOS','Android','Web','TV','Gaming Console']
preferred_genres = ['Horror','Thriller','SCIFI','Romance','Comedy']
subscription = ["Free", "Premium"]
role = ["User", "Admin"]


def generate_users():

    user_role =  random.choice(role)

    subscription_tier = "Premium" if user_role =="Admin" else random.choice(subscription)
    return {
        

        "user_id": f"usr_{str(uuid.uuid4())}",
        "birth_year": random.randint(1960,2007),
        "subscription_tier": subscription_tier,
        "country": random.choice(country),
        "device_type": random.choice(device_type),
        "preferred_genres": random.sample(preferred_genres, k = 2),
        "engagement_level": round(random.uniform(0,1),2),
        "display_name": f"User_{random.randint(100,999)}",
        "role": user_role,
        "created_at": random_timestamp()

        }
users = [generate_users() for x in range(1000)]

output_path = Path("data/raw/users.json")
output_path.parent.mkdir(parents = True, exist_ok = True)

with output_path.open("w", encoding = "utf-8") as u:
    json.dump(users, u, indent =2)
