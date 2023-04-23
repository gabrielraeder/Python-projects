from fastapi import FastAPI, Body, Query
from api.controllers.news_controller import NewsController
from api.middlewares import Middleware

app = FastAPI()

news_controller = NewsController()


@app.post("/scrape-news", status_code=201, tags=["scrape"])
async def scrape(amount: int = Body(embed=True, default=None)):
    Middleware.amount(amount)
    return news_controller.scrape_news(amount)


@app.get("/top-categories", tags=["search-filters"])
async def categories():
    return news_controller.top_categories()


@app.get("/title/", tags=["search-filters"])
async def title(q: str = Query(default="", max_length=50)):
    return news_controller.title_search(q)


@app.get("/category/{category}", tags=["search-filters"])
async def category(category: str):
    return news_controller.category_search(category)


@app.get("/date/{yyyy-mm-dd}", tags=["search-filters"])
async def date(date: str):
    return news_controller.date_search(date)
