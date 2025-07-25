from flask import Flask, jsonify, request
from markupsafe import escape
from PIL import Image

from python.cnn.CNN_predict import predict

names = ["Nickel", "Penny", "Quarter"]
values = [0.05, 0.01, 0.25]

app = Flask(__name__, static_folder="../app", static_url_path="/")

@app.route("/")
def index():
  return "Server Active"

# @app.route("/img/<path:img_data>", methods=['GET', 'POST'])
# def img(img_data):
#   label = predict(img_data)
#   data = {
#     "name": names[label],
#     "label": label,
#     "value": values[label]
#   }

#   return data

@app.post("/getCoin")
def getCoin(img_data):
    # error handling
    if 'image' not in request.files:
      print("Error 1: Failed to receive image.")
      return

    file = request.files['image']
    
    if file.filename == '':
      print("Error 2: Image name is invalid.")
      return

    image = Image.open(file)
    label = predict(image)
    
    data = {
        "name": names[label],
        "label": label,
        "value": values[label],
    }
    return data
  
if __name__ =="__main__":
  app.run()