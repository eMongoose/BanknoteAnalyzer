import sys

# the function
def imageAnalysis(model_type, image):
  print("your choice of model: ", model_type)
  print("image: ", image)

if __name__ == "__main__":
  model_type = sys.argv[1]
  image = sys.argv[2]

  imageAnalysis(model_type, image)
  