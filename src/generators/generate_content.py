import uuid
from src.utils.time import random_timestamp
import random
import json
from pathlib import Path
from datetime import timedelta, datetime

# content_type = ['movie','series','documentary',shorts]
# genre = ['Horror','Thriller','SCIFI','Romance','Comedy']
# titles = ['Friday', 'Harry Potter', 'Jason Bourne', 
#           'Insidious', 'Als Revenge', 'Broken Signal', 
#           'Broly Returns', 'Neon Skies','Fantasia']

content_seed = [
    {

    "content_id": "cnt_001",
    "author_id": "auth_001",
    "genre": "Comedy",
    "title": "Friday",
    "content_type": "movie"

    },
    {

    "content_id": "cnt_002",
    "author_id": "auth_002",
    "genre": "SCIFI",
    "title": "Harry Potter",
    "content_type": "movie"
    },
    {

    "content_id": "cnt_003",
    "author_id": "auth_003",
    "genre": "Comedy",
    "title": "Jason Bourne",
    "content_type": "documentary"
    },
    {

    "content_id": "cnt_004",
    "author_id": "auth_004",
    "genre": "Horror",
    "title": "Insidious",
    "content_type": "movie"
    },
    {

    "content_id": "cnt_005",
    "author_id": "auth_005",
    "genre": "Thriller",
    "title": "Als Revenge",
    "content_type": "documentary"
    },
    {

    "content_id": "cnt_006",
    "author_id": "auth_006",
    "genre": "Thriller",
    "title": "Broken Signal",
    "content_type": "short"
    },
    {

    "content_id": "cnt_007",
    "author_id": "auth_007",
    "genre": "Comedy",
    "title": "Neon Skies",
    "content_type": "short"
    },
    {

    "content_id": "cnt_008",
    "author_id": "auth_008",
    "genre": "Romance",
    "title": "Broly Returns",
    "content_type": "documentary"
    },
    {

    "content_id": "cnt_009",
    "author_id": "auth_009",
    "genre": "SCIFI",
    "title": "Fantasia",
    "content_type": "short"
    },

    {

    "content_id": "cnt_010",
    "author_id": "auth_010",
    "genre": "Romance",
    "title": "Notebook",
    "content_type": "movie"
    },
    {

    "content_id": "cnt_011",
    "author_id": "auth_011",
    "genre": "Horror",
    "title": "BMF",
    "content_type": "documentary"
    }


    ]


def random_published_date ():

    start = datetime(2010,1,1)
    end = datetime(2025,12,31)

    days_between = (end - start).days
    random_days = random.randint(0, days_between)

    return(
        start+ timedelta(days = random_days)
    ).date().isoformat()

def generate_content(seed):

    content = seed["content_type"]

    if content == "movie":
        duration = random.randint(4800,9000)
    elif content == "series":
        duration = random.randint(1200,4200)
    elif content =="short":
        duration = random.randint(10,60)
    else:
        duration = random.randint(1800,7200)


    return {

        "content_id":seed["content_id"],
        "author_id":seed["author_id"],
        "title": seed["title"],
        "content_type": seed["content_type"],
        "genre": seed["genre"],
        "duration_seconds": duration,
        "quality_score": round(random.uniform(.3,1.0),2),
        "published_at": random_published_date()


        }

content = []
for seed in content_seed:
    content.append(generate_content(seed))

output_path = Path("data/raw/content.json")
output_path.parent.mkdir(parents = True, exist_ok = True)

with output_path.open("w", encoding = "utf-8") as f:
    json.dump(content, f, indent =2)