#1.
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
#-----------------------------------------------------------------------
#2.
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
#challenge2

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_skill(self):
        print(f"{self.name} has a special skill: {self.hunting_skill}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def display_strength(self):
        print(f"{self.name}'s strength is {self.strength}.")


dog1 = Dog("Buddy", 3, "Golden")
dog1.description()
dog1.get_info()
dog2 = JackRussellTerrier("Max", 2, "White and Brown", "excellent digging")
dog2.description()
dog2.get_info()
dog2.special_skill()
dog3 = Bulldog("Rocky", 4, "Brown", "impressive")
dog3.description()
dog3.get_info()
dog3.display_strength()

"""
expected output
Buddy is 3 years old.
Buddy's coat color is Golden.
Max is 2 years old.
Max's coat color is White and Brown.
Max has a special skill: excellent digging
Rocky is 4 years old.
Rocky's coat color is Brown.
Rocky's strength is impressive.
"""


