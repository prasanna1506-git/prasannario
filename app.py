from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app)

# Dummy detection logic (NO MODEL NEEDED NOW)
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]
    img = Image.open(file).convert("RGB")

    # Simple rule-based demo output
    width, height = img.size
    pixels = np.array(img)

    if pixels.std() < 40:
        result = "AI Generated Image"
        confidence = 85.0
    else:
        result = "Real Image"
        confidence = 90.0

    return jsonify({
        "result": result,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)
