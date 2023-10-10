from fastapi import FastAPI
from random import randint

app = FastAPI()

#123

@app.get("/percentage")
async def get_random_percentage():
    return {'percentage': randint(0, 100)}

@app.get("/percentage/{lower_limit}/{upper_limit}")
async def limit(lower_limit: int, upper_limit: int):
    if lower_limit > upper_limit:
        return {"error": "The upper limit must be bigger then the lower limit!",
                "lower limit": lower_limit,
                "upper limit": upper_limit}
    else:
        random_number = random.randint(lower_limit, upper_limit)
        return {"Percentage": random_number}
    