# input processing of value and gradient
import math

class Value:
    def __init__(self, data, _children=()): # empty tuple for child node
        self.data = data
        self.grad = 0.0
        self._previous = set(_children)
        self._backward = lambda: None
    
    def __neg__(self): # -self
        return self * -1

    def __radd__(self, other): # other + self
        return self + other

    def __sub__(self, other): # self - other
        return self + (-other)

    def __rsub__(self, other): # other - self
        return other + (-self)

    def __rmul__(self, other): # other * self
        return self * other

    def __truediv__(self, other): # self / other
        return self * other**-1

    def __rtruediv__(self, other): # other / self
        return other * self**-1

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"    

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
    
    def __rmul__(self, other):  # for doing other * self (to avoiding the eroor)
        return self * other
    
    def __truediv__(self, other):   # divition self / other ~ self * other ^-1
        return self * other**-1

    def tanh(self):
        x = self.data
        t = ((math.exp(2*x) - 1) / (math.exp(2*x) + 1)) 
        out = Value(t, (self, ), )

        def _backward():
            self.grad += (1 - t**2) * out.grad # derivative of tanh is 1 - tanh^2 
        out._backward = _backward
        return out
    
    def exp(self):
        x = self.data
        out = Value(math.exp(x), (self, ), )

        def _backward():  
            self.grad += out.data * out.grad
        out._backward = _backward
        return out
    
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other-1)) * out.grad
        out._backward = _backward

        return out
   
    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out

    # backpropagation - topological sort of the graph 
    def backward(self):
        # building topological graph 
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
b = a.tanh()
b.backward()
print(f'tanh {a}')

a = Value(2.0)
b = a.exp()
b.backward()
print(f'exp {a}')