import torch as t
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.head_dim = d_model // num_heads
        
        self.query = nn.Linear(d_model, d_model)
        self.key = nn.Linear(d_model, d_model)
        self.value = nn.Linear(d_model, d_model)
        self.fc_out = nn.Linear(d_model, d_model)
    
    def forward(self, q, k, v, mask):
        q = self.query(q)
        k = self.key(k)
        v = self.value(v)

        q = q.view(q.size(0), -1, self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        k = k.view(k.size(0), -1, self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        v = v.view(v.size(0), -1, self.num_heads, self.head_dim).permute(0, 2, 1, 3)
         
        energy = t.matmul(q, k.permute(0, 1, 3, 2)) / t.sqrt(t.tensor(self.head_dim, dtype=t.float32))

        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))
        
        attention = F.softmax(energy, dim=-1)

        x = t.matmul(attention, v)

        x = x.permute(0, 2, 1, 3).contiguous()
        x = x.view(x.sixe(0), -1, self.d_model)

        x = self.fc_out(x)
        return x
    
