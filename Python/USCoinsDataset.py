import os
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from torchvision.io import decode_image

def get_classmap(img_dir):
  """
    Arguments:
      img_dir (string): Path to root directory of images
    Returns:
      dictionary mapping classes to labels
      -> {a: 0, b: 1, c: 2}
  """
  classmap = {}
  for k in os.listdir(img_dir):
    if os.path.isdir(os.path.join(img_dir, k)):
      classmap[k] = len(classmap)
  return classmap

class USCoinsDataset(Dataset):
  def __init__(self, csv_file, img_dir, transform=None):
    """
      Arguments:
        csv_file (string): Path to csv annotations for dataset
        img_dir (string): Path to root directory of images
        transform (callable, optional): Transform function to apply to a 
    """
    self.img_anno = pd.read_csv(csv_file)
    self.img_dir = img_dir
    self.transform = transform
    self.classmap = get_classmap(img_dir)
    
  def __len__(self):
    return len(self.img_anno)
  
  def __getitem__(self, idx):
    img_path = os.path.join(self.img_dir, self.img_anno.iloc[idx, 0], self.img_anno.iloc[idx, 1])
    image = decode_image(img_path)
    # Derive label from image folder
    label = self.classmap[self.img_anno.iloc[idx, 0]]
    if self.transform:
      image = self.transform(image)
    return image, label