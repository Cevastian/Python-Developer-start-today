# Python initiate method exercise

class Smartphone:
    def __init__(self, model, year):    # initiate class 'Smartphone' with following variables and function
        self.model = model
        self.year = year
        self.model_year = model + " " + str(year)


Apple_phone = Smartphone("iPhone 14", 2022)
Samsung_phone = Smartphone("Galaxy S23", 2023)

print(Apple_phone.model, Apple_phone.year)
print(Samsung_phone.model, Samsung_phone.year)

print(Apple_phone.model_year)
print(Samsung_phone.model_year)


# Python Calculator initializer method example

'''
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, var1, var2):
        self.result = var1 + var2
        return self.result

    def sub(self, var1, var2):
        self.result = var1 - var2
        return self.result

test_add = Calculator()
test_sub = Calculator()

print(test_add.add(4, 7))

test_sub.sub(7, 2)
print(test_sub.sub(9,6))

# Python Class initializer variable transfer example

def __init__(self, var1, var2):
    self.first_var = var1
    self.second_var = var2

'''


