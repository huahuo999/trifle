import torch

a = torch.rand(2, 2)
a = a * 10
print(a)
print(a.shape)
print(torch.floor(a))
print(torch.ceil(a))
print(torch.round(a))
print(torch.trunc(a))
# 整数部分
print(torch.frac(a))
# 小数部分
print(a % 2)
# 取余
