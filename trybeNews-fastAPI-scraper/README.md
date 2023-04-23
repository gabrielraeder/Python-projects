# fastAPI-scraper-project

## Build with:
 - [Python](https://www.python.org/)
 - [FastAPI](https://fastapi.tiangolo.com/)
 - [MongoDB](https://www.mongodb.com/)
 - [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/#)
 - [Uvicorn](https://www.uvicorn.org/)

------

#### - Clone Repository
```sh
git clone git@github.com:gabrielraeder/fastAPI-project.git
```

## Run application with:
```sh
chmod +x install-project.sh && ./install-project.sh
```
<details>
  <summary>Or install it yourself</summary>

  ## Install
#### - Virtual environment
```sh
python3 -m venv .venv && source .venv/bin/activate
```
#### - Install dependencies
```sh
python3 -m pip install -r dev-requirements.txt
```
#### - Docker container for MongoDB
```sh
docker-compose up -d
```
## Start
```sh
cd src && uvicorn main:app --reload
```
</details>

<br>

## Stop application with:
```sh
docker-compose down && deactivate
```

------

Access documentation at http://localhost:8000/docs

------

**Developed By [Gabriel Gonçalves](https://www.linkedin.com/in/gabrielraedergoncalves/).**
