import os
from torch.utils.data import Dataset
from torchvision import datasets, transforms
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader, random_split, Subset
from torch import randperm

from USCoinsDataset import USCoinsDataset

BATCH_SIZE = 64
NUM_WORKERS = 0 # Investigate RunTimeError when increasing this value

transform = transforms.Compose([
  transforms.Resize((32,32)),
  transforms.ToTensor(),
  transforms.Normalize((0.5, 0.5, 0.5),(0.5, 0.5, 0.5))
])

def load_data(batch_size = 32, num_workers = 0, debugging = False):
  '''
  Arguments:
    batch_size (Integer): size of each batch of images
    num_workers (Integer): number of concurrentprocesses to run
    debugging (Bool): reduce dataset training time to test other functionalities
  Returns:
    tuple (Dataloader): train_set and test_set
  '''
  csv_file = os.path.join("Dataset", "dataset.csv")
  img_dir = os.path.join("Dataset", "coins")
  dataset = USCoinsDataset(csv_file, img_dir, transform)
  
  if debugging == True:
    idx = randperm(len(dataset))[:150]
    print(idx.numpy())
    dataset = Subset(dataset, idx.numpy())

    train_set, test_set = random_split(dataset, [120, 30]) # 4:1 split
  else:
    train_set, test_set = random_split(dataset, [3000, 749]) # roughly 4:1 split

  train_set = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=num_workers)
  test_set = DataLoader(test_set, batch_size=batch_size, shuffle=True, num_workers=num_workers)

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