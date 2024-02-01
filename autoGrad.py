import torch
weights = torch.ones(4,requires_grad=True)
print(weights)
for epich in range(2):
    model_output= (weights*3).sum()
    print(model_output)
    model_output.backward()
    print(weights.grad)
    weights.grad.zero_()
