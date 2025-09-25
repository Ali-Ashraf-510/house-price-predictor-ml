# 🏠 House Price Predictor

An AI-powered web application that predicts house prices using machine learning. Built with Python, Flask, and scikit-learn.

![House Price Predictor](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [API Documentation](#api-documentation)
- [Test Cases](#test-cases)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a linear regression model to predict house prices based on key features like area income, house age, number of rooms, bedrooms, and population. The model is trained on the USA Housing dataset and deployed as a user-friendly web application.

### Key Features:
- **High Accuracy**: R² score of ~0.92 after outlier removal
- **Real-time Predictions**: Instant price estimates via web interface
- **RESTful API**: JSON API for programmatic access
- **Responsive Design**: Modern UI that works on all devices
- **Input Validation**: Comprehensive error handling and data validation

## 🚀 Features

- ✅ **Machine Learning Model**: Linear regression with feature scaling
- ✅ **Web Interface**: Beautiful, responsive HTML interface
- ✅ **REST API**: JSON API for integration
- ✅ **Data Preprocessing**: Outlier removal and feature scaling
- ✅ **Input Validation**: Client and server-side validation
- ✅ **Error Handling**: Comprehensive error management
- ✅ **Model Persistence**: Saved models for quick loading

## 📁 Project Structure

```
Linear Regression/3/
├── 📊 notebook.ipynb              # Jupyter notebook with EDA and model training
├── 🌐 app.py                      # Flask web application
├── 📁 templates/
│   └── 🎨 index.html             # HTML template
├── 🤖 linear_regression_model.pkl # Trained model (with outliers)
├── 🎯 linear_regression_model_no_outliers.pkl # Optimized model
├── ⚙️ scaler.pkl                 # Feature scaler
├── 📋 requirements.txt           # Python dependencies
├── 📖 README.md                  # Project documentation
└── 📊 USA_Housing.csv            # Dataset
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd "Linear Regression/3"
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Train the Model
Run the Jupyter notebook to generate the model files:
```bash
jupyter notebook notebook.ipynb
```
Or run all cells in the notebook to generate:
- `linear_regression_model.pkl`
- `linear_regression_model_no_outliers.pkl`
- `scaler.pkl`

## 🎮 Usage

### Running the Web Application

1. **Start the Flask server:**
```bash
python app.py
```

2. **Access the application:**
Open your browser and go to `http://localhost:5000`

3. **Make predictions:**
Fill in the form with house features and click "Predict House Price"

### Using the REST API

**Endpoint:** `POST /api/predict`

**Request Body:**
```json
{
    "Avg. Area Income": 68000.00,
    "Avg. Area House Age": 6.5,
    "Avg. Area Number of Rooms": 7.2,
    "Avg. Area Number of Bedrooms": 4.1,
    "Area Population": 35000.0
}
```

**Response:**
```json
{
    "prediction": 1248725.50,
    "formatted_prediction": "$1,248,726",
    "timestamp": "2024-01-15T14:30:00.000Z"
}
```

**Example using curl:**
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Avg. Area Income": 68000,
    "Avg. Area House Age": 6.5,
    "Avg. Area Number of Rooms": 7.2,
    "Avg. Area Number of Bedrooms": 4.1,
    "Area Population": 35000
  }'
```

## 📈 Model Performance

### Dataset Information
- **Size**: 5,000 samples
- **Features**: 5 numerical features
- **Target**: House prices in USD

### Model Metrics
| Metric | With Outliers | Without Outliers |
|--------|---------------|------------------|
| R² Score | ~0.88 | ~0.92 |
| MAE | ~$80,000 | ~$65,000 |
| RMSE | ~$100,000 | ~$85,000 |

### Feature Importance
1. **Avg. Area Income** - Strongest predictor
2. **Avg. Area Number of Rooms** - Second most important
3. **Area Population** - Moderate importance
4. **Avg. Area Number of Bedrooms** - Moderate importance
5. **Avg. Area House Age** - Least important

## 🧪 Test Cases

Use these realistic test cases to validate the application:

### Test Case 1: Average Property
```json
{
    "Avg. Area Income": 68584.00,
    "Avg. Area House Age": 5.98,
    "Avg. Area Number of Rooms": 6.98,
    "Avg. Area Number of Bedrooms": 3.98,
    "Area Population": 36163.00
}
```
**Expected Price**: ~$1,232,669

### Test Case 2: High-End Property
```json
{
    "Avg. Area Income": 80175.75,
    "Avg. Area House Age": 7.72,
    "Avg. Area Number of Rooms": 8.48,
    "Avg. Area Number of Bedrooms": 5.05,
    "Area Population": 43621.00
}
```
**Expected Price**: ~$1,600,000

### Test Case 3: Budget Property
```json
{
    "Avg. Area Income": 56721.25,
    "Avg. Area House Age": 4.30,
    "Avg. Area Number of Rooms": 5.52,
    "Avg. Area Number of Bedrooms": 2.97,
    "Area Population": 29403.25
}
```
**Expected Price**: ~$900,000

## 🛠️ Technologies Used

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.3.3**: Web framework
- **scikit-learn 1.3.0**: Machine learning library
- **pandas 2.0.3**: Data manipulation
- **numpy 1.24.3**: Numerical computing
- **joblib 1.3.2**: Model serialization

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with animations
- **JavaScript**: Client-side interactions
- **Font Awesome**: Icons
- **Google Fonts**: Typography

### Data Science
- **Jupyter Notebook**: Development environment
- **matplotlib**: Data visualization
- **seaborn**: Statistical plotting
- **plotly**: Interactive visualizations

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production:
```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
```

### Model Configuration
The application uses the optimized model (`linear_regression_model_no_outliers.pkl`) by default for better performance.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt
pip install jupyter matplotlib seaborn plotly

# Run tests
python -m pytest tests/

# Run with debug mode
export FLASK_DEBUG=1
python app.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Include error messages and system information

## 🚀 Future Enhancements

- [ ] Add more sophisticated models (Random Forest, XGBoost)
- [ ] Implement feature importance visualization
- [ ] Add prediction confidence intervals
- [ ] Create model comparison dashboard
- [ ] Add automated model retraining
- [ ] Implement user authentication
- [ ] Add prediction history tracking
- [ ] Deploy to cloud platforms (AWS, Heroku)

## 📊 Screenshots

### Web Interface
The application features a modern, responsive design with:
- Interactive form with input validation
- Real-time predictions
- Comprehensive error handling
- Mobile-friendly layout

### API Integration
- RESTful JSON API
- Comprehensive error responses
- Request/response logging
- Rate limiting ready

---

**Made with ❤️ and Python**

*Last updated: January 2024*
