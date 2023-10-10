import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

with open(r'practice/04_10_23.py/ASSIGNMENT_06/employee.json', 'r') as json_file:
    data = json.load(json_file)
    for employee_data in data:
        name = employee_data["name"]
        dob = employee_data["DOB"]
        height = employee_data["height"]
        city = employee_data["city"]
        state = employee_data["state"]
        
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")

# expected output
# Name: Ajith, DOB: 1992-08-05, Height: 6'6", City: Mumbai, State: Maharastra
# Name: Boby simha, DOB: 1988-03-25, Height: 5'10", City: Chennai, State: Tamilnadi
# Name: Cibichandran, DOB: 1995-11-05, Height: 5'4", City: Banagalore, State: Karnataka
# Name: Vijaykumar, DOB: 1990-06-03, Height: 6'0", City: Hyderabad, State: Telangana
# Name: Surya, DOB: 1987-09-15, Height: 5'7", City: Trivandrum, State: Kerala



"""
#json data
 [
    {
      "name": "Ajith",
      "DOB": "1992-08-05",
      "height": "6'6\"",
      "city": "Mumbai",
      "state": "Maharastra"
    },
    {
      "name": "Boby simha",
      "DOB": "1988-03-25",
      "height": "5'10\"",
      "city": "Chennai",
      "state": "Tamilnadi"
    },
    {
      "name": "Cibichandran",
      "DOB": "1995-11-05",
      "height": "5'4\"",
      "city": "Banagalore",
      "state": "Karnataka"
    },
    {
      "name": "Vijaykumar",
      "DOB": "1990-06-03",
      "height": "6'0\"",
      "city": "Hyderabad",
      "state": "Telangana"
    },
    {
      "name": "Surya",
      "DOB": "1987-09-15",
      "height": "5'7\"",
      "city": "Trivandrum",
      "state": "Kerala"
    }
  ]
"""

import json

indian_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Kerala":   "Trivandrum",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

with open('indian_capitals.json', 'w') as json_file:
    json.dump(indian_capitals, json_file)

print("Data has been written to 'indian_capitals.json' successfully.")

"""
expected output
Data has been written to 'indian_capitals.json' successfully.
"""