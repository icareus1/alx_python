import json
import requests

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

# Function to get the employee's username
def get_employee_username(employee_id):
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
    all_employee_data = {}  # Dictionary to store data for all employees

    for emp_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        todo_items = get_todo_items(emp_id)
        emp_username = get_employee_username(emp_id)

        if not todo_items:
            print(f"No TODO items found for Employee {emp_id}.")
            continue

        employee_data = []

        for item in todo_items:
            task_data = {
                "username": emp_username,
                "task": item["title"],
                "completed": item["completed"]
            }
            employee_data.append(task_data)

        all_employee_data[str(emp_id)] = employee_data

    # Specify the JSON file path
    json_file_path = 'todo_all_employees.json'

    # Open the JSON file in write mode
    with open(json_file_path, 'w') as json_file:
        # Serialize and write the data to the JSON file with proper indentation
        json.dump(all_employee_data, json_file)

if __name__ == "__main__":
    main()
