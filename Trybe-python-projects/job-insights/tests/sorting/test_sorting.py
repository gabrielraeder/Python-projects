from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def max_salary():
    return [
        {"date_posted": "2019-05-08", "max_salary": 10000, "min_salary": 1000},
        {"date_posted": "", "max_salary": 4000, "min_salary": None},
        {"date_posted": "2020-05-08", "max_salary": 1500, "min_salary": 500},
        {"date_posted": "2021-05-08", "max_salary": 500, "min_salary": 100},
    ]


@pytest.fixture
def min_salary():
    return [
        {"date_posted": "2021-05-08", "max_salary": 500, "min_salary": 100},
        {"date_posted": "2020-05-08", "max_salary": 1500, "min_salary": 500},
        {"date_posted": "2019-05-08", "max_salary": 10000, "min_salary": 1000},
        {"date_posted": "", "max_salary": 4000, "min_salary": None},
    ]


@pytest.fixture
def date_posted():
    return [
        {"date_posted": "2021-05-08", "max_salary": 500, "min_salary": 100},
        {"date_posted": "2020-05-08", "max_salary": 1500, "min_salary": 500},
        {"date_posted": "2019-05-08", "max_salary": 10000, "min_salary": 1000},
        {"date_posted": "", "max_salary": 4000, "min_salary": None},
    ]


def test_sort_by_criteria(max_salary, min_salary, date_posted):
    mock = [
        {"date_posted": "2020-05-08", "max_salary": 1500, "min_salary": 500},
        {"date_posted": "2019-05-08", "max_salary": 10000, "min_salary": 1000},
        {"date_posted": "2021-05-08", "max_salary": 500, "min_salary": 100},
        {"date_posted": "", "max_salary": 4000, "min_salary": None},
    ]
    sort_by(mock, "max_salary")
    assert mock == max_salary

    sort_by(mock, "min_salary")
    assert mock == min_salary

    sort_by(mock, "date_posted")
    assert mock == date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: xxx"):
        sort_by(mock, "xxx")
