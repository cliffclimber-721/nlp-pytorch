import torch as t
import torch.nn as nn
import torch.nn.functional as F

from multihead import MultiHeadAttention

class TransformerBlock(nn.Module):
    def __init__(self, d_model, num_heads, ff_hidden_dim, dropout=0.1):
        super(TransformerBlock, self).__init__()
        self.attention = MultiHeadAttention(d_model, num_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, ff_hidden_dim),
            nn.ReLU(),
            nn.Linear(ff_hidden_dim, d_model)
        )
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        attention_output = self.attention(x, x, x, mask)
        x = self.norm1(x + attention_output)
        ffn_output = self.ffn(x)
        x = self.norm2(x + ffn_output)
        x = self.dropout(x)
        return x