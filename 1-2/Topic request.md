# MindSpore端边云统一格式 — MindIR

1-2训练一个ResNet50网络。使用训练好的checkpoint文件，导出MindIR格式模型

使用了ModelArts平台提供的Notebook来跑 8vCPU+64G+1 x Tesla V100-PCIE-32G

（1）数据集的准备，这里使用的是CIFAR-10数据集。

（2）构建一个卷积神经网络，这里使用ResNet-50网络。