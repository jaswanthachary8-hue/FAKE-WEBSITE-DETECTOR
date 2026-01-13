from flask import Flask, render_template, request, jsonify
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ml.PREDICT import predict
from features.feature_extractor import extract_features

# Set template folder
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TEMPLATES')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_url():
    """API endpoint to predict if a URL is phishing."""
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({
                'error': 'URL is required'
            }), 400
        
        # Add protocol if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Get prediction
        result = predict(url)
        
        # Get features for display
        features = extract_features(url)
        
        return jsonify({
            'success': True,
            'url': url,
            'prediction': result['label'],
            'is_phishing': result['prediction'] == 1,
            'confidence': result['confidence'],
            'probabilities': result['probabilities'],
            'features': features
        })
    
    except FileNotFoundError as e:
        return jsonify({
            'error': 'Model not found. Please train the model first.',
            'details': str(e)
        }), 500
    
    except Exception as e:
        return jsonify({
            'error': 'An error occurred during prediction',
            'details': str(e)
        }), 500


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # Get port from environment variable (for cloud platforms) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Debug mode only in development (not in production)
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
