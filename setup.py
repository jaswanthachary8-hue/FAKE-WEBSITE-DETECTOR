"""
Quick setup script for Fake Web Detector
Run this to set up the project: python setup.py
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{'='*50}")
    print(f"Step: {description}")
    print(f"Command: {command}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

def main():
    print("🛡️ Fake Web Detector - Setup Script")
    print("="*50)
    
    # Step 1: Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("\n❌ Failed to install dependencies. Please install manually:")
        print("   pip install -r requirements.txt")
        return
    
    # Step 2: Generate dataset
    if not run_command("python dataset/generate_dataset.py", "Generating dataset"):
        print("\n⚠️  Warning: Dataset generation failed. You may need to create it manually.")
    
    # Step 3: Train model
    print("\n" + "="*50)
    print("Training the model...")
    print("="*50)
    print("This may take a few moments...")
    
    if not run_command("python ml/train_model.py", "Training model"):
        print("\n❌ Failed to train model. Please check the dataset exists.")
        return
    
    print("\n" + "="*50)
    print("✅ Setup Complete!")
    print("="*50)
    print("\nTo start the web application, run:")
    print("   python WEB/APP.PY")
    print("\nThen open your browser to: http://localhost:5000")
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
