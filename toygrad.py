# input processing of value and gradient

class Value:
    def __init__(self):
        self.data

    def __repr__(self):
        return f"value = {self.data}"

    def __add__(self, other_value): # a.__add__(b)
        return(self.data + other_value.data) 

    def __mul__(self, other_value): # a.__add__(b)
        return(self.data * other_value)

# gredient
a = 2.0
b = -1
c = 10
print(a, b)
print(a * b * c)