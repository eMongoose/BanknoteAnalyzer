import sys

import KNNmodel
import LCmodel

def imageAnalysis(model_type, image):
  print("your choice of model: ", model_type)
  print("image: ", image)
  
  # pass image path to wavelet transform function
  
  # save the processed data from the wavelet transform function
  X = [[3.2032,5.7588,-0.75345,-0.61251]]
  
  # pass the processed data through the selected model
  if model_type == 'KNN':
    print("You are predicting using K-Nearest Neighbors!")
    # TODO
    # save result
    
  if model_type == 'LC':
    print("You are predicting using Linear Classification!")
    LCmodel.lc_predict(X) # get X
    # save result
    
  # return classification result to the user (real or fake) with a confidence %

# =============================================================================
def predict(value):
  if value == 0:
    print("Your banknote is FAKE!")
    
  if value == 1:
    print("Your banknote is REAL!")
    
  return
# =============================================================================
def testImageAnalysis(model_type):
  X = [[3.2032,5.7588,-0.75345,-0.61251]]
  
  if model_type == 'LC':
    print("You are predicting using Linear Classification!")
    prediction = LCmodel.lc_predict(X) # get X
    # print(prediction)
    print(predict(prediction))
    
# =============================================================================
if __name__ == "__main__":
  model_type = sys.argv[1] 
  # image = sys.argv[2]

  # imageAnalysis(model_type, image)
  testImageAnalysis(model_type)
  
  