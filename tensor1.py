# pylint: disable=missing-module-docstring
import torch
x=torch.rand(4,4)
print(x)
# print(z)
y=x.view(-1,8)
print(y)
