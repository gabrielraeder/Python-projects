# Tech News

## Build with:
 - [Python](https://www.python.org/)
 - [MongoDB](https://www.mongodb.com/)
 - [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/#)
 - [Requests](https://pypi.org/project/requests/)

------

#### - Clone Repository
```sh
git clone git@github.com:gabrielraeder/Python-projects.git
```
#### - Access directory
```sh
cd Python-projects/Trybe-python-projects/tech-news
```


## Install
#### - Virtual environment
```sh
python3 -m venv .venv && source .venv/bin/activate
```
#### - Install dependencies
```sh
python3 -m pip install -r dev-requirements.txt
```

#### - Start Mongo Container
```sh
docker-compose up -d mongodb
```

## Start
- Inside the Virtual environment:
```sh
tech-news-analyzer
```

## Tests
```sh
python3 -m pytest
```

------

**Developed By [Gabriel Gonçalves](https://www.linkedin.com/in/gabrielraedergoncalves/) while studying at Trybe.**
