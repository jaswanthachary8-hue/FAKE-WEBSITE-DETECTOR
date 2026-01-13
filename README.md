# 🛡️ Fake Web Detector - Phishing URL Detection System

A machine learning-based web application that detects phishing and fake websites by analyzing URL characteristics, domain information, and webpage content.

## 📋 Features

- **URL Analysis**: Extracts features from URLs including length, special characters, subdomains, and suspicious patterns
- **Domain Analysis**: Checks domain age, expiry, TLD risk, and new domain status using WHOIS data
- **Content Analysis**: Analyzes webpage content for forms, password inputs, external scripts, iframes, and phishing keywords
- **Machine Learning Model**: Uses Logistic Regression to classify URLs as legitimate or phishing
- **Web Interface**: Beautiful, modern web UI for easy URL checking
- **API Endpoint**: RESTful API for programmatic access

## 🏗️ Project Structure

```
Myproject/
├── features/              # Feature extraction modules
│   ├── url_features.py    # URL-based features
│   ├── domain_features.py # Domain-based features
│   ├── content_features.py # Content-based features
│   └── feature_extractor.py # Main feature extractor
├── ml/                    # Machine learning components
│   ├── train_model.py     # Model training script
│   └── PREDICT.PY         # Prediction module
├── dataset/               # Dataset and generation scripts
│   ├── generate_dataset.py
│   └── phishing_dataset.csv
├── utils/                 # Utility modules
│   ├── keywords.py        # Phishing keywords list
│   └── HELPERS.PY         # Helper functions
├── WEB/                   # Web application
│   ├── APP.PY             # Flask application
│   └── TEMPLATES/
│       └── index.html     # Web UI
└── requirements.txt       # Python dependencies
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project

```bash
cd Myproject
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: On some systems, you may need to install `python-whois` separately:
```bash
pip install python-whois
```

### Step 3: Generate Dataset

The project includes a small sample dataset. To generate it:

```bash
python dataset/generate_dataset.py
```

This will create `dataset/phishing_dataset.csv` with sample URLs.

**Optional**: For better accuracy, you can use a larger dataset:
1. Download a phishing dataset (e.g., from Kaggle)
2. Place it in the `dataset/` folder
3. Update the dataset path in `ml/train_model.py` if needed

### Step 4: Train the Model

```bash
python ml/train_model.py
```

This will:
- Load the dataset
- Train a Logistic Regression model
- Evaluate the model performance
- Save the trained model to `ml/phishing_model.pkl`

### Step 5: Run the Web Application

```bash
python WEB/APP.PY
```

The application will start on `http://localhost:5000`

Open your browser and navigate to `http://localhost:5000` to use the web interface.

## 💻 Usage

### Web Interface

1. Start the web application (see Step 5 above)
2. Open `http://localhost:5000` in your browser
3. Enter a URL in the input field
4. Click "Check URL" to analyze
5. View the prediction results with confidence scores and extracted features

### Command Line Prediction

You can also use the prediction module directly:

```python
from ml.PREDICT import predict

result = predict("https://example.com")
print(result)
```

Output:
```python
{
    'prediction': 0,
    'label': 'Legitimate',
    'confidence': 95.5,
    'probabilities': {
        'legitimate': 95.5,
        'phishing': 4.5
    }
}
```

### API Endpoint

The web application provides a REST API:

**POST** `/predict`
```json
{
    "url": "https://example.com"
}
```

**Response:**
```json
{
    "success": true,
    "url": "https://example.com",
    "prediction": "Legitimate",
    "is_phishing": false,
    "confidence": 95.5,
    "probabilities": {
        "legitimate": 95.5,
        "phishing": 4.5
    },
    "features": {
        "url_length": 19,
        "has_ip": 0,
        ...
    }
}
```

## 🔍 Extracted Features

The system extracts 18 features from URLs:

### URL Features (8)
- URL length
- IP address presence
- @ symbol count
- Dash count
- Dot count
- Subdomain count
- URL shortener detection
- Suspicious word count

### Domain Features (4)
- Domain age (days)
- Domain expiry (days)
- New domain flag (< 180 days)
- Risky TLD detection

### Content Features (6)
- Form presence
- Password input presence
- External form action
- Iframe count
- External script count
- Phishing keyword count

## 📊 Model Performance

The model uses Logistic Regression and provides:
- Binary classification (Legitimate/Phishing)
- Confidence scores
- Probability distributions

To improve accuracy:
- Use a larger, more diverse training dataset
- Experiment with different ML algorithms (Random Forest, XGBoost, etc.)
- Add more features
- Fine-tune hyperparameters

## 🛠️ Development

### Testing Feature Extraction

```bash
python test_feature_extractor.py
```

### Adding More URLs to Dataset

Edit `dataset/generate_dataset.py` and add more URLs to the `URLS` list:

```python
URLS = [
    ("https://www.example.com", 0),  # 0 = legitimate
    ("http://suspicious-site.xyz", 1),  # 1 = phishing
    # Add more URLs...
]
```

Then regenerate:
```bash
python dataset/generate_dataset.py
```

## ⚠️ Limitations

1. **Small Dataset**: The default dataset has only 8 samples. For production use, train on a larger dataset.
2. **WHOIS Limitations**: Some domains may not return WHOIS data, resulting in default values.
3. **Content Analysis**: Some websites may block automated requests or require JavaScript.
4. **False Positives/Negatives**: No ML model is 100% accurate. Always use additional verification.

## 🔒 Security Note

This tool is for educational and research purposes. Always verify suspicious URLs through multiple sources and never rely solely on automated detection.

## 📝 License

This project is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to improve this project by:
- Adding more features
- Improving the ML model
- Enhancing the UI
- Adding more test cases
- Improving documentation

## 🚀 Deploying to GitHub

### Step 1: Initialize Git Repository

If you haven't already, initialize a git repository:

```bash
git init
```

### Step 2: Add Files to Git

```bash
git add .
```

**Note**: The `.gitignore` file will automatically exclude:
- Model files (`.pkl`, `.joblib`)
- Python cache files (`__pycache__/`)
- Dataset files (users should generate their own)
- Virtual environment folders

### Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: Fake Web Detector project"
```

### Step 4: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., `fake-web-detector`)
5. Choose public or private
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### Step 5: Connect Local Repository to GitHub

GitHub will show you commands. Use these (replace `YOUR_USERNAME` and `YOUR_REPO_NAME`):

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Step 6: Verify Deployment

Visit your repository on GitHub to verify all files are uploaded correctly.

## 🌐 Deploying to Cloud Platforms

### Option 1: Heroku

1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Create a `Procfile` in the root directory:
   ```
   web: python WEB/APP.PY
   ```
3. Login to Heroku:
   ```bash
   heroku login
   ```
4. Create Heroku app:
   ```bash
   heroku create your-app-name
   ```
5. Deploy:
   ```bash
   git push heroku main
   ```

### Option 2: Railway

1. Go to [Railway](https://railway.app)
2. Connect your GitHub repository
3. Railway will auto-detect Python and install dependencies
4. Set start command: `python WEB/APP.PY`
5. Deploy!

### Option 3: Render

1. Go to [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python WEB/APP.PY`
5. Deploy!

## 📧 Support

For issues or questions, please check the code comments or create an issue in the repository.

---

**Made with ❤️ for web security awareness**
