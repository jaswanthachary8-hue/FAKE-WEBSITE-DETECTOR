# 🚀 Quick Deploy Guide - Get Your Live App URL

## Option 1: Railway (Easiest & Free) ⭐ Recommended

### Steps:
1. **Go to**: https://railway.app
2. **Sign up** with GitHub (click "Login with GitHub")
3. **New Project** → "Deploy from GitHub repo"
4. **Select** your repository: `jaswanthachary8-hue/fake-web-detector`
5. **Railway auto-detects** Python
6. **Settings** → Add start command:
   ```
   python WEB/APP.PY
   ```
7. **Deploy** - Railway will automatically deploy!

### After Deployment:
- Railway gives you a URL like: `https://your-app-name.up.railway.app`
- **Train the model** (one-time):
  - Go to Railway dashboard → Your project → "View Logs" → "Run Command"
  - Run: `python dataset/generate_dataset.py`
  - Then: `python ml/train_model.py`

### Share Your Live URL:
```
https://your-app-name.up.railway.app
```

---

## Option 2: Render (Free Tier Available)

### Steps:
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

### Share Your Live URL:
```
https://fake-web-detector.onrender.com
```

---

## Option 3: PythonAnywhere (Free Tier)

### Steps:
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
   - Add new web app → Flask
   - Set source code path
   - Set WSGI file to `WEB/APP.PY`

### Share Your Live URL:
```
https://yourusername.pythonanywhere.com
```

---

## 📝 After Deployment

### Update Your README:
Add a "Live Demo" section to your README.md:

```markdown
## 🌐 Live Demo

Try the app: [Your Live URL]

Or clone and run locally:
```bash
git clone https://github.com/jaswanthachary8-hue/fake-web-detector.git
cd fake-web-detector
pip install -r requirements.txt
python dataset/generate_dataset.py
python ml/train_model.py
python WEB/APP.PY
```
```

### Share Both Links:
- **GitHub Repository**: https://github.com/jaswanthachary8-hue/fake-web-detector
- **Live App**: https://your-deployed-url.com

---

## ⚡ Quick Comparison

| Platform | Free Tier | Ease | Auto-Deploy |
|----------|-----------|------|-------------|
| Railway | ✅ Yes | ⭐⭐⭐⭐⭐ | ✅ Yes |
| Render | ✅ Yes | ⭐⭐⭐⭐ | ✅ Yes |
| PythonAnywhere | ✅ Yes | ⭐⭐⭐ | ❌ Manual |

**Recommendation**: Start with **Railway** - it's the easiest!
