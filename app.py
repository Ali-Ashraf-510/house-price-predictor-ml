from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Load the saved model and scaler with error handling
try:
    model = joblib.load('linear_regression_model_no_outliers.pkl')
    scaler = joblib.load('scaler.pkl')
    model_loaded = True
    print("✅ Models loaded successfully!")
except FileNotFoundError as e:
    print(f"❌ Error loading models: {e}")
    print("Please run the notebook first to generate the model files.")
    model_loaded = False

# Feature names (excluding 'Address' and 'Price')
feature_names = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                'Avg. Area Number of Bedrooms', 'Area Population']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model_loaded:
        return render_template('index.html', 
                             prediction_text='❌ Error: Model not loaded. Please run the notebook first.')
    
    try:
        # Get data from form and validate
        features = []
        input_values = {}
        
        for feature in feature_names:
            value = request.form.get(feature)
            if value is None or value == '':
                return render_template('index.html', 
                                     prediction_text='❌ Error: Please fill in all fields.')
            
            try:
                float_value = float(value)
                if float_value < 0:
                    return render_template('index.html', 
                                         prediction_text=f'❌ Error: {feature} cannot be negative.')
                features.append(float_value)
                input_values[feature] = float_value
            except ValueError:
                return render_template('index.html', 
                                     prediction_text=f'❌ Error: Invalid value for {feature}.')
        
        # Additional validation
        if features[0] < 10000:  # Income too low
            return render_template('index.html', 
                                 prediction_text='⚠️ Warning: Income seems unusually low. Please check your input.',
                                 input_values=input_values)
        
        # Convert to numpy array and reshape
        input_data = np.array(features).reshape(1, -1)
        
        # Scale the input data
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        predicted_price = prediction[0]
        
        # Format prediction with better styling
        if predicted_price > 1000000:
            formatted_price = f'${predicted_price/1000000:.2f}M'
        else:
            formatted_price = f'${predicted_price:,.0f}'
        
        prediction_text = f'🏠 Predicted House Price: {formatted_price}'
        
        # Log prediction (optional)
        log_prediction(input_values, predicted_price)
        
        return render_template('index.html', 
                             prediction_text=prediction_text,
                             input_values=input_values)
    
    except Exception as e:
        return render_template('index.html', 
                             prediction_text=f'❌ Error: {str(e)}')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    if not model_loaded:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        # Get JSON data
        data = request.get_json()
        
        # Extract and validate features
        features = []
        for feature in feature_names:
            if feature not in data:
                return jsonify({'error': f'Missing feature: {feature}'}), 400
            
            value = data[feature]
            if not isinstance(value, (int, float)) or value < 0:
                return jsonify({'error': f'Invalid value for {feature}'}), 400
            
            features.append(value)
        
        # Convert to numpy array and reshape
        input_data = np.array(features).reshape(1, -1)
        
        # Scale the input data
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        predicted_price = float(prediction[0])
        
        # Format prediction
        if predicted_price > 1000000:
            formatted_price = f'${predicted_price/1000000:.2f}M'
        else:
            formatted_price = f'${predicted_price:,.0f}'
        
        return jsonify({
            'prediction': predicted_price,
            'formatted_prediction': formatted_price,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def log_prediction(input_values, prediction):
    """Log predictions for monitoring (optional)"""
    try:
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'input': input_values,
            'prediction': float(prediction)
        }
        # You could save this to a database or file for monitoring
        print(f"📝 Prediction logged: ${prediction:,.0f}")
    except Exception as e:
        print(f"Warning: Could not log prediction: {e}")

@app.errorhandler(404)
def not_found(error):
    return render_template('index.html', 
                         prediction_text='❌ Error: Page not found.'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('index.html', 
                         prediction_text='❌ Error: Internal server error.'), 500

if __name__ == '__main__':
    print("🚀 Starting House Price Predictor...")
    print(f"📍 Access the app at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
