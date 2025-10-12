# 🗑️ Smart Garbage Classification Project

A comprehensive machine learning project for automatic waste classification using Convolutional Neural Networks (CNN) with Flask web deployment.

## 📊 Project Overview

This project implements a deep learning solution to classify waste materials into 6 categories:
- **Cardboard** 📦
- **Glass** 🍷
- **Metal** ⚙️
- **Paper** 📄
- **Plastic** 🥤
- **Trash** 🗑️

## 🎯 Key Features

- **Advanced CNN Architecture** with Batch Normalization and Dropout
- **Data Augmentation** for improved model generalization
- **Early Stopping** and Learning Rate Reduction
- **Flask Web Application** with modern UI
- **Model Comparison** tools
- **Comprehensive Testing** with both local and internet images

## 📁 Project Structure

```
Smart-Garbage-Classification-Project/
├── 📓 notebooks/
│   └── smart_garbage.ipynb          # Main training and testing notebook
├── 🚀 deployment/
│   ├── app.py                       # Flask web application
│   ├── templates/
│   │   └── index.html              # Web interface
│   ├── utils.py                    # Helper functions
│   ├── requirements.txt            # Python dependencies
│   └── README.md                   # Deployment instructions
├── 🤖 models/
│   └── improved_model_fixed.keras  # Trained model (50 epochs)
├── 📊 data/
│   ├── Train/                      # Training images (6 classes)
│   └── Test/                       # Test images (6 classes)
├── 📚 docs/
│   └── (documentation files)
└── 📋 scripts/
    └── (utility scripts)
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Smart-Garbage-Classification-Project.git
cd Smart-Garbage-Classification-Project
```

### 2. Install Dependencies
```bash
pip install -r deployment/requirements.txt
```

### 3. Run the Web Application
```bash
cd deployment
python app.py
```

### 4. Access the Application
Open your browser and go to: `http://localhost:5004`

## 🧪 Model Performance

### Model Comparison

| Model | Epochs | Architecture | Accuracy | File Size |
|-------|--------|--------------|----------|-----------|
| **Basic Model** | 10 | Simple CNN | ~60-70% | 33 MB |
| **Improved Model** | 50 | Advanced CNN + BatchNorm + Dropout | ~80-90% | 196 MB |

### Training Features
- ✅ **Data Augmentation**: Rotation, flip, zoom, shear
- ✅ **Early Stopping**: Prevents overfitting
- ✅ **Learning Rate Reduction**: Adaptive learning
- ✅ **Model Checkpointing**: Saves best model
- ✅ **Validation Split**: 20% for validation

## 📱 Web Application Features

### 🎨 Modern UI Design
- **Green Theme** with glassmorphism effects
- **Responsive Design** for all devices
- **Animated Backgrounds** and smooth transitions
- **Real-time Predictions** with confidence scores

### 🔧 Functionality
- **File Upload**: Upload images from your device
- **URL Prediction**: Test images from internet URLs
- **Confidence Scores**: See prediction confidence
- **Visual Results**: Display images with predictions

## 🧪 Testing the Model

### Notebook Testing
The `smart_garbage.ipynb` notebook includes comprehensive testing:

1. **Cell 47**: Test with actual dataset images
2. **Cell 48**: Test with internet images
3. **Cell 49**: Quick individual image testing
4. **Cell 50**: Model comparison (old vs new)

### Example Usage
```python
# Test local image
test_local_image('data/Test/paper/paper1.jpg')

# Test internet image
test_internet_image('https://example.com/image.jpg')
```

## 🛠️ Technical Details

### Model Architecture
```python
# Advanced CNN with regularization
- Conv2D layers with BatchNormalization
- MaxPooling2D for downsampling
- Dropout layers (0.5, 0.3) for regularization
- Dense layers (512, 256 neurons)
- Softmax output (6 classes)
```

### Training Configuration
```python
# Optimized training setup
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy
- Batch Size: 32
- Image Size: 300x300x3
- Data Augmentation: Yes
- Early Stopping: Yes (patience=15)
```

## 📊 Dataset Information

- **Total Images**: 2,186 training images
- **Classes**: 6 waste categories
- **Image Format**: JPG/PNG
- **Resolution**: Variable (resized to 300x300)
- **Split**: 80% training, 20% testing

## 🔧 Dependencies

### Core Libraries
- **TensorFlow/Keras**: Deep learning framework
- **Flask**: Web application framework
- **PIL/Pillow**: Image processing
- **NumPy**: Numerical computing
- **Matplotlib**: Visualization

### Full Requirements
```
Flask==2.3.3
tensorflow==2.13.0
Pillow==10.0.0
numpy==1.24.3
matplotlib==3.7.2
requests==2.31.0
```

## 🚀 Deployment Options

### Local Deployment
```bash
cd deployment
python app.py
# Access at http://localhost:5004
```

### Production Deployment
- Use Gunicorn or uWSGI for production
- Configure reverse proxy (Nginx)
- Set up SSL certificates
- Use environment variables for configuration

## 📈 Performance Metrics

### Training Results
- **Training Accuracy**: ~95%
- **Validation Accuracy**: ~85%
- **Test Accuracy**: ~80-90%
- **Training Time**: ~2-3 hours (50 epochs)
- **Model Size**: 196 MB

### Inference Speed
- **Prediction Time**: ~50ms per image
- **Memory Usage**: ~500MB RAM
- **GPU Support**: CUDA compatible

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Simon Uddin**
- GitHub: [@Simonuddin11](https://github.com/SimonUddin11)
- Email: Simon.uddin@student.uts.edu.au

## 🙏 Acknowledgments

- Original dataset from [Smart Garbage Segregation](https://github.com/raison024/Smart-Garbage-Segregation)
- TensorFlow/Keras community for excellent documentation
- Flask community for web framework

## 📞 Support

If you have any questions or need help, please:
1. Check the [Issues](https://github.com/SimonUddin11/Smart-Garbage-Classification-Project/issues) page
2. Create a new issue with detailed description
3. Contact the author directly

---

⭐ **Star this repository if you found it helpful!**
