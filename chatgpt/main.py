import torch as t
import torch.nn as nn
import torch.nn.functional as F
from tb import TransformerBlock
from multihead import MultiHeadAttention
from transformer import Transformer

input_dim = 10000
d_model = 512
num_heads = 8
num_layers = 6
ff_hidden_dim = 2048
output_dim = 10
dropout = 0.6

model = Transformer(input_dim, d_model, num_heads, num_layers, ff_hidden_dim, output_dim, dropout)
print(model)
