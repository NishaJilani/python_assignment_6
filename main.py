# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Anaya", 97)
s2 = Student("Salar", 100)
print(s1.name, s1.marks)
print(s2.name, s2.marks)

# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        return(f"Total objects created: {cls.count}")
    
c1 = Counter()
c2 = Counter()
c3 = Counter()
print(c1.display_count())


# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return(f"{self.brand} is starting")
    
car1 = Car("Mercedes")
car2 = Car("BMW")
print(car1.start())
print(car2.start())


# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Meezan Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(b1.bank_name)
print(b2.bank_name)
Bank.change_bank_name("Bank Al Habib limited")
print(b1.bank_name)
print(b2.bank_name)


# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(5, 10))
    
# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

log1 = Logger()
print(log1)

del log1


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp1 = Employee("Anaya", 50000, "123-45-6789")
print(emp1.name)
print(emp1._salary)
# print(emp1.__ssn)
print(emp1._Employee__ssn)

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t1 = Teacher("Anaya", "Chemistry")
print(f"Teacher name: {t1.name}, Subject: {t1.subject}")

# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
r1 = Rectangle(5, 10)
print(f"Area of Rectangle: {r1.area()}")

# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return(f"{self.name} says woooffff!!!")

dog1 = Dog("Tommy", "Labrador")
print(dog1.bark())    


# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author

        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
b1 = Book("A Good Girl Guides to Murder", "Holly Jackson")
b2 = Book("Good Girl Bad Blood", "Holly Jackson")
b3 = Book("As Good As Dead", "Holly Jackson")
b4 = Book("Silent Patient", "Alex Michaelides")

print(f"Total Books Created: {Book.get_total_books()}")
    

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
celsius = (25)
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equall to {fahrenheit}°F.")

# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        return "Engine Started..."
    
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        return self.engine.start()
    
engine1 = Engine()
car1 = Car(engine1)
print(car1.start_car())

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return(f"Employee: {self.name}")
    
class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def show_department_details(self):
        return(f"{self.name}, {self.employee.get_details()}")
    
emp1 = Employee("Alice")
dep1 = Department("HR", emp1)

print(dep1.show_department_details())

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "A's show() method."
    
class B:
    def show(A):
        return "B's show() method."
    
class C:
    def show(A):
        return "C's show() method."
    
class D(B, C):
    pass

d = D()
print(d.show())

print(D.__mro__)

# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper():
        print("Function is being called.")

        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply decorator to a Person class

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Anaya")
print(p1.greet())

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class product:
    def __init__(self, price):
        self._price = price

@property
def price(self):
    # getter for price
    return self._price

@price.setter
def price(self, value):
    # """Setter for price"""
    if value < 0:
        raise ValueError("Price cannot be negative.")
    self._price = value

    @price.deleter
    def price(self):
        # Deleter for price
        print("Deleting price...")
        del self._price

p = product(100)
print(p._price)

p.price = 150
print(p.price)

del p.price

# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
    
# creating an instance with a specific factor
double = Multiplier(2)

# check if the obj is callable()
print(callable(double))

# call the object like a function
print(double(4))

# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, messege="Age must be 18 or older."):
        super().__init__(messege)

def check_age(age):
        if age < 18:
            raise InvalidAgeError()
        else:
            print("Access granted.")

# use try...except to handle the exceptions
try:
    user_age = int(input("Enter your age:"))
    check_age(user_age)
except InvalidAgeError as e:
    price(f"Access denied: {e}")
except ValueError:
    print("Please enter a valid number.")

# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage
for number in Countdown(5):
    print(number)


