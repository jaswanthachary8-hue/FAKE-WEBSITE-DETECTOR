# 🚀 Quick GitHub Deployment Guide

## Step-by-Step Instructions

### 1️⃣ Open Terminal/PowerShell

Navigate to your project folder:
```bash
cd Myproject
```

### 2️⃣ Initialize Git (First Time Only)

```bash
git init
```

### 3️⃣ Add All Files

```bash
git add .
```

This will add all files except those in `.gitignore` (like model files, cache, etc.)

### 4️⃣ Create First Commit

```bash
git commit -m "Initial commit: Fake Web Detector project"
```

### 5️⃣ Create GitHub Repository

1. Go to **https://github.com**
2. Click the **"+"** icon (top right)
3. Click **"New repository"**
4. Fill in:
   - **Repository name**: `fake-web-detector` (or your choice)
   - **Description**: "ML-based phishing URL detection system"
   - **Visibility**: Public or Private
   - **IMPORTANT**: Do NOT check any boxes (README, .gitignore, license)
5. Click **"Create repository"**

### 6️⃣ Connect and Push

Copy the commands GitHub shows you, or use these (replace YOUR_USERNAME and YOUR_REPO_NAME):

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 7️⃣ Authentication

If asked for credentials:
- **Username**: Your GitHub username
- **Password**: Use a **Personal Access Token** (not your password)
  - Create one: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - Give it `repo` permissions

### 8️⃣ Done! ✅

Visit your repository: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`

---

## 🔄 Updating Your Repository

After making changes:

```bash
git add .
git commit -m "Description of your changes"
git push
```

---

## 📋 What Gets Uploaded?

✅ **Uploaded:**
- All Python source code
- HTML templates
- README.md
- requirements.txt
- Configuration files

❌ **NOT Uploaded** (via .gitignore):
- Model files (`.pkl`)
- Python cache (`__pycache__/`)
- Virtual environments
- Generated datasets

---

## 🆘 Troubleshooting

**"remote: Support for password authentication was removed"**
→ Use Personal Access Token instead of password

**"Permission denied"**
→ Check repository URL and your GitHub access

**"fatal: not a git repository"**
→ Run `git init` first

---

**Need more details?** See `DEPLOYMENT.md` for cloud platform deployment options!
