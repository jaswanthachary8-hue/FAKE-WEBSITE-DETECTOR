# 🐛 Troubleshooting Guide - Common Errors & Solutions

## 📋 Quick Diagnosis

**Please share the exact error message!** This helps identify the issue quickly.

---

## 🔴 Common Errors & Solutions

### 1. "Model not found" / FileNotFoundError

**Error Message:**
```
FileNotFoundError: Model not found at ml/phishing_model.pkl
```

**Solution:**
```bash
# Step 1: Generate the dataset
python dataset/generate_dataset.py

# Step 2: Train the model
python ml/train_model.py
```

This creates `ml/phishing_model.pkl` which is needed for predictions.

---

### 2. "ModuleNotFoundError" / Import Errors

**Error Message:**
```
ModuleNotFoundError: No module named 'flask'
ModuleNotFoundError: No module named 'pandas'
```

**Solution:**
```bash
# Install all dependencies
pip install -r requirements.txt

# If that doesn't work, install individually:
pip install flask pandas scikit-learn joblib numpy requests beautifulsoup4 lxml tldextract python-whois
```

---

### 3. "Dataset not found" Error

**Error Message:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'dataset/phishing_dataset.csv'
```

**Solution:**
```bash
# Generate the dataset first
python dataset/generate_dataset.py
```

---

### 4. Port Already in Use

**Error Message:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**

**Option 1**: Kill the process using port 5000
```bash
# Windows PowerShell
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Or use a different port in WEB/APP.PY
```

**Option 2**: Change the port in `WEB/APP.PY`:
```python
app.run(debug=debug, host='0.0.0.0', port=8000)  # Use port 8000 instead
```

---

### 5. "Template not found" Flask Error

**Error Message:**
```
jinja2.exceptions.TemplateNotFound: index.html
```

**Solution:**
- Check that `WEB/TEMPLATES/index.html` exists
- Verify the template folder path in `WEB/APP.PY`

---

### 6. WHOIS / Domain Lookup Errors

**Error Message:**
```
whois.parser.PywhoisError: No match for domain
```

**Solution:**
- This is normal! Some domains don't have WHOIS data
- The code handles this gracefully (returns -1 for missing values)
- Not a critical error - the app will still work

---

### 7. SSL Certificate Errors (Content Features)

**Error Message:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solution:**
This happens when fetching content from some sites. The code handles this in the `except` block, so it's not fatal. But if you want to fix it:

```python
# In features/content_features.py, you can add verify=False (not recommended for production)
response = requests.get(url, headers=HEADERS, timeout=8, verify=False)
```

---

### 8. Deployment Errors (Railway/Render)

**Error Message:**
```
ModuleNotFoundError or Import errors on deployment
```

**Solution:**
1. Make sure `requirements.txt` includes ALL dependencies
2. Check the build logs on your deployment platform
3. Ensure Python version matches (check `runtime.txt`)

**For Railway:**
- Go to Settings → Start Command: `python WEB/APP.PY`
- Make sure Build Command is empty or `pip install -r requirements.txt`

**For Render:**
- Build Command: `pip install -r requirements.txt`
- Start Command: `python WEB/APP.PY`

---

### 9. Path Issues (Windows/Deployment)

**Error Message:**
```
FileNotFoundError or path-related errors
```

**Solution:**
- Use forward slashes `/` in paths (works on all platforms)
- Or use `os.path.join()` (already done in code)
- Make sure you're running from the project root directory

---

### 10. Python Version Issues

**Error Message:**
```
SyntaxError or version-related errors
```

**Solution:**
- Requires Python 3.8 or higher
- Check version: `python --version`
- Update Python if needed

---

## 🔧 Quick Test Commands

Test if everything is set up correctly:

```bash
# 1. Test Python version
python --version  # Should be 3.8+

# 2. Test dependencies
python -c "import flask, pandas, sklearn; print('All imports OK')"

# 3. Generate dataset
python dataset/generate_dataset.py

# 4. Train model
python ml/train_model.py

# 5. Test feature extraction
python test_feature_extractor.py

# 6. Run the app
python WEB/APP.PY
```

---

## 📞 Still Having Issues?

**Please share:**
1. ✅ The exact error message (copy/paste)
2. ✅ What command you ran
3. ✅ Your Python version (`python --version`)
4. ✅ Your operating system

**Common Information to Include:**
```
Error: [paste full error here]
Command: python WEB/APP.PY
Python: 3.11.0
OS: Windows 10
```

---

## ✅ Pre-Flight Checklist

Before running the app, make sure:

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Dataset generated (`python dataset/generate_dataset.py`)
- [ ] Model trained (`python ml/train_model.py`)
- [ ] Running from project root directory
- [ ] Port 5000 is available (or change port)

---

## 🆘 Need More Help?

1. Check the error message carefully
2. Search for the error online
3. Check the deployment platform logs (if deploying)
4. Review the code comments for hints
5. Make sure you followed all installation steps
