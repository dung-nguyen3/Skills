# Notion Automation & File Upload Guide - Complete Reference

## Overview

This guide covers automation tools, connectors, and file upload methods for Notion, specifically for automating study guide workflows on Mac.

---

## Table of Contents

1. [Automation Platforms Comparison](#automation-platforms-comparison)
2. [Free Tier Details](#free-tier-details)
3. [Best Automation Platform for Study Guides](#best-automation-platform-for-study-guides)
4. [File Upload Methods](#file-upload-methods)
5. [Mac Automator & Apple Shortcuts Integration](#mac-automator--apple-shortcuts-integration)
6. [Popular Notion Integrations](#popular-notion-integrations)
7. [Step-by-Step Setup Guides](#step-by-step-setup-guides)
8. [Recommended Workflow for Study Guides](#recommended-workflow-for-study-guides)

---

## Automation Platforms Comparison

### Available Platforms (9 Total)

You can integrate with Notion using:
1. **Zapier** - Most popular, 8,000+ apps
2. **Make.com** (formerly Integromat) - Visual workflow builder
3. **n8n** - Open-source, self-hosted option
4. **Pabbly Connect** - Budget-friendly
5. **IFTTT** - Simple if-this-then-that automation
6. **Unito** - Two-way sync specialist
7. **Integrately** - Pre-built automation recipes
8. **Pipedream** - Developer-friendly
9. **Albato** - Emerging platform

### Platform Comparison Table

| Platform | Free Tier | Paid Plans Start At | Best For | Notion Support |
|----------|-----------|---------------------|----------|----------------|
| **Zapier** | Limited (100 tasks/month) | $19.99/month | Beginners, most integrations | Full ✅ |
| **Make** | 1,000 operations/month | $10.59/month | Visual workflows, complexity | Full ✅ |
| **n8n** | Unlimited (self-hosted) | $24/month (cloud) | Technical users, no limits | Full ✅ |
| **Pabbly** | No free tier | $19/month | Unlimited automation | Full ✅ |
| **IFTTT** | 2 applets free | $2.50/month | Simple automation | Basic |
| **Pipedream** | 100 credits/day free | $19/month | Developers, custom code | API access |

---

## Free Tier Details

### Zapier Free Plan
- **100 tasks per month**
- 5 Zaps (workflows) maximum
- Single-step Zaps only
- 15-minute update interval
- **Good for**: Testing automation, simple workflows
- **Limitation**: Cannot create multi-step workflows (e.g., "when file uploaded → create database entry → send notification")

### Make.com Free Plan ⭐ RECOMMENDED
- **1,000 operations per month**
- Unlimited active scenarios (workflows)
- 15-minute execution interval
- All integrations included
- **Good for**: Complex workflows, pharmacy student needs
- **Note**: Each action = 1 operation. A workflow with 5 steps uses 5 operations per run.

**Example for Study Guides:**
```
Upload source file → Create database entry → Tag with subject → Update status = 4 operations
Running this 250 times = 1,000 operations (free tier limit)
```

### n8n Community Edition ⭐ BEST VALUE
- **Completely free** (self-hosted on your Mac)
- **Unlimited** workflows and executions
- All integrations included
- Requires technical setup (Docker or Node.js)
- **Good for**: Users comfortable with command line, unlimited automation needs
- **Limitation**: You host it yourself (uses your Mac's resources)

### Notion Free Plan Limitations
- **5 MB per file** upload limit (vs unlimited on paid plans)
- Fewer admin controls for integrations
- API rate limits for heavy automation
- **Still works with**: Slack, Google Calendar, Zapier, Make, most automations

---

## Best Automation Platform for Study Guides

### Recommended: Make.com (Free Tier)

**Why Make.com is best for pharmacy students:**

1. **1,000 operations = plenty for monthly study guide creation**
   - Create 10 study guides with 10-step automation each = 100 operations
   - Leaves 900 operations for other tasks

2. **Visual workflow builder** (drag-and-drop)
   - No coding required
   - See exactly what happens at each step

3. **Full Notion integration**
   - Create database entries
   - Upload files
   - Update properties
   - Search and filter

4. **Pre-built templates available**
   - "Upload file to Google Drive → Create Notion database entry"
   - "Gmail attachment → Notion database"

### Alternative: n8n (Self-Hosted) - If You Want Unlimited

**Pros:**
- Completely free forever
- No monthly operation limits
- More powerful than Make or Zapier
- Open-source (constantly improving)

**Cons:**
- Requires technical setup (install Docker or Node.js)
- Need to keep Mac running for automation (or use cloud hosting)
- Learning curve steeper than Make

**Setup difficulty**: Moderate (1-2 hours initial setup)

---

## File Upload Methods

### Method 1: Notion API Direct Upload (Up to 20 MB)

**Official Notion API supports:**
- Files up to **20 MB** (larger than 5 MB free plan in-app limit!)
- Direct upload to Notion-managed storage
- Attachable to pages, blocks, or database properties

**3-Step Process:**

```
Step 1: Create File Upload Object
POST to Notion API → Returns upload_url and file_id

Step 2: Upload Binary File
PUT file contents to upload_url → File stored in Notion

Step 3: Attach File to Database/Page
Use file_id to attach to database entry → File appears in Notion
```

**Time Limit**: Files must be attached within **1 hour** or auto-archived

**Best for**: Automating study guide source file uploads

### Method 2: Third-Party Integration Platforms

**Via Make.com:**
- "Google Drive → Notion" module
- "Dropbox → Notion" module
- "Email attachment → Notion" module

**Via Zapier:**
- Similar pre-built file upload integrations
- Limited to 100/month on free tier

**Via n8n:**
- File upload nodes for Notion
- Can process multiple files in batch

### Method 3: Mac Automator + Notion API

**Native Mac automation** (covered in detail below)

---

## Mac Automator & Apple Shortcuts Integration

### Apple Shortcuts (Native Mac/iOS Integration)

**What Shortcuts Can Do with Notion:**

Notion provides **2 built-in actions** for Apple Shortcuts:
1. **Add to Database** - Create new database entries
2. **Add Content** - Add content to pages

**Current Limitations (2025):**
- Can only set **title** and **content** when creating database page
- **Cannot set custom properties** (e.g., Status, Subject, Date)
- For full property control, need to use Notion API

**Good for:**
- Quick note capture
- Voice-activated task creation (via Siri)
- Simple workflows

**Not good for:**
- Complex study guide automation
- Setting multiple database properties
- File uploads

### Mac Automator Workflows

**Mac Automator Integration:**

1. **Convert Automator to Shortcuts** (native macOS feature)
   - Drag Automator workflow file into Shortcuts app
   - Automatic conversion to Shortcut
   - Run via keyboard shortcut

2. **Create Custom Workflows**
   - Use "Run Shell Script" action
   - Execute curl commands to Notion API
   - Automate file uploads from specific folders

**Example Automator Workflow for Study Guides:**

```
Workflow: "Auto-Upload Source Files to Notion"

Step 1: Watch folder for new .txt files (~/Documents/Pharmacy/Source Files)
Step 2: When new file detected, run shell script
Step 3: Shell script calls Notion API with file upload
Step 4: Create database entry with file attached
Step 5: Move file to "Uploaded" folder
```

### Advanced: Notion API via Terminal/Shell Scripts

**For maximum control**, use shell scripts with `curl` to interact with Notion API.

**Example: Upload file and create database entry**

```bash
#!/bin/bash
# upload-to-notion.sh

# 1. Create file upload object
UPLOAD_RESPONSE=$(curl -X POST https://api.notion.com/v1/files \
  -H "Authorization: Bearer YOUR_NOTION_API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json")

# 2. Extract upload URL and file ID
UPLOAD_URL=$(echo $UPLOAD_RESPONSE | jq -r '.upload_url')
FILE_ID=$(echo $UPLOAD_RESPONSE | jq -r '.id')

# 3. Upload file
curl -X PUT "$UPLOAD_URL" \
  --upload-file "$1"

# 4. Create database entry with attached file
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer YOUR_NOTION_API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": { "database_id": "YOUR_DATABASE_ID" },
    "properties": {
      "Title": { "title": [{ "text": { "content": "'"$2"'" } }] },
      "Source File": { "files": [{ "file": { "id": "'"$FILE_ID"'" } }] }
    }
  }'
```

**Run with:** `./upload-to-notion.sh source_file.txt "Lecture 42"`

### Third-Party Mac Tools

**Nautomate** (Paid but affordable)
- Mac app specifically for Notion automation
- Drag-and-drop interface
- Create rich pages automatically
- No Zapier needed
- **Price**: One-time purchase (check website)

---

## Popular Notion Integrations

### Top 5 Most Used Integrations

1. **Google Calendar** - Sync events to Notion databases
2. **Slack** - Send notifications, create pages from messages
3. **Google Sheets** - Two-way sync with Notion databases
4. **Discord** - Post updates to Discord from Notion
5. **OneNote** - Import notes to Notion

### Study Guide Specific Integrations

**For Pharmacy Students:**

1. **Google Drive**
   - Auto-upload lecture PDFs to Notion
   - Store source files in Drive → auto-create Notion entry

2. **Gmail**
   - Email lecture notes → auto-add to database
   - Professor sends syllabus → auto-create study guide entry

3. **Everhour** (Time Tracking)
   - Track study time per subject
   - Log hours spent on each study guide

4. **Todoist**
   - Sync exam deadlines to Notion
   - Create task for each learning objective

5. **Anki**
   - Export Notion notes to Anki flashcards
   - (Requires custom integration via Make/n8n)

---

## Step-by-Step Setup Guides

### Option 1: Make.com Setup (Recommended for Beginners)

**Step 1: Create Make.com Account**
```
1. Go to make.com
2. Sign up with email (free plan)
3. Verify email
```

**Step 2: Connect Notion to Make**
```
1. In Make dashboard, click "Create new scenario"
2. Click "+" to add module
3. Search "Notion"
4. Click "Create a connection"
5. Authorize Make to access your Notion workspace
```

**Step 3: Create Your First Automation**

**Example: "Google Drive Upload → Notion Database Entry"**

```
Module 1: Google Drive - Watch Files in Folder
- Select folder: "Pharmacy/Source Files"
- Trigger: When new file added

Module 2: Notion - Create Database Item
- Database: "Study Guides Master Database"
- Title: {{file name}}
- Source File: {{file download URL}}
- Status: "Not Started"
- Subject: (set default or extract from folder name)

Module 3: Google Drive - Move File
- Move to: "Pharmacy/Uploaded Files"
```

**Step 4: Test and Activate**
```
1. Click "Run once" to test
2. Upload test file to Google Drive folder
3. Verify Notion entry created
4. Click "Scheduling" → "ON" to activate
```

### Option 2: n8n Setup (Advanced - Unlimited Free)

**Step 1: Install n8n on Mac**

**Via Homebrew (easiest):**
```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Node.js
brew install node

# Install n8n globally
npm install n8n -g

# Start n8n
n8n start
```

**n8n will run at:** `http://localhost:5678`

**Step 2: Connect Notion**
```
1. Open http://localhost:5678
2. Create new workflow
3. Add "Notion" node
4. Create credentials:
   - Go to notion.so/my-integrations
   - Create new integration
   - Copy Internal Integration Token
   - Paste into n8n credentials
```

**Step 3: Create File Upload Workflow**

**Example workflow:**
```
Node 1: Webhook Trigger
- Listen for file upload from Mac Automator or folder watch

Node 2: HTTP Request - Upload to Notion
- Method: POST
- URL: https://api.notion.com/v1/files
- Authentication: Notion credentials
- Body: File binary

Node 3: Notion - Create Database Page
- Database: Study Guides
- Properties: Map file info to database fields

Node 4: Move File - Execute Command
- Command: mv {{file_path}} ~/Documents/Archived/
```

**Step 4: Keep n8n Running**

**Option A: Run when needed**
```bash
n8n start
# Keep terminal window open
```

**Option B: Run as background service** (always on)
```bash
# Install PM2 (process manager)
npm install pm2 -g

# Start n8n with PM2
pm2 start n8n

# Set to start on Mac boot
pm2 startup
pm2 save
```

### Option 3: Apple Shortcuts (Simple, No Third-Party Tools)

**Step 1: Get Notion API Key**
```
1. Go to notion.so/my-integrations
2. Click "Create new integration"
3. Name: "Study Guide Uploader"
4. Copy Internal Integration Token
```

**Step 2: Share Database with Integration**
```
1. Open your "Study Guides" database in Notion
2. Click "..." menu → "Connections"
3. Add "Study Guide Uploader" integration
```

**Step 3: Create Shortcut**

**Shortcut: "Upload Study Guide Source File"**

```
Actions:
1. Get File (from Finder)
2. Get text from input
3. Set variable: FileName to input
4. Text: Create JSON body (manual entry of Notion API call)
5. Get Contents of URL:
   - URL: https://api.notion.com/v1/pages
   - Method: POST
   - Headers:
     * Authorization: Bearer YOUR_API_TOKEN
     * Notion-Version: 2022-06-28
     * Content-Type: application/json
   - Request Body: JSON (properties for database)
6. Show Notification: "File uploaded to Notion"
```

**Step 4: Add to Menu Bar or Keyboard Shortcut**
```
1. In Shortcuts app, right-click shortcut
2. "Add to Menu Bar"
3. Or assign keyboard shortcut (e.g., Cmd+Shift+N)
```

---

## Recommended Workflow for Study Guides

### Hybrid Approach: Claude Code + Make.com + Notion

**Why this combination works best:**

1. **Claude Code** - Generate study guides (Word/Excel/HTML)
2. **Make.com** - Automate file organization and Notion updates
3. **Notion** - Track progress, organize files, search/reference

### Complete Automation Setup

**Workflow 1: Source File Upload**

```
When: New .txt file added to ~/Documents/Pharmacy/Source Files/

Automation (Make.com):
1. Detect new file
2. Upload file to Notion API (20 MB limit)
3. Create entry in "Study Guides Master Database":
   - Title: Filename
   - Source File: Uploaded file
   - Status: "Not Started"
   - Subject: Extract from folder name
4. Move original file to "Uploaded" folder
5. Send notification (optional)
```

**Workflow 2: Study Guide Completion**

```
When: Study guide created by Claude Code

Manual step:
1. Upload completed .docx/.xlsx/.html to Notion database entry

Automation (Make.com):
1. Detect file upload to "Output File" property
2. Update Status to "Needs Verification"
3. Send Slack/Discord notification (optional)
4. Create calendar reminder for verification (optional)
```

**Workflow 3: Mnemonic Library Update**

```
When: New mnemonic discovered during study guide creation

Manual step:
1. Add to "Medical Mnemonics" database in Notion

Automation (Make.com):
1. When new entry added
2. Cross-reference with "Study Guides" database
3. Update "Used In" relation field
4. Tag with subject/topic automatically
```

### Mac Automator Integration

**Folder Action: Auto-Upload Source Files**

```
Create Automator Folder Action:

1. Right-click folder: ~/Documents/Pharmacy/Source Files
2. Services → Folder Actions Setup
3. Attach script: "Upload to Notion"

Script runs:
- When file added to folder
- Calls Make.com webhook URL
- Make.com handles Notion upload
```

**Keyboard Shortcut: Create Study Guide Entry**

```
Create Automator Quick Action:

1. Workflow receives: Files or Folders (from Finder)
2. Run Shell Script:
   - Pass input: as arguments
   - Script: Call Make.com webhook with file path
3. Display notification: "Study guide entry created"

Assign keyboard shortcut:
System Preferences → Keyboard → Shortcuts → Services
Assign: Cmd+Shift+S to "Create Study Guide Entry"
```

---

## Cost Comparison

### Free Options

| Tool | Free Tier | Best For |
|------|-----------|----------|
| Make.com | 1,000 operations/month | Most students ✅ |
| n8n (self-hosted) | Unlimited | Technical users |
| Zapier | 100 tasks/month | Basic testing |
| Apple Shortcuts | Unlimited | Simple automation |
| Notion (free plan) | 5 MB file uploads | Starting out |

**Recommended for pharmacy students:** Make.com free tier (1,000 operations is plenty)

### Paid Options (If You Need More)

| Tool | Price | Operations/Month | Value |
|------|-------|-----------------|-------|
| Make.com | $10.59/month | 10,000 | ⭐⭐⭐⭐⭐ |
| Zapier | $19.99/month | 750 tasks | ⭐⭐⭐ |
| n8n Cloud | $24/month | 2,500 executions | ⭐⭐⭐⭐ |
| Notion Plus | $10/month | Unlimited file uploads | ⭐⭐⭐⭐ |

**Best value if you need paid:** Make.com ($10.59) + Notion Plus ($10) = $20.59/month total

---

## Quick Setup Checklist

**For pharmacy student using Mac + Claude Code + Notion:**

### Phase 1: Accounts (Free)
- [ ] Create Notion account (free plan)
- [ ] Create Make.com account (free tier)
- [ ] Create Notion integration at notion.so/my-integrations
- [ ] Copy integration token (save in secure note)

### Phase 2: Notion Setup
- [ ] Create "Study Guides Master Database" (use template from NOTION_AI_SETUP_GUIDE.md)
- [ ] Create "Medical Mnemonics" database
- [ ] Create "Source Files" database
- [ ] Share all databases with your integration

### Phase 3: Make.com Automation
- [ ] Connect Notion to Make.com
- [ ] Create Scenario: "Google Drive → Notion Database"
- [ ] Test with one source file
- [ ] Activate automation

### Phase 4: Mac Automator (Optional)
- [ ] Create folder action for ~/Documents/Pharmacy/Source Files
- [ ] Create keyboard shortcut for quick entry creation
- [ ] Test automation

### Phase 5: Test Complete Workflow
- [ ] Upload source .txt file to Google Drive
- [ ] Verify Notion entry created automatically
- [ ] Use Claude Code to create study guide
- [ ] Upload completed study guide to Notion entry
- [ ] Mark status as "Complete"

---

## Troubleshooting

### Common Issues

**Issue: Make.com scenario not triggering**
- Check: Scenario is "ON" (switch in top right)
- Check: Google Drive connection still valid
- Check: Folder path is correct
- Test: Click "Run once" manually

**Issue: Notion API returning 401 Unauthorized**
- Check: Integration token is correct
- Check: Database is shared with integration (Connections settings)
- Check: Token hasn't been regenerated (old token invalid)

**Issue: File upload fails (too large)**
- Notion API limit: 20 MB max
- Notion free plan in-app: 5 MB max
- Solution: Use Notion API upload (20 MB) or upgrade to Notion Plus (unlimited)

**Issue: Mac Automator workflow not running**
- Check: Folder Actions is enabled in System Preferences
- Check: Folder is actually being watched (green indicator)
- Check: Script has execute permissions (`chmod +x script.sh`)

**Issue: Apple Shortcut API call fails**
- Check: Notion-Version header is "2022-06-28" (current version)
- Check: JSON body is properly formatted (use jsonlint.com)
- Check: Database ID is correct (copy from database URL)

---

## Additional Resources

### Official Documentation
- [Notion API Reference](https://developers.notion.com/reference)
- [Notion File Upload Guide](https://developers.notion.com/docs/uploading-small-files)
- [Make.com Notion Modules](https://www.make.com/en/help/app/notion)
- [n8n Notion Integration](https://n8n.io/integrations/notion/)
- [Apple Shortcuts User Guide](https://support.apple.com/guide/shortcuts-mac)

### Tutorials
- [Thomas Frank - Notion Automations Guide](https://thomasjfrank.com/notion-automations/)
- [Make.com Notion Integration Tutorial](https://www.make.com/en/integrations/notion)
- [n8n Notion Workflow Examples](https://n8n.io/workflows/?categories=Notion)

### Community
- [r/Notion Reddit](https://reddit.com/r/Notion) - Automation tips
- [Notion Discord](https://discord.gg/notion) - Help and templates
- [Make.com Community](https://community.make.com) - Scenario sharing

---

## Summary & Recommendation

### For Pharmacy Students Creating Study Guides on Mac

**Best Setup (All Free):**

1. **Make.com** (free tier) - Handle file uploads and database automation
2. **Notion** (free plan) - Organize and track study guides
3. **Claude Code** - Generate actual study guide files
4. **Apple Shortcuts** (optional) - Quick capture and keyboard shortcuts

**Total Cost: $0/month**

**Upgrade If Needed:**
- Notion Plus ($10/month) - For unlimited file uploads and collaboration
- Make.com Core ($10.59/month) - If you exceed 1,000 operations (unlikely for most students)

**Total Cost (Paid): $20.59/month** - Only if you need it

### Why This Setup Works

✅ **Free for most students** (1,000 Make operations = plenty)
✅ **No coding required** (visual workflow builder)
✅ **Mac-native** (works seamlessly with Automator and Shortcuts)
✅ **Scalable** (upgrade only if needed)
✅ **Integrates with Claude Code** (your existing system)

---

**Next Step:** Follow the Quick Setup Checklist above to get started in 30 minutes.
