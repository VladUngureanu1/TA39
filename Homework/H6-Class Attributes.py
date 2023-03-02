# 1
class Circle:
    radius = 5
    color = 'rosu'

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def describe_circle(self):
        print(f'The radius of the circle is {self.radius} and the color is  {self.color}.')

    def area(self):
        return 3.14 * (self.radius ** 2)

    def diameter(self):
        return self.radius * 2

    def circumference(self):
        return 2 * 3.14 * self.radius


circle1 = Circle(10, 'green')
circle1.describe_circle()
print('The area of the circle is', circle1.area())
print('The diameter of the circle is', circle1.diameter())
print('The circumference of the circle is, ', round(circle1.circumference(), 2))
circle2 = Circle(25, 'blue')
circle2.describe_circle()
print('The area of the circle is', circle2.area())
print('The diameter of the circle is', circle2.diameter())
print('The circumference of the circle is', round(circle2.circumference(), 2))

# 2
class Rectanle:
    lenght = 10
    width = 5
    color = 'gray'

    def __init__(self, lenght, width, color):
        self.lenght = lenght
        self.width  = width
        self.color = color

    def describe(self):
        print(f'The new color is {self.color}')

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return (self.lenght + self.width) * 2

    def change_color(self, new_color):
        self.color = new_color


rectangle1 = Rectanle(30, 20, 'red')
rectangle1.describe()
print(rectangle1.area())
print(rectangle1.perimeter())
rectangle1.change_color('red')
rectangle1.describe()
rectangle2 = Rectanle(40, 30, 'blue')
rectangle2.describe()
print(rectangle2.area())
print(rectangle2.perimeter())
rectangle2.change_color('green')
rectangle2.describe()

# 3
class Employee:
    first_name = 'David'
    last_name = 'Coop'
    salary = 2000

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def describe(self, department):
        print('The department this employee belongs to is:', department)

    def full_name(self):
        print(f'The employee-s full name is {self.first_name} {self.last_name}.')

    def monthly_salary(self):
        print(f'He has a salary of {self.salary} RON/luna.')

    def annual_salary(self):
        print(f'The annual salary is {self.salary * 12} RON.')

    def salary_increase(self, percent):
        print(f'This employee-s salary increase will be: {round(percent / 100 * self.salary)} RON')


employee1 = Employee('Maria', 'Vlas', 3000)
employee1.describe('HR')
employee1.full_name()
employee1.monthly_salary()
employee1.annual_salary()
employee1.salary_increase(15)
employee2 = Employee('Sorin', 'Ovidiu', 4000)
employee2.describe('banking')
employee2.full_name()
employee2.monthly_salary()
employee2.annual_salary()
employee2.salary_increase(25)

# 4
class Account:
    iban = '1111 2222 3333 4444'
    account_holder = 'Dan Spataru'
    bank_balance = 10000

    def __init__(self, iban, account_holder, bank_balance):
        self.iban = iban
        self.account_holder = account_holder
        self.bank_balance = bank_balance

    def show_balance(self):
        print(f'The holder {self.account_holder} has in account {self.iban} the amount of {self.bank_balance} RON.')

    def debit_account(self, sum):
        self.bank_balance -= sum
        print(f'From the curent account was withdrawn {sum}, and the current amount is: {self.bank_balance} RON')

    def account_crediting(self, sum):
        self.bank_balance += sum
        print(f'To the current amount was added {sum}, and the current amount is: {self.bank_balance} RON')


account1 = Account('1111 1111 1111 1111', 'Ion Dolanescu', 20000)
account1.show_balance()
account1.debit_account(1000)
account1.account_crediting(2000)
account2 = Account('2222 2222 2222 2222', 'Maria Ciobanu', 15000)
account2.show_balance()
account2.debit_account(500)
account2.account_crediting(1000)