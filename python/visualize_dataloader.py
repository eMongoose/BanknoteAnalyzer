import matplotlib.pyplot as plt
import numpy as np
from dataset.dataloader import load_data
from torchvision.utils import make_grid


train_set, test_set = load_data(4)
images, labels = next(iter(train_set))

def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

imshow(make_grid(images))
