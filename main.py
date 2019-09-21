from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

heroes = [
    {
        "id": 1,
        "name": "Clark Kent",
        "alter_ego": "Superman",
        "description": "He can fly and can be boring",
    },
    {
        "id": 2,
        "name": "Bruce Wayne",
        "alter_ego": "Batman",
        "description": "Always prepare, the most coolest hero",
    },
    {
        "id": 3,
        "name": "Diana Prince",
        "alter_ego": "Wonder Woman",
        "description": "She's a princess and she's a goddess",
    },
    {
        "id": 4,
        "name": "Arthur Curry",
        "alter_ego": "Aquaman",
        "description": "He can swim",
    },
]

app = FastAPI()


class Hero(BaseModel):
    id: int
    name: str
    alter_ego: str
    description: str = None


@app.get("/heroes/{hero_id}", response_model=Hero)
async def read_main(hero_id: int):
    hero = next(hero for hero in heroes if hero_id == hero['id'])
    if not hero:
        raise HTTPException(status_code=404, detail="Item not found")
    return hero


@app.post("/heroes/", response_model=Hero)
async def create_item(hero: Hero):
    if hero.dict() in heroes:
        raise HTTPException(status_code=400, detail="Item already exists")
    heroes.append(hero.dict())
    return hero
