import csv
from collections import Counter
from datetime import datetime

def read_csv(filename):
    """Reads a CSV file and returns a list of dictionaries for its contents."""
    with open(filename, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(filename, list_of_dictionaries):
    """Writes a list of dictionaries to a CSV file."""
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list_of_dictionaries[0].keys())
        writer.writeheader()
        writer.writerows(list_of_dictionaries)

def filter_by_key(list_of_dictionaries, key, value):
    """Returns a list of dictionaries that contain the given key-value pairing."""
    return [entry for entry in list_of_dictionaries if entry[key] == value]

def discard_by_key(list_of_dictionaries, key, value):
    """Returns a list of dictionaries that do not contain the given key-value pairing."""
    return [entry for entry in list_of_dictionaries if entry[key] != value]

def filter_range(list_of_dictionaries, key, low, high):
    """Returns a list of dictionaries within a specified range of a given key."""
    return [entry for entry in list_of_dictionaries if low <= entry[key] < high]

def calculate_duration(date1_str, date2_str):
    """Calculates the duration in days between two dates."""
    date_format = "%m/%d/%Y"  # Assuming the date format is like '01/31/2020'
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    return (date2 - date1).days

def get_departments(list_of_dictionaries):
    """Returns a sorted list of unique departments."""
    return sorted(set(entry["SUBJECT"] for entry in list_of_dictionaries))

def get_open_year(entry):
    """Returns the year a request was opened."""
    return entry["OPEN DATE"].split('/')[-1]

def filter_year(list_of_dictionaries, low, high):
    """Filters entries based on year range."""
    return [entry for entry in list_of_dictionaries if low <= get_open_year(entry) < high]

def parse_date(date_str):
    """Converts a date string to a datetime.date object."""
    return datetime.strptime(date_str, "%m/%d/%Y").date()

