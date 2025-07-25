import sys

from python.cnn.CNN_predict import predict

names = ["Nickel", "Penny", "Quarter"]
values = [0.05, 0.01, 0.25]

def imageAnalysis(img_path):
  print(">>> Your selected image: ", img_path)
    
  x = predict(img_path)

  print(f"The model predicts that your coin is a {names[x]} that has value ${values[x]}, with return label [{x}]")
    
# =============================================================================
if __name__ == "__main__":
  img_path = sys.argv[1] 

  imageAnalysis(img_path)