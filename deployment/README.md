# 🚀 Flask Web Application Deployment

This directory contains the Flask web application for the Smart Garbage Classification project.

## 📁 Files Overview

- **`app.py`** - Main Flask application with improved model (50 epochs)
- **`templates/index.html`** - Modern web interface with green theme
- **`utils.py`** - Helper functions for model loading and preprocessing
- **`requirements.txt`** - Python dependencies
- **`weights/`** - Directory for model weights (if using old model)

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access the Web App
Open your browser and go to: `http://localhost:5004`

## 🎯 Features

### Web Interface
- **Modern Design**: Green theme with glassmorphism effects
- **File Upload**: Upload images from your device
- **URL Prediction**: Test images from internet URLs
- **Real-time Results**: Instant predictions with confidence scores
- **Responsive**: Works on desktop and mobile devices

### Model Information
- **Model**: `improved_model_fixed.keras` (50 epochs)
- **Architecture**: Advanced CNN with BatchNorm + Dropout
- **Accuracy**: ~80-90% on test data
- **Input Size**: 300x300x3 RGB images
- **Classes**: 6 waste categories

## 🔧 Configuration

### Port Configuration
The app runs on port 5004 by default. To change:
```python
# In app.py, line 107
app.run(debug=True, host='0.0.0.0', port=5004)
```

### Model Path
The app loads the improved model from:
```python
# In app.py, line 16
model = load_model("../../improved_model_fixed.keras")
```

## 📊 API Endpoints

### 1. Home Page
- **URL**: `/`
- **Method**: GET
- **Description**: Serves the main web interface

### 2. File Upload Prediction
- **URL**: `/predict`
- **Method**: POST
- **Description**: Upload image file for classification
- **Response**: JSON with prediction results

### 3. URL Prediction
- **URL**: `/predict_url`
- **Method**: POST
- **Description**: Classify image from URL
- **Response**: JSON with prediction results

## 🧪 Testing the API

### Using curl
```bash
# Test file upload
curl -X POST -F "file=@test_image.jpg" http://localhost:5004/predict

# Test URL prediction
curl -X POST -H "Content-Type: application/json" \
     -d '{"url":"https://example.com/image.jpg"}' \
     http://localhost:5004/predict_url
```

### Using Python
```python
import requests

# Test file upload
with open('test_image.jpg', 'rb') as f:
    response = requests.post('http://localhost:5004/predict', 
                           files={'file': f})
    print(response.json())

# Test URL prediction
response = requests.post('http://localhost:5004/predict_url',
                        json={'url': 'https://example.com/image.jpg'})
print(response.json())
```

## 🐛 Troubleshooting

### Common Issues

1. **Model Loading Error**
   ```
   ValueError: File not found: improved_model_fixed.keras
   ```
   **Solution**: Ensure the model file exists in the correct path

2. **Port Already in Use**
   ```
   Address already in use
   ```
   **Solution**: Change the port in `app.py` or kill existing processes

3. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'tensorflow'
   ```
   **Solution**: Install dependencies with `pip install -r requirements.txt`

### Debug Mode
The app runs in debug mode by default. To disable:
```python
# In app.py, line 107
app.run(debug=False, host='0.0.0.0', port=5004)
```

## 🔒 Production Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5004 app:app
```

### Using Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5004

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5004", "app:app"]
```

### Environment Variables
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
export MODEL_PATH=../../improved_model_fixed.keras
```

## 📈 Performance Optimization

### Model Optimization
- Use TensorFlow Lite for mobile deployment
- Implement model quantization for smaller size
- Add caching for repeated predictions

### Web Optimization
- Enable gzip compression
- Use CDN for static assets
- Implement request caching

## 🔍 Monitoring

### Logging
The app includes basic logging. For production:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Health Check
Add a health check endpoint:
```python
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'model': 'loaded'})
```

## 📞 Support

For deployment issues:
1. Check the logs for error messages
2. Verify all dependencies are installed
3. Ensure model file exists and is accessible
4. Check port availability

---

**Happy Deploying! 🚀**