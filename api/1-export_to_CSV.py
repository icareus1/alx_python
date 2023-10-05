import csv
import os
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

# Function to get the employee's username
def get_employee_username(employee_id):
    """
    Retrieve the username of an employee from a remote API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The username of the employee.
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

    emp_username = get_employee_username(emp_id)
    csv_filename = f"{emp_id}.csv"
    
    # Open the CSV file for writing
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for item in todo_items:
            completed_status = "True" if item["completed"] else "False"
            task_title = item["title"]
            writer.writerow({
                "USER_ID": emp_id,
                "USERNAME": emp_username,
                "TASK_COMPLETED_STATUS": completed_status,
                "TASK_TITLE": task_title
            })

    # Remove the blank line at the end of the file
    with open(csv_filename, 'rb+') as csv_file:
        csv_file.seek(-2, os.SEEK_END)
        csv_file.truncate()

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    main()
