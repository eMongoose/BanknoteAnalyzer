import torch
import os
from python.cnn.CNN import CNN
from PIL import Image

from python.dataset.dataloader import transform

def predict(img_path):
  local_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

  # Load model from memory
  model = CNN(3)
  model.load_state_dict(torch.load(os.path.join("python", "Models", "CNN.torch")))

  # Image needs to be reshaped to include batch info (1)
  # This is because model expects multiple images to be loaded
  image = Image.open(img_path)
  image = transform(image).reshape(-1, 3, 32, 32)
  image = image.to(local_device)

  # Predict on image
  with torch.no_grad():
    model.eval()

    output = model(image)
 
    prediction = torch.argmax(output.data).numpy()

    return prediction
