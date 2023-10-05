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
    return response.json()["name"]
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return "Unknown"

# Function to export TODO list items to JSON
def export_to_json(emp_id, emp_name, todo_items):
  """
  Export TODO list items to JSON.

  Args:
    emp_id (int): The ID of the employee.
    emp_name (str): The name of the employee.
    todo_items (list): A list of TODO list items (dictionaries).
  """

  # Create a JSON object
  json_data = {
    "USER_ID": emp_id,
    "USERNAME": emp_name,
    "TASKS": [],
  }

  # Add the TODO list items to the JSON object
  for item in todo_items:
    json_data["TASKS"].append({
      "task": item["title"],
      "completed": item["completed"],
    })

  # Write the JSON object to a file
  with open(f"{emp_id}.json", "w") as f:
    json.dump(json_data, f, indent=4)

# Main function
def main():
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

  # Export TODO list items to JSON
  export_to_json(emp_id, emp_name, todo_items)

if __name__ == "__main__":
  main()