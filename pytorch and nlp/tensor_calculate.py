import torch

# add

a = torch.rand(2, 3)
b = torch.rand(2, 3)

print(a)
print(b)

print(a + b)
print(a.add(b))
print(torch.add(a, b))
print(a)
print(a.add_(b))

# sub
print("==== sub res ====")
print(a - b)
print(a.sub(b))
print(a.sub_(b))
print(a)

# mul

print("===== mul ======")
print(a * b)
print(torch.mul(a, b))
print(a.mul(b))
print(a)
print(a.mul_(b))
print(a)

# div
print("=== div ===")
print(a / b)
print(torch.div(a, b))
print(a.div(b))
print(a.div_(b))
print(a)

# matmul

a = torch.ones(2, 1)
b = torch.ones(1, 2)
print(a @ b)
print(a.matmul(b))
print(torch.mm(a, b))
print(a.mm(b))

# 高维tensor

a = torch.ones(1, 2, 3, 4)
b = torch.ones(1, 2, 4, 3)
# 最后两个维度要可以进行矩阵运算
print(a.matmul(b).shape)

#pow
a = torch.tensor([1,2])
print(torch.pow(a, 3))
print(a.pow(3))
print(a**3)
print(a.pow_(3))
print(a)

#exp

a = torch.tensor([1,2], dtype=torch.float)
print(torch.exp(a))
print(torch.exp_(a))
print(a.exp())
print(a.exp_())

#log
a = torch.tensor([1,2], dtype=torch.float)
print(torch.log(a))


#sqrt

print(torch.sqrt(a))
print(torch.sqrt_(a))
