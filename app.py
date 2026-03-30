import os
from flask import Flask, request, jsonify, render_template
from predict import make_prediction

app = Flask(__name__)

# Valid categories (matches your dataset + UI)
VALID_CATEGORIES = [
    "<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validate ocean_proximity
        if data.get("ocean_proximity") not in VALID_CATEGORIES:
            return jsonify({"error": "Invalid ocean_proximity value"})

        prediction = make_prediction(data)

        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})


# -----------------------
# Entry point for local or Render
# -----------------------
if __name__ == "__main__":
    # Render sets PORT automatically; default to 10000 for local testing
    port = int(os.environ.get("PORT", 10000))
    # Bind to all interfaces so Render can reach it
    app.run(host="0.0.0.0", port=port, debug=True)