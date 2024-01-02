import math
import torch
from torch import nn
from matplotlib import pyplot as plt

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        pos = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
            # 0을 시작으로 해서 d_model에서 끝내는데, 2 간격을 주고 d_model까지 함수를 사용한다는 뜻이다.
            # exp는 자연상수 e인 지수함수로 변환해준다는 뜻
            # => exp 괄호에 있는 값이 나오면 그 값에 대해서 계산을 하고 그 값 도출은 지수함수를 통해서 계산해서 알려주는 것이다.
            # ex) e^0 = 1 e^1 = 2.71, 0이랑 1이 torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model) 값을 의미
        

        pe = torch.zeros(max_len, 1, d_model)
        # zeros() => 0으로 가득 찬 array를 출력
        # 0으로 구성된 max_len * 1 * d_model array 를 출력
        pe[:, 0, 0::2] = torch.sin(pos * div_term)
        pe[:, 0, 1::2] = torch.cos(pos * div_term)
        pe.numpy()
        self.register_buffer("pe :", pe)
    
    def forward(self, x):
        x = x + self.pe[:, x.size(0)]
        return self.dropout(x)
        

encoding = PositionalEncoding(d_model=128, max_len=50)
graph = encoding.pe.numpy()

plt.pcolormesh(graph.squeeze(), cmap="RdBu")
plt.xlabel("Embedding Dimension")
plt.xlim((0, 128))
plt.ylabel("Position")
plt.colorbar()
plt.show()