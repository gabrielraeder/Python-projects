from fastapi import FastAPI, Body
from api.controllers.store_controller import StoresController
from pydantic import BaseModel

app = FastAPI()

storesController = StoresController()


class Item(BaseModel):
    search_term: str
    quantity: int


@app.post("/scrape-product", status_code=201)
async def scrape(obj: Item = Body(embed=True, default=None)):
    return storesController.scrape(obj.search_term, obj.quantity)
