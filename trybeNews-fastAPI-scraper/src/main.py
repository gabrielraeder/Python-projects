from fastapi import FastAPI, Body
from api.controllers.news_controller import NewsController
from api.middlewares import Middleware

app = FastAPI()

news_controller = NewsController()


@app.post("/scrape-news", status_code=201)
async def scrape(amount: int = Body(embed=True, default=None)):
    Middleware.amount(amount)
    return news_controller.scrape_news(amount)


@app.get("/top-categories")
async def categories():
    return news_controller.top_categories()


@app.get("/title/{title}")
async def title(title: str):
    return news_controller.title_search(title)


@app.get("/category/{category}")
async def category(category: str):
    return news_controller.category_search(category)


@app.get("/date/{yyyy-mm-dd}")
async def date(date: str):
    return news_controller.date_search(date)
