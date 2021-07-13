import torch

a = torch.Tensor([[1, 2], [3, 4]])
print(a)
print(a.type())
## 2*2的张量
b = torch.Tensor(2, 3)
print(b)
print(b.type())

c = torch.ones(2, 2)
print(c)
print(c.type())

d = torch.eye(2, 2)
print(d)
print(d.type())

e = torch.zeros(2, 2)
print(e)
print(e.type())

f = torch.zeros_like(b)
print(f)
print(f.type())

g = torch.ones_like(b)
print(g)
print(g.type())

'''随机'''
h = torch.rand(2, 2)
print(h)
print(h.type())

i = torch.normal(mean=0.0, std=torch.rand(5))
print(i)
print(i.type())

j = torch.normal(mean=torch.rand(5), std=torch.rand(5))
print(j)
print(j.type())

a = torch.Tensor(2, 2).uniform_(-1, 1)
print(a)
print(a.type())

'''序列'''
a = torch.arange(0, 10, 1)
print(a)
print(a.type())

a = torch.linspace(2, 10, 4)
print(a)
print(a.type())

a = torch.randperm(10)
print(a)
print(a.type())
