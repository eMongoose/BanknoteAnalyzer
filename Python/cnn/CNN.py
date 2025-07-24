import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

class CNN(nn.Module):
    def __init__(self, num_classes):
        super(CNN, self).__init__()
        
        # applying 2D convolution
        # nn.Conv2d(in_channel, out_channel, kernel_size)
        # 3 since we are considering RGB and then as we create
        # more feature maps (32), as the model learns higher-level
        # features and finds more differentiating attributes
        # padding (default = 0): refers to addition of extra pixels around the edge of the input image
        # stride (default = 1): refers to the number of pixels each kernel moves across the image input 
        self.conv1 = nn.Conv2d(3, 32, 3) 

        # takes 32 inputs and creates 32 output channels by
        # applying 32 filters (since out_channel=32) of size 3x3 
        # allowing the model to pick up more abstract features
        self.conv2 = nn.Conv2d(32, 32, 3)
        
        # pooling layers (resizing image)
        # nn.MaxPool2d(kernel_size, stride)
        self.max_pool1 = nn.MaxPool2d(2, 2)

        # applying more 2D convolution
        self.conv3 = nn.Conv2d(32,64,3)
        self.conv4 = nn.Conv2d(64,64,3)
        
        # pooling layers (resizing image)
        self.max_pool2 = nn.MaxPool2d(2,2)

        # nn.Linear(in_feat, out_feat)
        # combining all the features extracted from convulutional 
        # layers (input size) into a vector (output size).
        self.fc1 = nn.Linear(1600, 128)

        # ReLU(inplace=False)
        # ReLU is a mathematical function which is applied and then the model
        # determines whether it should be activated
        self.relu = nn.ReLU()

        # combining the new activated layer and then determining
        # which class they should be part of (classification)
        self.fc2 = nn.Linear(128, num_classes)

    # function to pass the image through the CNN model
    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.max_pool1(out)
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.max_pool2(out)       
        out = out.reshape(out.size(0), -1) # built in PyTorch function to flatten features
        out = self.fc1(out)
        out = self.relu(out)
        return self.fc2(out)
