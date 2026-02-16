# input processing of value and gradient

class Value:
    def __init__(self, data, _children=()): # empty tuple for child node
        self.data = data
        self.grad = 0.0
        self._previous = set(_children)
        self._backward = lambda: None
        
    def __repr__(self):
        return f"value = {self.data}, grad ={self.grad}"

    def __add__(self, other): # a.__add__(b)
        out = Value(self.data + other.data, (self, other)) # Return Value
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
       
        out._backward = _backward
        return out

    def __mul__(self, other): # a.__mul__(b)
        out = Value(self.data * other.data, (self, other)) # same 
        def _backward():
            self.grad += out.grad * other.data
            other.grad += out.grad * self.data
        
        out._backward = _backward
        return out

    # backpropagation - topological sort of the graph 
    def backward(self):
        topo = []
        visit = set()

        def build(v):
            if v not in visit: 
                visit.add(v)
                for child in v._previous:
                    build(child)
                topo.append(v)

        build(self)

        self.grad = 1.0

        for v in reversed(topo):
            v._backward()

a = Value(2.0)
b = Value(-1.0)
c = Value(10.0)

d = a * b
e = d * c   # output

e.backward()

print("e =", e)
print("a.grad =", a.grad)
print("b.grad =", b.grad)
print("c.grad =", c.grad)