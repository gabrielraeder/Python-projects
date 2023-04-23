from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file = read(path)
    return max(
        {
            int(item["max_salary"])
            for item in file
            if item["max_salary"].isdigit()
        }
    )


def get_min_salary(path: str) -> int:
    file = read(path)
    return min(
        {
            int(item["min_salary"])
            for item in file
            if item["min_salary"].isdigit()
        }
    )


def validate_properties_and_salary(job: Dict, salary: Union[int, str]):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) not in [int, str]
        or type(job["max_salary"]) not in [int, str]
        or type(salary) not in [int, str]
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError("Invalid information")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_properties_and_salary(job, salary)
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    result = []
    errors = []
    for job in jobs:
        try:
            is_valid = matches_salary_range(job, salary)
        except ValueError as err:
            errors.append(err)
        else:
            if is_valid:
                result.append(job)
    return result
