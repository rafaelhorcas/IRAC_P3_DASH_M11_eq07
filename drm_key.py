from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

@app.route("/getkey", methods=["POST"])
def get_key():
    user = request.json.get('user')

    if user == "irac":
     return jsonify({
            "keys": [
                {
                    "kty": "oct",
                    "kid": "oW5AK5BW43HzbTSKpiu3SQ",
                    "k": "hyN9IKGfWKdAwFaE5pm0qg"
                }
            ],
            "type": "temporary"
        })
    else:
        return jsonify({"error": "Unauthorized"}), 403
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
