from flask import Flask, jsonify, request
from flask_cors import CORS
from markupsafe import escape
from PIL import Image

from python.cnn.CNN_predict import predict

names = ["Nickel", "Penny", "Quarter"]
values = [0.05, 0.01, 0.25]

app = Flask(__name__)
CORS(app, resources={
  r"/getCoin": {"origins": ["https://banknote-analyzer-mdym.vercel.app"]}
})

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

@app.route("/getCoin", methods=['POST'])
def getCoin():
    # error handling
    if 'image' not in request.files:
      print("Error 1: Failed to receive image.")
      return jsonify({"error": "No image received"}), 400

    file = request.files['image']
    
    if file.filename == '':
      print("Error 2: Image name is invalid.")
      return jsonify({"error": "Empty filename"}), 400

    try:
        label = predict(file)
        data = {
            "name": names[label],
            "label": label,
            "value": values[label]
        }
        print(data)
        return jsonify(data)
    except Exception as e:
        print("Error 3:", str(e))
        return jsonify({"error": str(e)}), 500
      
  
if __name__ =="__main__":
  app.run(host="0.0.0.0", port=5000)
