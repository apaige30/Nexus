import uuid
from utils.time import random_timestamp
import random

content_type = ['movie','series','documentary']
genre = ['Horror','Thriller','SCIFI','Romance','Comedy']
titles = ['Friday', 'Harry Potter', 'Jason Bourne', 
          'Insidious', 'Als Revenge', 'Broken Signal', 
          'Broly Returns', 'Neon Skies','Fantasia']

def generate_content():

    return {

        "content_id": str(uuid.uuid4()),
        "author_id":f"auth_{random.randint(0,999)}",
        "title": random.choice(titles),
        "content_type": random.choice(content_type),
        "genre": random.choice(genre),
        "duration_seconds": random.randint(8,14400),
        "quality_score": round(random.uniform(.3,1.0),2),
        "published_at": random_timestamp()


        }

