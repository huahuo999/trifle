import torch

a = torch.rand(2, 2)
print(a)
print(torch.mean(a))
print(torch.sum(a))
print(torch.prod(a))
# 求乘积

print(torch.mean(a, dim=0))
# 按维度求和 进行降维度

print(torch.argmax(a, dim=0))
print(torch.argmin(a, dim=0))
print(torch.std(a))
print(torch.var(a))
print(torch.median(a))
print(torch.mode(a))

a = torch.rand(2, 2) * 10
print(a)
print(torch.histc(a, 6, 0, 0))

a = torch.randint(0, 10, [10])
print(torch.bincount(a))
# 只支持一维tensor
# 统计某一类别样本个数

