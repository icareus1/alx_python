import csv
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

  # Export TODO list items to CSV
  with open(f"{emp_id}.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    # Write the data rows
    for item in todo_items:
      writer.writerow([emp_id, emp_name, item["completed"], item["title"]])

if __name__ == "__main__":
  main()