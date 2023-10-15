# create a class programmer for storing info of few programers working at microsoft
import sys


class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


nikhs = Programmer("nikhs", "Skype")
harry = Programmer("harry", "GitHub")
nikhs.getInfo()
harry.getInfo()


# write a class calculator capable of finding square, cube and square root of a number
# we can also initialize the number using __init__ method
class Calculator:
    def square(self, number):
        print(f"Square of {number}: {number**2}")

    def cube(self, number):
        print(f"Cube of {number}: {number**3}")

    def squareRoot(self, number):
        print(f"Square root of {number}: {number**0.5}")


calculate = Calculator()
user = int(input('Enter number: '))
calculate.square(user)
calculate.cube(user)
calculate.squareRoot(user)


# Create a class with a class attribute a; create an object from it and set a directly using object a=0. Does this change the class attribute?
# Answer is No
class User:
    a = "nikhs"

    def printData(self):
        print(f'User:{self.a}')


person = User()
person.a = "John"
person.printData()
print(User.a)


# Add a static method in problem 2 to greet the user with hello
class Calculator:

    def __init__(self, number):
        self.number = number

    @staticmethod
    def greet():
        print('Welcome!')

    def square(self):
        print(f"Square of {self.number}: {self.number**2}")

    def cube(self):
        print(f"Cube of {self.number}: {self.number**3}")

    def squareRoot(self):
        print(f"Square root of {self.number}: {self.number**0.5}")


user = int(input('Enter number: '))

calculate = Calculator(user)
calculate.greet()

calculate.square()
calculate.cube()
calculate.squareRoot()


# Write a class Train which has methods to book a ticket, get status ( no. of seats) and get fare information of trains running under Indian Railways


class Train:
    def __init__(self, name, fare, seat):
        self.name = name
        self.fare = fare
        self.seat = seat

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available are {self.seat}")

    def getFareInformation(self):
        print(f"The price of the ticket is {self.fare}")

    def bookTicket(self):
        if (self.seat > 0):
            print(
                f'Your ticket has been booked! Your seat number is {self.seat}')
            self.seat -= 1
        else:
            print('Sorry, there is no tickets available')

    def cancelTicket(self, seat):
        list_of_seats = []
        for i in range(1, (self.seat)+1):
            list_of_seats.append(i)

        self.seat += 1
        list_of_seats.append(seat)
        print(list_of_seats)


intercity = Train('intercity', 100, 4)
intercity.getStatus()
intercity.getFareInformation()
intercity.bookTicket()
intercity.getStatus()
yes_or_no = input('Do you want to cancel this ticket? ')
if yes_or_no == 'yes':
    seat_number = int(input("Enter your seat number:"))
    intercity.cancelTicket(seat_number)
    intercity.getStatus()
else:
    sys.exit()


# Define a base class Vehicle
class Vehicle:
    def __init__(self):
        self.steering_wheel = True
        self.accelerator = True
        self.clutch = True
        self.brakes = True

    def start(self):
        print("Starting the vehicle")

# Define a class Car that inherits from Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 4

    def start(self):
        super().start()
        print("Car started")

# Define a class Truck that inherits from Vehicle


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 6

    def start(self):
        super().start()
        print("Truck started")

# Define a class Bus that inherits from Vehicle


class Bus(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 8

    def start(self):
        super().start()
        print("Bus started")


# Create instances of each class and call their start methods
car = Car()
truck = Truck()
bus = Bus()

car.start()
truck.start()
bus.start()
print(bus.wheels)
print(bus.steering_wheel)
