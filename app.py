from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model (ensure the model.pkl file exists or adjust accordingly)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome to the Flask App! Use the /predict endpoint to make predictions.'


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(pd.DataFrame([data]))
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
