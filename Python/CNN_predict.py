import torch
import os
from CNN import CNN

from dataloader import transform, load_data

def predict(img):
  model = CNN(3)
  model.load_state_dict(torch.load(os.path.join("Python", "Models", "CNN.torch")))

  local_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

  train_loader, test_loader = load_data(64, debugging=True)

  with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images = images.to(local_device)
        labels = labels.to(local_device)
        outputs = model(images)
        print(outputs.data)
        print(outputs)
        _, predicted = torch.max(outputs.data, 1)
        print(_)
        print(predicted)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    print(f'Accuracy of the network on the train images: {100 * correct / total} %')

predict("a")
