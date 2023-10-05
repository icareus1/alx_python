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
    Main function to export employee's TODO list in JSON format.
    """
    if len(sys.argv) < 2:
        print("Please provide the employee ID as a command-line argument.")
        return

    emp_id = int(sys.argv[1])
    todo_items = get_todo_items(emp_id)
    
    if not todo_items:
        print("No TODO items found for this employee.")
        return

    emp_name = get_employee_name(emp_id)
    json_filename = f"{emp_id}.json"


    # Create a dictionary to store the data in the specified format
    employee_data = {str(emp_id): []}

    for item in todo_items:
        completed_status = False if not item["completed"] else True
        task_title = item["title"]
        data_entry = {
            "task": task_title,
            "completed": completed_status,
            "username": emp_name
        }
        employee_data[str(emp_id)].append(data_entry)

    # Convert the data to JSON format
    json_data = json.dumps(employee_data)

    # Write the JSON data to a file named EMPLOYEE_ID.json
    json_filename = f"{emp_id}.json"
    with open(json_filename, "w") as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    main()
