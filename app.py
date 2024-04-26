from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict(pd.DataFrame([data]))
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
