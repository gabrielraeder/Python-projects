from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def read_db():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-2",
            "title": "Notícia 2",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-3",
            "title": "Notícia 3",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 10,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-4",
            "title": "Notícia 4",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 12,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
    ]


@pytest.fixture
def group_result():
    return {
        "readable": [
            {
                "unfilled_time": 2,
                "chosen_news": [
                    (
                        "Notícia bacana",
                        4,
                    ),
                    (
                        "Notícia 2",
                        4,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Notícia 3",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("Notícia 4", 12),
        ],
    }


def test_reading_plan_group_news(read_db, group_result):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
    reading_plan = ReadingPlanService
    reading_plan._db_news_proxy = MagicMock(return_value=read_db)
    result = reading_plan.group_news_for_available_time(10)
    assert result == group_result
