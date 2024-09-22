from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *,
    # ge=1(item_id>=1), gt=1(item_id>1), le(item_id<=1)
    item_id: int = Path(title="The ID of the item to get", gt=1, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results