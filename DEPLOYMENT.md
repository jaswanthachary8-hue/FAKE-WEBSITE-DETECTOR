# 🚀 Deployment Guide - Fake Web Detector

This guide will help you deploy the Fake Web Detector project to GitHub and various cloud platforms.

## 📦 Preparing for GitHub

### 1. Check Your Files

Make sure you have:
- ✅ `.gitignore` file (created automatically)
- ✅ `README.md` with project documentation
- ✅ `requirements.txt` with all dependencies
- ✅ All source code files

### 2. Files That Won't Be Uploaded

The `.gitignore` excludes:
- `*.pkl` - Trained model files (users train their own)
- `__pycache__/` - Python cache
- `venv/`, `env/` - Virtual environments
- `dataset/phishing_dataset.csv` - Generated datasets
- `.DS_Store`, `Thumbs.db` - OS files

## 🔵 GitHub Deployment Steps

### Step 1: Initialize Git (if not done)

```bash
# Navigate to your project directory
cd Myproject

# Initialize git repository
git init
```

### Step 2: Check Git Status

```bash
git status
```

This shows which files will be added. Make sure model files (`.pkl`) are not listed.

### Step 3: Add Files

```bash
# Add all files (respecting .gitignore)
git add .
```

### Step 4: Create First Commit

```bash
git commit -m "Initial commit: Fake Web Detector - Phishing URL Detection System"
```

### Step 5: Create GitHub Repository

1. **Go to GitHub**: https://github.com
2. **Click** the "+" icon (top right) → "New repository"
3. **Repository name**: `fake-web-detector` (or your preferred name)
4. **Description**: "Machine learning-based phishing URL detection system"
5. **Visibility**: Choose Public or Private
6. **IMPORTANT**: Do NOT check:
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
   
   (We already have these files!)

7. **Click** "Create repository"

### Step 6: Connect and Push

GitHub will show you commands. Use these (replace with your username and repo name):

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**If you get authentication errors**, you may need to:
- Use a Personal Access Token instead of password
- Or use SSH: `git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git`

### Step 7: Verify

Visit your repository URL to confirm all files are uploaded.

## ☁️ Cloud Platform Deployment

### Option 1: Heroku

#### Prerequisites
- Heroku account: https://signup.heroku.com
- Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

#### Steps

1. **Create Procfile** (in project root):
   ```
   web: python WEB/APP.PY
   ```

2. **Create runtime.txt** (optional, specify Python version):
   ```
   python-3.11.0
   ```

3. **Login to Heroku**:
   ```bash
   heroku login
   ```

4. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

6. **Train model on Heroku** (one-time):
   ```bash
   heroku run python dataset/generate_dataset.py
   heroku run python ml/train_model.py
   ```

7. **Open app**:
   ```bash
   heroku open
   ```

### Option 2: Railway

#### Steps

1. **Go to**: https://railway.app
2. **Sign up** with GitHub
3. **New Project** → "Deploy from GitHub repo"
4. **Select** your repository
5. **Railway auto-detects** Python
6. **Settings** → Add start command:
   ```
   python WEB/APP.PY
   ```
7. **Deploy** automatically happens!

**Note**: You'll need to train the model after first deployment:
- Go to Railway dashboard → "View Logs" → "Run Command"
- Run: `python dataset/generate_dataset.py && python ml/train_model.py`

### Option 3: Render

#### Steps

1. **Go to**: https://render.com
2. **Sign up** with GitHub
3. **New** → "Web Service"
4. **Connect** your GitHub repository
5. **Configure**:
   - **Name**: `fake-web-detector`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python WEB/APP.PY`
6. **Deploy**!

### Option 4: PythonAnywhere

#### Steps

1. **Sign up**: https://www.pythonanywhere.com
2. **Upload files** via Files tab
3. **Open Bash console**
4. **Install dependencies**:
   ```bash
   pip3.10 install --user -r requirements.txt
   ```
5. **Train model**:
   ```bash
   python3.10 dataset/generate_dataset.py
   python3.10 ml/train_model.py
   ```
6. **Create Web App**:
   - Go to Web tab
   - Add new web app
   - Select Flask
   - Set source code path to your project
   - Set WSGI file to point to `WEB/APP.PY`

## 🔧 Post-Deployment Checklist

After deploying, make sure to:

- [ ] Train the model on the server (if not included in deployment)
- [ ] Test the web interface
- [ ] Test the API endpoint
- [ ] Update README with live URL (if applicable)
- [ ] Add badges to README (optional)

## 📝 Adding Badges to README

You can add these badges to your README.md (after deployment):

```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
```

## 🐛 Troubleshooting

### Git Push Issues

**Error**: "remote: Support for password authentication was removed"
- **Solution**: Use Personal Access Token or SSH keys

**Error**: "Permission denied"
- **Solution**: Check repository URL and your access permissions

### Deployment Issues

**Model not found error**:
- Train the model on the server after deployment
- Or include a pre-trained model (if small enough)

**Import errors**:
- Make sure all dependencies are in `requirements.txt`
- Check Python version compatibility

**Port issues**:
- Some platforms require specific ports
- Update `WEB/APP.PY` to use `os.environ.get('PORT', 5000)`

## 📚 Additional Resources

- [GitHub Docs](https://docs.github.com)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Railway Docs](https://docs.railway.app)
- [Render Docs](https://render.com/docs)

---

**Need help?** Open an issue on GitHub!
