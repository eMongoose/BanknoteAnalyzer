import sys

import KNNmodel

# the function
def imageAnalysis(model_type, image):
  print("your choice of model: ", model_type)
  print("image: ", image)
  
  
  # pass image path to wavelet transform function
  
  # save the processed data from the wavelet transform function
  
  # pass the processed data through the selected model
  if model_type == 'KNN':
    # TODO
    print("do something")
  
  # save result
  
  # return classification result to the user (real or fake) with a confidence %


# joe
if __name__ == "__main__":
  model_type = sys.argv[1] 
  image = sys.argv[2]

  imageAnalysis(model_type, image)
  