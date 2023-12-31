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
        return response.json()["name"]
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
    
    # Calculate the number of completed tasks
    completed = [todo for todo in todo_items if todo['completed']]
    num_completed = len(completed)
    
    # Calculate the total number of tasks
    total = len(todo_items)
    
    print(f"Employee {emp_name} is done with tasks({num_completed}/{total}):")

    for item in todo_items:
        if item["completed"]:
            print(f"\t {item['title']}")

if __name__ == "__main__":
    main()
