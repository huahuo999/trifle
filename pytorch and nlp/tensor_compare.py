import torch

a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)
print(torch.eq(a, b))
print(torch.equal(a, b))
print(torch.ge(a, b))
print(torch.gt(a, b))
print(torch.lt(a, b))

# sort

a = torch.tensor([1, 4, 4, 3, 5])
print(torch.sort(a, descending=True))

a = torch.tensor([[1, 4, 4, 3, 5],
                  [2, 4, 4, 3, 5]
                  ])
print(torch.sort(a, dim=1, descending=False))

# topk

a = torch.tensor([[1, 4, 4, 3, 5],
                  [2, 4, 4, 3, 5]
                  ])
print(a.shape)
print(torch.topk(a, k=1, dim=1))

# 最小值
print(torch.kthvalue(a, k=2, dim=0))

a = torch.rand(2, 3)
print(a)
print(torch.isfinite(a))
print(torch.isfinite(a / 0))
print(torch.isinf(a / 0))
print(torch.isnan(a))

import numpy as np

a = torch.tensor([1, 2, np.nan])
print(torch.isnan(a))
