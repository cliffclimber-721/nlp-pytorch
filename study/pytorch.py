import torch
from torch import nn
from torch import optim

def torch_version():
    print(torch.__version__)

def torch_testing():
    # tensor = int, Tensor = float
    print(torch.tensor([1, 2, 3]))
    print(torch.Tensor([[1, 2, 3], [4, 5, 6]]))
    print(torch.LongTensor([1, 2, 3]))
    print(torch.FloatTensor([1, 2, 3]))

def torch_parameter_testing():
    x = torch.FloatTensor([
        [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]    
    ])
    y = torch.FloatTensor([
        [0.94], [1.98], [2.88], [3.96], [4.55], [5.64], [6.3], [7.44], [8.46], [9.1]
    ])

    model = nn.Linear(1, 1)
    print("Linear: ", model)
    criteria = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001)

    for epoch in range(10000):
        output = model(x)
        # x에 관해서 linear 모델을 실행하고 
        cost = criteria(output, y)

        # optim 패키지 사용할 때 zero.grad => backward => step 순서대로 호출해준다
        optimizer.zero_grad()
        # 값을 0으로 만들어준다
        cost.backward()
        # 역전파 단계 : 모델의 학습 가능한 모든 매개변수에 대해 손실 변화도를 계산
        optimizer.step()
        # 매개변수 갱신
        if (epoch + 1) % 1000 == 0:
            print(f"Epoch : {epoch+1:4d}, Model : {list(model.parameters())}, Cost : {cost:.3f}")

#torch_testing()
torch_parameter_testing()