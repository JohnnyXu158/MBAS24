#build your own model.


import torch
from torch import nn
import torch.nn.functional as F

class ABCNet(nn.Module):
    def __init__(self):
        super(ABCNet, self).__init__()
        self.conv1 = nn.Conv3d(1, 16, 3, 1, 1, 1)

    def forward(self, x):
        out = self.conv1(x)
        return out
