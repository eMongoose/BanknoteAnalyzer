import torch
import torch.nn as nn

class CoinCNN(nn.Module):
    def __init__(self, num_classes=3): # 3 types of coins
        super(CoinCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3)
        self.conv2 = nn.Conv2d(32, 32, 3)
        self.max_pool1 = nn.MaxPool2d(2, 2)

        self.conv_layer3 = nn.Conv2d(32,64,3)
        self.conv_layer4 = nn.Conv2d(64,64,3)
        self.max_pool2 = nn.MaxPool2d(2,2)

        self.fc1 = nn.Linear(1600, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, num_classes)
        

    def forward(self, x):
        out = self.conv_layer1(x)
        out = self.conv_layer2(out)
        out = self.max_pool1(out)
        
        out = self.conv_layer3(out)
        out = self.conv_layer4(out)
        out = self.max_pool2(out)
                
        out = out.reshape(out.size(0), -1)
        
        out = self.fc1(out)
        out = self.relu1(out)
        return self.fc2(out)