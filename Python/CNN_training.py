from dataloader import load_data
from torch import device, cuda
from torch.optim import SGD
import torch.nn as nn
from CNN import CNN

def train_CNN(epochs = 20, learning_rate = 0.001, debugging = False):
  local_device = device('cuda' if cuda.is_available() else 'cpu')

  train_loader, test_loader = load_data(64, debugging=debugging)
  print("Data loaded")

  model = CNN(3)
  loss_function = nn.CrossEntropyLoss()

  optimizer = SGD(model.parameters(), lr=learning_rate, weight_decay = 0.005, momentum = 0.9)
  total_step = len(train_loader)

  print("Beginning training")
  for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
      images = images.to(local_device)
      labels = labels.to(local_device)

      # forward pass
      outputs = model(images)
      loss = loss_function(outputs, labels)

      # backward pass
      optimizer.zero_grad()
      loss.backward()
      optimizer.step()
    
    print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')

train_CNN(debugging = True)