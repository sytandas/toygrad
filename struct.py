# input processing of value and gradient
class Value:
    def __init___(self, data):
        self.data = data 
        print(data)
#    def __repr__(self):
#        return f"value = {self.data}"
#        print(data)
    def __add__(self, other_value): # a.__add__(b)
        return(self.data + other_value.data) 
        print(data)

    def __mul__(self, other_value): # a.__add__(b)
        return(self.data * other_value)

a = 2.0
b = -1
c = 10
print(a, b)
print(a * b * c)