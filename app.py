from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model (ensure the model.pkl file exists or adjust accordingly)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to the Flask App! Use the /predict endpoint to make predictions.'

@app.route('/predict')
def predict():
    sepal_length = request.args.get('sepal_length')
    sepal_width = request.args.get('sepal_width')
    petal_length = request.args.get('petal_length')
    petal_width = request.args.get('petal_width')
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return 'prediction is'+ str(prediction)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     prediction = model.predict(pd.DataFrame([data]))
#     return jsonify({'prediction': list(prediction)})

@app.route('/predict', methods=['POST'])
def predict_file():
    data = pd.read_csv(request.files.get('file'))
    prediction = model.predict(data) 
    return 'predictions for the csv is' + str(list(prediction))


if __name__ == '__main__':
    app.run(debug=True)
