# 🚀 Deployment Guide - Streamlit Cloud

This guide will help you deploy the **Multi-Agent AI Research System** to Streamlit Cloud in just a few minutes!

---

## What is Streamlit Cloud?

Streamlit Cloud is a free hosting platform specifically designed for Streamlit applications. It:
- ✅ Automatically deploys from GitHub
- ✅ Provides free tier (perfect for our use case)
- ✅ No server management required
- ✅ Instant updates when you push to GitHub
- ✅ Secure secret management for API keys

---

## Prerequisites

1. ✅ Project pushed to GitHub (Already done!)
2. ✅ Streamlit account (Free)
3. ✅ Groq API key
4. ✅ Tavily API key

---

## Step 1: Create Streamlit Account

1. Go to **https://streamlit.io/cloud**
2. Click **"Sign up"** or **"Sign in"**
3. Use your **GitHub account** to sign up (easiest)
4. Grant Streamlit access to your GitHub repositories

---

## Step 2: Deploy Your App

### Option A: Deploy from Streamlit Dashboard

1. Visit **https://share.streamlit.io** (after signing in)
2. Click **"New app"** button
3. Select:
   - **Repository**: `Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **"Deploy"**

### Option B: Direct Deployment Link

Simply visit this URL after logging in and it will auto-detect your repo:
```
https://share.streamlit.io/new
```

---

## Step 3: Add API Secrets

After clicking Deploy, wait for initial deployment (it will fail without API keys - that's normal).

Then add your secrets:

1. Click the **"⋯ (three dots)"** menu in the top-right corner
2. Select **"Settings"**
3. Go to the **"Secrets"** tab
4. Add your API keys:

```toml
GROQ_API_KEY = "your_actual_groq_api_key_here"
TAVILY_API_KEY = "your_actual_tavily_api_key_here"
```

**Important**: Replace the values with your actual API keys from:
- Groq: https://console.groq.com
- Tavily: https://tavily.com

5. Click **"Save"**
6. The app will automatically restart and should now work!

---

## Step 4: Access Your Deployed App

Once deployed successfully, your app will be available at:
```
https://share.streamlit.io/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant
```

Or visit the **"View app"** link shown in the Streamlit Cloud dashboard.

---

## How It Works After Deployment

### Automatic Updates
Every time you push code to GitHub:
```bash
git add .
git commit -m "Your message"
git push origin main
```

Your app on Streamlit Cloud will automatically update! ✨

### App URL
Your app will be accessible 24/7 at:
```
https://share.streamlit.io/your-username/your-repo-name
```

In your case:
```
https://share.streamlit.io/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant
```

---

## Environment Variables & Secrets

### For Local Development
Your `.env` file is used locally (not committed to GitHub).

### For Streamlit Cloud
Add your secrets through the Streamlit Cloud dashboard:
1. Settings → Secrets → Add your keys

The app code automatically uses:
- `st.secrets` when running on Streamlit Cloud
- `.env` file when running locally

---

## Troubleshooting Deployment

### Problem: "AttributeError: module 'streamlit' has no attribute 'secrets'"
**Solution**: Update Streamlit
```bash
pip install --upgrade streamlit>=1.18.0
```

### Problem: "API Key Invalid" after deployment
**Solution**: 
- Copy your exact API key (including any characters)
- Go to Settings → Secrets
- Paste key correctly (no extra spaces/quotes)
- Click Save
- Wait for app to restart

### Problem: App shows "Please add GROQ_API_KEY to secrets"
**Solution**:
- Go to Settings → Secrets
- Add both API keys exactly as shown above
- Make sure keys are valid and active
- Save and wait for restart

### Problem: Deployment takes too long
**Solution**:
- This is normal on first deployment (5-10 minutes)
- Streamlit Cloud is installing dependencies
- Wait patiently, it will complete

### Problem: App crashes or shows errors
**Solution**:
- Check the **"Logs"** tab in the app settings
- Look for error messages
- Most common: missing API keys or wrong key format
- Fix in Secrets tab and restart

---

## Features After Deployment

✅ **24/7 Availability** - App runs 24/7
✅ **Free Tier** - No cost for basic usage
✅ **Instant Updates** - Push to GitHub → Auto-updates
✅ **Custom URL** - Share your app link with others
✅ **Automatic Scaling** - Handles multiple users
✅ **Secure Secrets** - API keys never visible in code

---

## Sharing Your App

Once deployed, share the link:
```
https://share.streamlit.io/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant
```

Anyone can use your app without installing anything!

---

## Making Updates

After deployment, to update your app:

1. **Make changes locally**
```bash
cd Multi-Agent-AI-Research-Assistant
# Make your code changes
```

2. **Commit and push to GitHub**
```bash
git add .
git commit -m "Your description"
git push origin main
```

3. **Wait 1-2 minutes** for Streamlit Cloud to redeploy

4. **Refresh your deployed app** - it's updated! 🎉

---

## Advanced: Custom Domain (Optional)

To use your own domain:
1. Go to Settings → Custom Domain
2. Enter your domain (e.g., research.yourdomain.com)
3. Update DNS settings as instructed
4. Your app is now at your custom domain!

(This requires purchased domain)

---

## Limits & Quotas

### Free Tier Includes:
- ✅ 1 free public app
- ✅ Unlimited concurrent users
- ✅ 10GB of storage
- ✅ Monthly resets

### Your API Limits:
- **Groq**: Very generous free tier (usually unlimited)
- **Tavily**: 100 searches/month on free tier

If you hit Tavily limit, either:
- Upgrade to paid Tavily plan
- Wait for monthly reset
- Implement caching in your app

---

## Monitoring Your App

After deployment, monitor:

1. **App Logs** - Click app → Settings → Logs
2. **App Health** - Check if it's running
3. **Error Messages** - Look for API issues
4. **Usage** - See how many people are using it

---

## Useful Links

- 📚 [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- 🔐 [Secrets Management](https://docs.streamlit.io/streamlit-cloud/deploy-your-app/secrets-management)
- 📊 [Streamlit Dashboard](https://share.streamlit.io)
- 🐛 [Troubleshooting](https://docs.streamlit.io/streamlit-cloud/troubleshooting)

---

## Quick Reference

### Deploy Steps (TL;DR)
1. Go to https://share.streamlit.io
2. Click "New app"
3. Select repository and `app.py`
4. Click "Deploy"
5. Add API keys in Settings → Secrets
6. Done! ✨

### Update App (TL;DR)
```bash
git add .
git commit -m "changes"
git push origin main
# Wait 1-2 minutes, refresh browser
```

---

## Still Need Help?

- 📧 Check Streamlit Cloud documentation
- 🐛 Open an issue on GitHub
- 💬 Check app logs for error messages
- 🔑 Verify API keys are correct and active

---

**Happy Deploying! 🚀**

Your Multi-Agent AI Research System is now accessible to everyone!
