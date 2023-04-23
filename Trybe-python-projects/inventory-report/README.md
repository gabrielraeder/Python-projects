# Inventory report

## Build with:
 - [Python](https://www.python.org/)

------

#### - Clone Repository
```sh
git clone git@github.com:gabrielraeder/Python-projects.git
```
#### - Access directory
```sh
cd Python-projects/Trybe-python-projects/inventory-report
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
```sh
pip install .
```

## Start
```sh
inventory_report arg1 arg2
```
##### or
```sh
python3 -m inventory_report.main argumento1 argumento2
```
> arg1 must be a path to a file to be imported, this file may be `csv`, `json` or `xml`.

> arg2 must be either of the following strings: `simples` or `completo`, each generating their respective report.

<br>


------

**Developed By [Gabriel Gonçalves](https://www.linkedin.com/in/gabrielraedergoncalves/) while studying at Trybe.**