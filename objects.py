#Create a class called Circle with a method that computes the area of the circle.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
my_circle = Circle(4)
print(my_circle.area()) 


          
            
    

#Create a class called Rectangle with methods to compute the area and perimeter of the 
#rectangle.
class Rectangle:
    def __init__(self,length,width):
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*(self.width+self.length) 
my_rectangle=Rectangle(7,5) 
print(my_rectangle.area())
print(my_rectangle.perimeter())  

#Create a class called Employee with attributes name, age, and salary. Create a method
# that increases the salary of an employee object by a certain percentage.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def raise_salary(self, percentage):
        self.salary += self.salary * percentage / 100
# Create an employee object
employee = Employee('John', 25, 50000)

# Print the initial salary
print('Initial salary:', employee.salary)

# Raise the salary by 10%
employee.raise_salary(10)

# Print the updated salary
print('Updated salary:', employee.salary)

#Create a class called Car with attributes make, model, and year. Create a method that 
#returns a string representation of the car object in the form "year make model".

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
print(my_car)

#Create a class called BankAccount with attributes account_number and balance. Create 
#methods to deposit and withdraw funds from the account.
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited {amount} in account number {self.account_number}.New balance is:{self.balance}")
    def withdraw(self,amount):
        if self.balance>amount:
            print(f"withdrew {amount} from account number {self.account_number}.New balance is{self.balance}")
        else:
            self.balance<amount
            print(f"withdrew failed.insuffient balance in account number {self.account_number}.new balance is {self.balance}")

account1 = BankAccount("123456789", 500.0)
account1.deposit(100.0)
account1.withdraw(2500.0)


class Ankara:
    def __init__(self,temperature,mood):
        self.temperature=temperature
        self.mood=mood
    def change_pattern(self):
        temperature=40
        mood='happy' 
        if self.temperature>=temperature  and self.mood>=mood:
            print(f"wear light and more patterned Ankara")
        else: 
            print(f"wear dull and less patterned Ankara") 
            
ankara=Ankara(20,"happy") 
print(ankara.change_pattern()) 
             


class AnkaraFabric:
    def __init__(self, temperature, mood):
        self.temperature = temperature
        self.mood = mood

    def predict_pattern_change(self):
        if self.temperature > 45 and self.mood == 'happy':
            return 'Wear light and more patterned Ankara'
        elif self.temperature < 45 and self.mood == 'sad':
            return 'Wear dull and less patterned Ankara'
        else:
            return 'No change in pattern'
fabric = AnkaraFabric(23, 'sad')
print(fabric.predict_pattern_change())

# class Animal:
#     def __init__(self, species, name, current_location):
#         self.species = species
#         self.name = name
#         self.current_location = current_location
#     def migrate(self, next_location):
#         print(f"The {self.name}, one of the {self.species}, is migrating from {self.current_location} to {next_location}.")
class Environment:
    def __init__(self, weather, river, predators_current_location):
        self.weather = weather
        self.river = river
        self.predators_current_location = predators_current_location
    def check_conditions(self,animal,next_location):
    
        if self.weather == "Sunny" and self.river == "Low" and self.predators_current_location=="mara":
            return f" this {animal} is migrating from {self.predators_current_location} to the {next_location}"
        elif self.weather== "rainy" and self.river=="high" and self.predators_current_location=="serengeti":
            return f" this {animal} is migrating from {self.predators_current_location} to the {next_location}"
        else:
            return "No migration"

env = Environment("Sunny", "Low", "mara")
print(env.check_conditions("zebra","serengeti"))

class FilmProject:
    def __init__(self, name, cast, schedule, budget):
        self.name = name
        self.cast = cast
        self.schedule = schedule
        self.budget = budget
        self.projects=[]

# class MovieManager:
#     def __init__(self):
#         self.projects = []
    
    def add_project(self, project):
        self.projects.append(project)
        return f"{project.name} added to project list."
    
    def remove_project(self, project_name):
        for project in self.projects:
            if project.name == project_name:
                self.projects.remove(project)
                return f"{project_name} removed from project list."
        # return f"Project {project_name} not found."
    
    def adjust_budget(self, project_name, new_budget):
        for project in self.projects:
            if project.name == project_name:
                project.budget = new_budget
                return f"{project_name} budget adjusted to {new_budget}."
        # return f"Project {project_name} not found."
    
    def schedule_shoot(self, project_name, new_schedule):
        for project in self.projects:
            if project.name == project_name:
                project.schedule = new_schedule
                return f"{project_name} shoot scheduled for {new_schedule}."
        # return f"Project {project_name} not found."

project1 = FilmProject("The Batman", ["Robert Pattinson", "Zoe Kravitz", "Paul Dano"], "2022-03-07", 1000)
# project=busy
# add=project1.add_project(busy)
# print(add)
project1.add_project(project1)
print(project1.projects)

project1.remove_project("The Batman")
print(project1.projects)

project1.adjust_budget("The Batman", 2000)
print(project1.budget)

project1.schedule_shoot("The Batman", "2023-03-04")
print(project1.schedule)






