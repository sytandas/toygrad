# grading and backpropagate
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1   # y = x² + 3x + 1
y.backward()         # compute dy/dx
print(x.grad)        # dy/dx = 2x + 3 → 7
