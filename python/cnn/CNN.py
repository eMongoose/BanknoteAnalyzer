import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self, num_classes: int, channels = (64, 128, 256), dropout = 0.5):
        super(CNN, self).__init__()

        # assigning channel sizes for each stage of the network
        c1, c2, c3 = channels 

        # nn.sequential chains layers in the order given
        # each layer applies conv, BN, and ReLU
        # convolutional layers identify spatial filters (edges, textures, shapes)
        # padding = 1 is used to maintain spatial size of inputs before pooling
        # BN stabilizes training by adjusting the inputs and speeds up training
        # ReLU is a non-linear activation function (helps network learn more compelx patterns)
        # max pooling condenses information by halving the spatial dimensions
        # total of 11 trainable layers, 5 conv, 5 bn, 1 linear

        self.features = nn.Sequential(
            nn.Conv2d(3, c1, 3, padding = 1), nn.BatchNorm2d(c1), nn.ReLU(),
            nn.Conv2d(c1, c1, 3, padding = 1), nn.BatchNorm2d(c1), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(c1, c2, 3, padding = 1), nn.BatchNorm2d(c2), nn.ReLU(),
            nn.Conv2d(c2, c2, 3, padding = 1), nn.BatchNorm2d(c2), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(c2, c3, 3, padding = 1), nn.BatchNorm2d(c3), nn.ReLU(),
            nn.MaxPool2d(2)
        )
        # AdaptiveAvgPool averages each channel map so output  size is (c3, 1, 1)
        self.gap = nn.AdaptiveAvgPool2d(1)
        
        # dropout randomly zeroes features for to reduce overfitting (for training)
        self.dropout = nn.Dropout(dropout)

        # linear maps c3 features to class scores (logits) guiding the prediction
        self.classify = nn.Linear(c3, num_classes)
        
    # forward pass dataset through model
    def forward(self, x):
        
        # passes images through the feature extracts (trainable layers)
        x = self.features(x)
        
        # gloabl average pooling flattens output size to (batch_size, c3)
        x = self.gap(x).flatten(1)
        
        # dropout to reduce overfitting the model to training dataset (for training)
        x = self.dropout(x)
        
        # returns raw scores for each class
        return self.classify(x)
