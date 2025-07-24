from ..dataset.dataloader import load_data
import torch
from torch.optim import SGD
import torch.nn as nn
from .CNN import CNN
import os

def train_CNN(epochs = 20, learning_rate = 0.001, debugging = False):
  local_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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

  print("Beginning testing")
  with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = images.to(local_device)
        labels = labels.to(local_device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    print(f'Accuracy of the network on the train images: {100 * correct / total} %')

  print("Saving model to /python/Models/")
  torch.save(model.state_dict(), os.path.join("python", "Models", "CNN.torch"))