from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model AND THE SCALER
model = joblib.load("diabetes_predictor.pkl")
# FIX: Load the scaler as well
scaler = joblib.load("scaler.pkl") 

# Home route — show input form
@app.route('/')
def home():
    # Assuming 'index.html' is your form with 8 input fields
    return render_template('index.html')

# Prediction route — handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form (as a list of 8 floats)
        # Note: This assumes the form fields are submitted in the correct order!
        features = [float(x) for x in request.form.values()]
        input_data = np.array([features])

        # FIX: Scale the input data BEFORE making the prediction
        scaled_input = scaler.transform(input_data)

        # Make prediction on the SCALED data
        prediction = model.predict(scaled_input)[0]

        # Interpret result
        result = "⚠️ The person is likely Diabetic." if prediction == 1 else "✅ The person is likely Non-Diabetic."

        return render_template('result.html', result=result)
    except Exception as e:
        # A more helpful error message for debugging
        return render_template('result.html', result=f"An error occurred during prediction: {e}. Check your logs and input feature order.")

# Run the app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

