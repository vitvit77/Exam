from fastapi import FastAPI, Query
from pydantic import BaseModel
import db

database = db.Database("./db.json")
print(database.get_by_id(1))

app = FastAPI()

@app.get('/sensors')
async def get_all_sensors():
    return database.get_all_sensors(item)