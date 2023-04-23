import requests
from time import sleep
from bs4 import BeautifulSoup
import re


class NewsScraper:
    @staticmethod
    def beautify(page):
        return BeautifulSoup(page, "html.parser")

    @staticmethod
    def fetch(url):
        header = {"user-agent": "Fake user-agent"}
        sleep(1)
        try:
            response = requests.get(url, timeout=3, headers=header)
            response.raise_for_status()
        except (requests.HTTPError, requests.ReadTimeout):
            return None
        else:
            return response.text

    @staticmethod
    def scrape_updates(html_content):
        soup = NewsScraper.beautify(html_content)
        links = soup.find_all("a", {"class": "cs-overlay-link"})
        return [str(link["href"]) for link in links if links]

    @staticmethod
    def scrape_next_page_link(html_content):
        try:
            soup = NewsScraper.beautify(html_content)
            return soup.find("link", {"rel": "next"})["href"]
        except (TypeError, AttributeError):
            return None

    @staticmethod
    def clean_string(text: str):
        while text.endswith(" ") or text.endswith("\xa0"):
            text = text.rstrip(" ")
            text = text.rstrip("\xa0")
        return text

    @staticmethod
    def scrape_news(html_content):
        soup = NewsScraper.beautify(html_content)
        return {
            "url": soup.find("link", {"rel": "canonical"})["href"],
            "title": NewsScraper.clean_string(
                soup.find("h1", {"class": "entry-title"}).text
            ),
            "timestamp": soup.find("li", {"class": "meta-date"}).text,
            "writer": soup.find("a", {"class": "url fn n"}).text,
            "reading_time": int(
                re.findall(
                    r"\d+",
                    soup.find("li", {"class": "meta-reading-time"}).text,
                )[0]
            ),
            "summary": NewsScraper.clean_string(
                soup.find("div", {"class": "entry-content"}).p.text
            ),
            "category": soup.find("span", {"class": "label"}).text,
        }
