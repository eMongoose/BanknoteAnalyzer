from flask import Flask, jsonify
from markupsafe import escape
from python.cnn.CNN_predict import predict

names = ["Nickel", "Penny", "Quarter"]
values = [0.05, 0.01, 0.25]

app = Flask(__name__)

@app.route("/img/<path:img_data>")
def img(img_data):
  label = predict(img_data)
  data = {
    "name": names[label],
    "label": label,
    "value": values[label]
  }

  return data