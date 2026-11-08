import torch

def matrixmul(a, b) -> torch.Tensor:
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    if a_t.ndim != 2 or b_t.ndim != 2 or a_t.size(1) != b_t.size(0):
        return torch.tensor(-1)
    return a_t @ b_t 
