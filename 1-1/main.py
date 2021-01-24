import time
import mindspore.nn as nn
from datetime import datetime
from mindspore.common.initializer import Normal

import numpy as np
from mindspore.train.serialization import export, load_checkpoint, load_param_into_net
from mindspore import Tensor

class LeNet5(nn.Cell):
    """Lenet network structure."""
    # define the operator required
    def __init__(self, num_class=10, num_channel=1):
        super(LeNet5, self).__init__()
        self.conv1 = nn.Conv2d(num_channel, 6, 5, pad_mode='valid')
        self.conv2 = nn.Conv2d(6, 16, 5, pad_mode='valid')
        self.fc1 = nn.Dense(16 * 5 * 5, 120, weight_init=Normal(0.02))
        self.fc2 = nn.Dense(120, 84, weight_init=Normal(0.02))
        self.fc3 = nn.Dense(84, num_class, weight_init=Normal(0.02))
        self.relu = nn.ReLU()
        self.max_pool2d = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = nn.Flatten()

    # use the preceding operators to construct networks
    def construct(self, x):
        x = self.max_pool2d(self.relu(self.conv1(x)))
        x = self.max_pool2d(self.relu(self.conv2(x)))
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x) 
        return x

lenet = LeNet5()
# 返回模型的参数字典
param_dict = load_checkpoint("./lenet.ckpt")
# 加载参数到网络
load_param_into_net(lenet, param_dict)
input = np.random.uniform(0.0, 1.0, size=[32, 1, 32, 32]).astype(np.float32)
# 以指定的名称和格式导出文件
export(lenet, Tensor(input), file_name='lenet.mindir', file_format='MINDIR',)

t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(" ")
print("============== Model conversion succeeded ==============")
print(t)