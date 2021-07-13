import torch

# torch.where

a = torch.rand(4, 4)
b = torch.rand(4, 4)
out = torch.where(a > 0.5, a, b)
print(a)
print(b)
print(out)
# 利用阈值做二值化

# torch.index_select
print("torch.index_select")
a = torch.rand(4, 4)
print(a)
print(torch.index_select(a, dim=0, index=torch.tensor([0, 3, 2])))

# torch.gather
print(torch.gather)
a = torch.linspace(1, 16, 16).view(4, 4)
print(torch.gather(a, dim=0, index=torch.tensor()))
# 按照列进行索引 每个对应一个维度
