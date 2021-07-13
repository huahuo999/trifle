import torch
x = torch.ones(2, 2, requires_grad=True)
x.register_hook(lambda grad:grad*2)
y = x + 2
z = y * y * 3
z.backward(torch.ones(2, 2), retain_graph=True)
# retain_graph保留当前图
print(y.grad)
# y不是叶子结点
print(x.grad)
print(x.grad_fn)
print(y.grad_fn)
print(z.grad_fn)