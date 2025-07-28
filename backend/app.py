from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="../app", static_url_path="/")

@app.route('/getCoin', methods = ["GET"])
def getCoin():
    if request.method == 'GET':
        data = {
            "name": "cameron",
            "currency": "CAD",
            "value": 0.25
        }
        return jsonify(data)

if __name__ =="__main__":
    app.run()