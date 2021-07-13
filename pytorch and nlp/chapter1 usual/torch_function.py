import torch

class line(torch.autograd.Function):
    @staticmethod
    def forward(ctx, w, x, b):
        ctx.save_for_backward(w,x,b)
        return w*x+b
    @staticmethod
    def backward(ctx, grad_out):
        pass