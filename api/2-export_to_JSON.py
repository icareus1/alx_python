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

# Main function
def main():
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
        return

    emp_id = int(sys.argv[1])
    todo_items = get_todo_items(emp_id)
    
    if not todo_items:
        print("No TODO items found for this employee.")
        return

    emp_name = get_employee_name(emp_id)
    
    # Create a list of dictionaries in the format specified
    output_data = [
        {
            "task": item["title"],
            "completed": item["completed"],
            "username": emp_name
        }
        for item in todo_items
    ]

    # Create a dictionary for the final JSON structure
    employee_json = {
        str(emp_id): output_data
    }

    # Specify the JSON file path
    json_file_path = f'{emp_id}.json'

    # Open the JSON file in write mode
    with open(json_file_path, 'w') as json_file:
        # Serialize and write the data to the JSON file
        json.dump(employee_json, json_file)

if __name__ == "__main__":
    main()
