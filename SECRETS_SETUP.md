# 🔐 Setting Up API Keys on Streamlit Cloud - Simple Guide

If you can't find the Settings option, here are **3 easy ways** to add your API keys to Streamlit Cloud:

---

## Method 1: Via App Dashboard (Recommended if you can see it)

1. Go to https://share.streamlit.io/
2. Find your app: **Multi-Agent-AI-Research-Assistant**
3. Click on the app name to open it
4. Wait for it to load completely
5. Look at the **top-right corner** for the **hamburger menu (≡)** or **gear icon (⚙️)**
6. Click it → Select **"Settings"** or **"App settings"**
7. Look for **"Secrets"** tab
8. Paste this:
```
GROQ_API_KEY = "your_actual_groq_key_here"
TAVILY_API_KEY = "your_actual_tavily_key_here"
```
9. Click **"Save"**
10. App will restart automatically ✨

---

## Method 2: Direct Link to Settings

Try opening the settings directly:
```
https://share.streamlit.io/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant/settings/secrets
```

If that doesn't work, try:
```
https://share.streamlit.io/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant/settings
```

Then look for "Secrets" tab.

---

## Method 3: Via Your Deployed App Page

1. Go to your deployed app URL (if it exists)
2. Look for a **"Manage app"** button (usually bottom-right or top-right)
3. Click it
4. You'll see Settings
5. Go to **"Secrets"** tab
6. Add your keys as shown above

---

## Method 4: If Streamlit Cloud UI Isn't Working

You can add secrets directly to GitHub by editing `.streamlit/secrets.toml`:

1. Go to GitHub: https://github.com/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant
2. Click **"Code"** tab
3. Navigate to `.streamlit/secrets.toml` folder
4. Click the **pencil icon** to edit
5. Update the file with your actual keys:
```
GROQ_API_KEY = "your_actual_groq_key_here"
TAVILY_API_KEY = "your_actual_tavily_key_here"
```
6. Scroll down and click **"Commit changes"**
7. Streamlit Cloud will automatically redeploy with your secrets

---

## Getting Your API Keys

### Groq API Key
1. Go to https://console.groq.com
2. Sign up or log in
3. Go to **"API Keys"** section
4. Click **"Create API Key"**
5. Copy the entire key (looks like: `gsk_...`)

### Tavily API Key
1. Go to https://tavily.com
2. Sign up or log in
3. Go to **"API Keys"** in dashboard
4. Copy your key (starts with `tvly-`)

---

## Quick Checklist

- [ ] Got Groq API key (starts with `gsk_`)
- [ ] Got Tavily API key (starts with `tvly-`)
- [ ] Added both to Streamlit Secrets
- [ ] Clicked Save/Committed changes
- [ ] Waited 1-2 minutes for app to restart
- [ ] Refreshed the app page in browser

---

## Still Not Working?

### If you see "API Key Invalid":
- Check your keys don't have extra spaces
- Copy paste them carefully (no quotes at start/end)
- Make sure they're still active in your provider accounts
- Try regenerating a new key

### If Settings tab is hidden:
- Try signing out and back in to Streamlit Cloud
- Try a different browser
- Check if you're the app owner (you should be)

### If you still can't find Settings:
- Check Streamlit Cloud documentation: https://docs.streamlit.io/streamlit-cloud/deploy-your-app/secrets-management
- Open an issue on GitHub

---

## Test It's Working

Once you've added the secrets:
1. Refresh your app page
2. Wait for it to load (might say "Rerunning")
3. Try entering a research topic
4. Click "Run Research Pipeline"
5. If it works, you're all set! 🎉

---

## Example Secrets Format

Your `.streamlit/secrets.toml` should look like:

```toml
GROQ_API_KEY = "gsk_xAbCd1234567890xYz..."
TAVILY_API_KEY = "tvly-abcd1234567890xyz..."
```

**Important**: 
- No quotes around the key values (actually, the `=` means values ARE strings in TOML, but the quotes help)
- Each key on its own line
- Make sure you're using the correct keys (not truncated)

---

## Questions?

Check the full deployment guide:
- Read: [DEPLOYMENT.md](../DEPLOYMENT.md)
- GitHub Issues: https://github.com/Vinay-Birajdar3/Multi-Agent-AI-Research-Assistant/issues

---

**You're almost there! Just add those API keys and your research system will be live! 🚀**
