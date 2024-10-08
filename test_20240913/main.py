from typing import Union

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int, 
#     item: Item,
#     user: User,
#     importance: int = Body(gt=0),
#     q: str | None = None,
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results