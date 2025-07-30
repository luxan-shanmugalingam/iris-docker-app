from flask import Flask, request, jsonify, render_template_string
import pickle
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

# Load the model
with open("rf.pkl", "rb") as f:
    model = pickle.load(f)

# Home route with slider UI
@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Iris Flower Predictor</title>
        <style>
            label { display: block; margin-top: 10px; }
            input[type=range] { width: 300px; }
            #result { margin-top: 20px; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>Iris Flower Predictor</h1>
        
        <label>Sepal length: <span id="sepallength_val">5.0</span></label>
        <input type="range" id="sepallength" min="4" max="8" step="0.1" value="5.0" oninput="updateValue('sepallength')">

        <label>Sepal width: <span id="sepalwidth_val">3.0</span></label>
        <input type="range" id="sepalwidth" min="2" max="4.5" step="0.1" value="3.0" oninput="updateValue('sepalwidth')">

        <label>Petal length: <span id="petallength_val">1.0</span></label>
        <input type="range" id="petallength" min="1" max="7" step="0.1" value="1.0" oninput="updateValue('petallength')">

        <label>Petal width: <span id="petalwidth_val">0.1</span></label>
        <input type="range" id="petalwidth" min="0" max="2.5" step="0.1" value="0.1" oninput="updateValue('petalwidth')">

        <br>
        <button onclick="makePrediction()">Predict</button>

        <div id="result"></div>

        <script>
            function updateValue(id) {
                document.getElementById(id + "_val").innerText = document.getElementById(id).value;
            }

            function makePrediction() {
                const sl = document.getElementById('sepallength').value;
                const sw = document.getElementById('sepalwidth').value;
                const pl = document.getElementById('petallength').value;
                const pw = document.getElementById('petalwidth').value;

                fetch(`/predict?Sepal length=${sl}&Sepal width=${sw}&Petal length=${pl}&Petal width=${pw}`)
                .then(response => response.json())
                .then(data => {
                    if (data.prediction) {
                        document.getElementById('result').innerText = "Prediction: " + data.prediction;
                    } else if (data.error) {
                        document.getElementById('result').innerText = "Error: " + data.error;
                    }
                })
                .catch(error => {
                    document.getElementById('result').innerText = "Error: " + error;
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/predict', methods=["GET"])
@swag_from({
    'parameters': [
        {"name": "Sepal length", "in": "query", "type": "number", "required": True, "description": "Sepal length in cm"},
        {"name": "Sepal width",  "in": "query", "type": "number", "required": True, "description": "Sepal width in cm"},
        {"name": "Petal length", "in": "query", "type": "number", "required": True, "description": "Petal length in cm"},
        {"name": "Petal width",  "in": "query", "type": "number", "required": True, "description": "Petal width in cm"},
    ],
    'responses': {
        200: {
            'description': 'Prediction result',
            'examples': {'application/json': {'prediction': 'setosa'}}
        }
    }
})
def predict_class():
    try:
        sepal_length = float(request.args.get("Sepal length"))
        sepal_width = float(request.args.get("Sepal width"))
        petal_length = float(request.args.get("Petal length"))
        petal_width = float(request.args.get("Petal width"))

        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        species = prediction[0]

        return jsonify({'prediction': species})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
