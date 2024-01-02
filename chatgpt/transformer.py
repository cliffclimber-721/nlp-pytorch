import torch as t
import torch.nn as nn
import torch.nn.functional as F
from tb import TransformerBlock

class Transformer(nn.Module):
    def __init__(self, input_dim, d_model, num_heads, num_layers, ff_hidden_dim, output_dim, dropout=0.1):
        super(Transformer, self).__init__()
        self.embedding = nn.Embedding(input_dim, d_model)
        self.transformer_block = nn.ModuleList(
            [TransformerBlock(d_model, num_heads, ff_hidden_dim, dropout)
            for _ in range(num_layers)]
        )
        self.fc_out = nn.Linear(d_model, output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        x = self.embedding(x)
        for tb in self.transformer_block:
            x = tb(x, mask)
        x = x.mean(dim=1)
        x = self.fc_out(x)
        return x