# 🚀 Deployment Guide - Terminal X AI

## Quick Deploy Options

### **Option 1: Streamlit Cloud (Recommended) ⭐**

**Perfect for**: Interviews, demos, quick sharing

#### Step 1: Prepare Your Code
```bash
# Make sure your code is ready
git add .
git commit -m "Ready for deployment"
git push origin main
```

#### Step 2: Deploy to Streamlit Cloud
1. **Go to**: [share.streamlit.io](https://share.streamlit.io/)
2. **Sign in** with GitHub
3. **Click "New app"**
4. **Configure**:
   - Repository: `your-username/your-repo-name`
   - Branch: `main`
   - Main file path: `terminal_x_gemini.py`
5. **Click "Deploy"**

#### Step 3: Add API Key
1. **In Streamlit Cloud dashboard**, go to your app
2. **Click "Settings"** → "Secrets"
3. **Add your Gemini API key**:
```toml
GEMINI_API_KEY = "your-actual-api-key-here"
```
4. **Save** and your app will redeploy automatically

#### Step 4: Share Your App
- **Your app URL**: `https://your-app-name.streamlit.app`
- **Share this link** in your interview!

---

### **Option 2: Heroku (Professional)**

**Perfect for**: Professional demos, custom domains

#### Step 1: Create Heroku App
```bash
# Install Heroku CLI
brew install heroku/brew/heroku  # macOS
# or download from heroku.com

# Login and create app
heroku login
heroku create your-terminal-x-ai
```

#### Step 2: Add Buildpacks
```bash
heroku buildpacks:add heroku/python
```

#### Step 3: Deploy
```bash
git push heroku main
```

#### Step 4: Set Environment Variables
```bash
heroku config:set GEMINI_API_KEY="your-api-key-here"
```

---

### **Option 3: Railway (Alternative)**

**Perfect for**: Easy deployment, good performance

1. **Go to**: [railway.app](https://railway.app/)
2. **Connect GitHub** repository
3. **Add environment variable**: `GEMINI_API_KEY`
4. **Deploy automatically**

---

## 🎯 Interview Deployment Strategy

### **Before Interview**
1. **Deploy to Streamlit Cloud** (takes 5 minutes)
2. **Test your app** thoroughly
3. **Prepare demo script**:
   - "This is my Terminal X AI system deployed live"
   - "Let me show you how it processes financial documents"
   - "Watch as the AI analyzes this investment memo"

### **During Interview**
1. **Share your live URL**: `https://your-app.streamlit.app`
2. **Demonstrate live**: Use sample documents
3. **Show real-time processing**: Let them see AI working
4. **Highlight features**: Point out the 7-prompt pipeline

### **After Interview**
- **Keep app running** for follow-up questions
- **Share GitHub repo** for code review
- **Document any issues** for improvements

---

## 🔧 Troubleshooting

### **Common Issues**

#### **App Won't Deploy**
```bash
# Check requirements.txt
pip install -r requirements.txt

# Test locally first
streamlit run terminal_x_gemini.py
```

#### **API Key Issues**
- **Verify key format**: Should start with `AIza...`
- **Check billing**: Ensure Google AI billing is set up
- **Test locally**: Run `python test_gemini.py`

#### **Performance Issues**
- **Monitor rate limits**: Free tier has limits
- **Add billing**: For unlimited usage
- **Optimize prompts**: Reduce token usage

---

## 📊 Deployment Checklist

### **Pre-Deployment**
- [ ] Code works locally
- [ ] API key is valid
- [ ] Requirements.txt is updated
- [ ] README.md is complete
- [ ] Sample data is included

### **Deployment**
- [ ] Repository is pushed to GitHub
- [ ] Streamlit Cloud app is created
- [ ] API key is added to secrets
- [ ] App deploys successfully
- [ ] App is tested with sample data

### **Post-Deployment**
- [ ] App URL is working
- [ ] All features are functional
- [ ] Demo script is prepared
- [ ] Backup plan is ready

---

## 🎉 Success Tips

### **For Interviews**
1. **Deploy early** - Don't wait until interview day
2. **Test everything** - Use different documents
3. **Prepare backup** - Have local version ready
4. **Practice demo** - Know exactly what to show

### **For Sharing**
1. **Add instructions** - How to use the app
2. **Include samples** - Pre-loaded documents
3. **Document features** - What the AI can do
4. **Provide context** - Why this matters

---

## 🚀 Your Deployment URL

Once deployed, your app will be available at:
```
https://your-app-name.streamlit.app
```

**Share this URL in your interview to show a live, working Terminal X AI system!** 🎯 