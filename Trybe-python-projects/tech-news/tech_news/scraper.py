import requests
from time import sleep
from bs4 import BeautifulSoup
import re
from tech_news.database import create_news, search_news


def beautify(page):
    return BeautifulSoup(page, "html.parser")


# Requisito 1
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


# Requisito 2
def scrape_updates(html_content):
    soup = beautify(html_content)
    links = soup.find_all("a", {"class": "cs-overlay-link"})
    return [str(link["href"]) for link in links if links]


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        soup = beautify(html_content)
        return soup.find("link", {"rel": "next"})["href"]
        # return soup.find("nav", {"class": "pagination"}).find(
        #     "a", {"class": "next"}
        # )["href"]
    except (TypeError, AttributeError):
        return None


def clean_string(text: str):
    while text.endswith(" ") or text.endswith("\xa0"):
        text = text.rstrip(" ")
        text = text.rstrip("\xa0")
    return text


# Requisito 4
def scrape_news(html_content):
    soup = beautify(html_content)
    return {
        "url": soup.find("link", {"rel": "canonical"})["href"],
        "title": clean_string(soup.find("h1", {"class": "entry-title"}).text),
        "timestamp": soup.find("li", {"class": "meta-date"}).text,
        "writer": soup.find("a", {"class": "url fn n"}).text,
        "reading_time": int(
            re.findall(
                r"\d+", soup.find("li", {"class": "meta-reading-time"}).text
            )[0]
        ),
        "summary": clean_string(
            soup.find("div", {"class": "entry-content"}).p.text
        ),
        "category": soup.find("span", {"class": "label"}).text,
    }


def create_news_db(links):
    news = [scrape_news(fetch(link)) for link in links]
    remove_repeated = [
        new
        for new in news
        if not search_news({"title": new["title"], "url": new["url"]})
    ]
    try:
        create_news(remove_repeated)
    except TypeError:
        return ""
    return remove_repeated


# Requisito 5
def get_tech_news(amount):
    page = fetch("https://blog.betrybe.com/")
    all_links = scrape_updates(page)
    next_link = scrape_next_page_link(page)
    while len(all_links) < amount:
        next_page = fetch(next_link)
        new_page_links = scrape_updates(next_page)
        all_links.extend(new_page_links)
        next_link = scrape_next_page_link(next_page)
    return create_news_db(all_links[:amount])
