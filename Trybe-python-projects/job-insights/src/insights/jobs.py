from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    if not path.endswith(".csv"):
        raise ValueError("Formato inválido!")
    with open(path, encoding="utf8") as file:
        content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = content
    result = [
        {header[index]: item for index, item in enumerate(value)}
        for value in data
    ]
    return result


def get_unique_job_types(path: str) -> List[str]:
    return {item["job_type"] for item in read(path)}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
