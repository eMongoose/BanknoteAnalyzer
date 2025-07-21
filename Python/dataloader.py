import os
from torch.utils.data import Dataset
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader, random_split

from USCoinsDataset import USCoinsDataset

BATCH_SIZE = 64
NUM_WORKERS = 0 # Investigate RunTimeError when increasing this value

transform = transforms.Compose([
  transforms.Resize((32,32)),
  transforms.ToTensor(),
  transforms.Normalize((0.5, 0.5, 0.5),(0.5, 0.5, 0.5))
])

def load_data():
  '''
  Returns:
    train_set (Dataloader): training set
    test_set (DataLoader): test set
  '''
  csv_file = os.path.join("Dataset", "dataset.csv")
  img_dir = os.path.join("Dataset", "coins")
  dataset = USCoinsDataset(csv_file, img_dir, transform)

  train_set, test_set = random_split(dataset, [3000, 749]) # roughly 4:1 split

  train_set = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)
  test_set = DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)

  return train_set, test_set

# test code, remove later
def test_load_data():
  csv_file = os.path.join("Dataset", "dataset.csv")
  img_dir = os.path.join("Dataset", "coins")
  dataset = USCoinsDataset(csv_file, img_dir, transform)

  print(f"Loaded {len(dataset)} samples to the dataset")

  dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=NUM_WORKERS)

  for batch in dataloader:
    images, labels = batch
    print(f"Batch size: {images.shape}, Labels: {labels.shape}")