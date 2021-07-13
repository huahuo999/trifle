import torch

dev = torch.device('cpu')
dev = torch.device('cuda:0')
a = torch.tensor([2, 2], device=dev, dtype=torch.float32)
print(a)

i = torch.tensor([[0, 1, 2], [0, 1, 2]])
# 坐标 0,0 1,1 2,2
v = torch.tensor([1, 2, 3])
a = torch.sparse_coo_tensor(i, v, (4, 4), dtype=torch.float32).to_dense()
print(a)
#稀疏元素
