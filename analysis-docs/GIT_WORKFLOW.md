# Git Workflow - Clone and Pull Guide

## Initial Setup: Clone Repository to Mac

### For Private Repositories

**Step 1: Create GitHub Personal Access Token**

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Name it: `Mac clone access`
4. Expiration: Choose 90 days or No expiration
5. **Check the `repo` checkbox** (full control of private repositories)
6. Scroll down, click **"Generate token"**
7. **COPY THE TOKEN** (looks like `ghp_xxxxxxxxxxxx`) - you only see it once

**Step 2: Clone Repository**

```bash
cd /Users/kimnguyen/Documents/Github
git clone https://YOUR_TOKEN@github.com/dung-nguyen3/Skills.git
```

Replace `YOUR_TOKEN` with the token you copied.

**Example:**
```bash
cd /Users/kimnguyen/Documents/Github
git clone https://ghp_abc123xyz456@github.com/dung-nguyen3/Skills.git
```

This clones the repository to `/Users/kimnguyen/Documents/Github/Skills`.

## Regular Updates: Pull Latest Changes

### Pull Changes from Main Branch

When Claude makes changes and pushes to GitHub, update your Mac repository:

```bash
cd /Users/kimnguyen/Documents/Github/Skills
git pull origin main
```

### Pull Changes from Specific Branch

If working on a feature branch:

```bash
cd /Users/kimnguyen/Documents/Github/Skills
git checkout branch-name
git pull origin branch-name
```

## Check Current Status

### See which branch you're on:
```bash
git branch
```

### See unpushed commits:
```bash
git status
```

### See recent commits:
```bash
git log --oneline -10
```

## Important Notes

- Your Mac repository does NOT automatically update when changes are pushed to GitHub
- You must manually run `git pull` to get the latest changes
- Always check which branch you're on before pulling
- If you have local uncommitted changes, commit or stash them before pulling

## Common Workflow

1. **Before starting work:**
   ```bash
   cd /Users/kimnguyen/Documents/Github/Skills
   git checkout main
   git pull origin main
   ```

2. **After Claude makes changes:**
   - Wait for Claude to push to GitHub
   - Run the pull commands above
   - Your Mac now has the latest code

3. **Check what changed:**
   ```bash
   git log -5
   git diff HEAD~1
   ```
