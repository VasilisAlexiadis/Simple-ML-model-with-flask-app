from flask import Flask, request, jsonify
import pandas as pd
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to the Flask App! Use the /predict endpoint to make predictions.'

@app.route('/predict', methods=['GET'])
def predict():
    """
    This is the prediction API using URL parameters.
    ---
    parameters:
      - name: sepal_length
        in: query
        type: number
        required: true
      - name: sepal_width
        in: query
        type: number
        required: true
      - name: petal_length
        in: query
        type: number
        required: true
      - name: petal_width
        in: query
        type: number
        required: true
    responses:
      200:
        description: The output values
    """
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return 'Prediction is '+ str(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_file():
    """
    Predict from a file upload.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - in: formData
        name: file
        type: file
        required: true
    responses:
      200:
        description: The prediction list from the file
    """
    data = pd.read_csv(request.files.get('file'))
    prediction = model.predict(data)
    return 'Predictions for the uploaded CSV are: ' + str(list(prediction))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
