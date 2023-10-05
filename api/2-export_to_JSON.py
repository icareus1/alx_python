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
    """
    Retrieve TODO list items for an employee from a remote API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of TODO list items (dictionaries).
    """
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
    """
    Retrieve the name of an employee from a remote API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee.
    """
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
    """
    Main function to display an employee's completed TODO tasks.
    """
    # Check if an employee ID is provided
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
        return

    emp_id = int(sys.argv[1])
    todo_items = get_todo_items(emp_id)
    
    if not todo_items:
        print("No TODO items found for this employee.")
        return

    emp_name = get_employee_name(emp_id)
    
    # Create a dictionary with the expected JSON structure
    employee_json = {
        str(emp_id): [
            {
                "task": item["title"],
                "completed": item["completed"],
                "username": emp_name
            }
            for item in todo_items
        ]
    }

    # Specify the JSON file path
    json_file_path = f'{emp_id}.json'

    # Write the JSON data to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(employee_json, json_file)

if __name__ == "__main__":
    main()
