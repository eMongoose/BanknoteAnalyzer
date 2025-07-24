from flask import Flask
from markupsafe import escape

app = Flask(__name__)

obj = {
  "name": "lincoln coin",
  "label": 1
}
obj2 = {
  "name": "washington coin",
  "label": 2
}

swit = {
  "asd": obj,
  "asb": obj2
}

@app.route("/img/<img_data>")
def img(img_data):
  return f'Image data: {swit[escape(img_data)]}'