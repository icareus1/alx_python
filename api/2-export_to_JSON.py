"""
Module for retrieving and exporting TODO list items for employees.

This module provides two functions:

* `get_todo_items()`: Retrieves TODO list items for an employee.
* `export_to_csv()`: Exports TODO list items to a CSV file.
"""

import json
import requests
import sys

# Function to get TODO list items for an employee
def get_todo_items(employee_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

# Function to get the employee's name
def get_employee_name(employee_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()["username"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Unknown"

#Main function
def main():
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
        return

    emp_id = int(sys.argv[1])
    todo_items = get_todo_items(emp_id)
    
    if not todo_items:
        print("No TODO items found for this employee.")
        return

    # Get the employee's name
    employee_name = get_employee_name(emp_id)

    # Prepare the data to be exported

    data = {
        str(emp_id): [
                {
                "task": item["title"],
                "completed": item["completed"],
                "username": employee_name
                }
                for item in todo_items
        ]
    }

    # Export the data to JSON
    with open(f"{emp_id}.json", "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()
