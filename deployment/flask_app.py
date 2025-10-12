from flask import Flask, request, render_template, jsonify
import numpy as np
from PIL import Image
import io
import base64
from utils import model_arc, preprocess, gen_labels
import os

app = Flask(__name__)

# Load labels
labels = gen_labels()

# Load model
model = model_arc()
model.load_weights("./weights/modelnew.h5")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the uploaded file
        file = request.files['file']
        
        if file is None:
            return jsonify({'error': 'No file uploaded'})
        
        # Read and preprocess the image
        image = Image.open(io.BytesIO(file.read()))
        
        # Preprocess the image
        processed_img = preprocess(image)
        
        # Make prediction
        prediction = model.predict(processed_img[np.newaxis, ...])
        
        # Get the predicted class and confidence
        predicted_class_idx = np.argmax(prediction[0], axis=-1)
        predicted_class = labels[predicted_class_idx]
        confidence = float(np.max(prediction[0], axis=-1))
        
        # Get all class probabilities
        class_probabilities = {}
        for i, prob in enumerate(prediction[0]):
            class_probabilities[labels[i]] = float(prob)
        
        # Convert image to base64 for display
        img_buffer = io.BytesIO()
        image.save(img_buffer, format='PNG')
        img_str = base64.b64encode(img_buffer.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'predicted_class': predicted_class,
            'confidence': confidence,
            'class_probabilities': class_probabilities,
            'image': img_str
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predict_url', methods=['POST'])
def predict_url():
    try:
        data = request.get_json()
        image_url = data.get('url')
        
        if not image_url:
            return jsonify({'error': 'No URL provided'})
        
        # Download and process image from URL
        import urllib.request
        with urllib.request.urlopen(image_url) as response:
            image_data = response.read()
        
        image = Image.open(io.BytesIO(image_data))
        
        # Preprocess the image
        processed_img = preprocess(image)
        
        # Make prediction
        prediction = model.predict(processed_img[np.newaxis, ...])
        
        # Get the predicted class and confidence
        predicted_class_idx = np.argmax(prediction[0], axis=-1)
        predicted_class = labels[predicted_class_idx]
        confidence = float(np.max(prediction[0], axis=-1))
        
        # Get all class probabilities
        class_probabilities = {}
        for i, prob in enumerate(prediction[0]):
            class_probabilities[labels[i]] = float(prob)
        
        # Convert image to base64 for display
        img_buffer = io.BytesIO()
        image.save(img_buffer, format='PNG')
        img_str = base64.b64encode(img_buffer.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'predicted_class': predicted_class,
            'confidence': confidence,
            'class_probabilities': class_probabilities,
            'image': img_str
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
