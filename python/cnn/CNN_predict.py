import os

import torch
from PIL import Image

from ..dataset.dataloader import transform
from .CNN import CNN


def predict(img_path):
  local_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

  # Load model from memory
  model = CNN(3)
  model_path = os.path.join(os.path.dirname(__file__), '..', 'Models', 'CNN.torch')
  model_path = os.path.abspath(model_path)
  model.load_state_dict(torch.load(model_path, map_location=local_device))

  # Image needs to be reshaped to include batch info (1)
  # This is because model expects multiple images to be loaded
  image = Image.open(img_path)
  image = transform(image).reshape(-1, 3, 32, 32)
  image = image.to(local_device)

  # Predict on image
  with torch.no_grad():
    model.eval()

    output = model(image)
 
    prediction = torch.argmax(output.data).item()

    return prediction
