# 🎓 CollegeBot Maharashtra — Engineering College Assistant

> A fully functional, mobile-responsive Maharashtra Engineering College web app with integrated AI chatbot.

---

## 🚀 Live Features

| Feature | Status |
|---|---|
| Hero Section with animated gradient | ✅ |
| Animated stats counters (Intersection Observer) | ✅ |
| 10 College Cards with full data | ✅ |
| Quick Question Chips → Auto-send to chatbot | ✅ |
| Sortable Comparison Table | ✅ |
| Built-in AI Chatbot (local knowledge base) | ✅ |
| Dialogflow REST API integration hook | ✅ |
| Mobile responsive + hamburger menu | ✅ |
| Smooth scroll, hover animations | ✅ |

---

## 📁 File Structure

```
webapp/
├── index.html       ← Everything in one file (HTML + CSS + JS)
└── README.md        ← This file
```

---

## 🔌 Connecting Your Dialogflow Agent

The chatbot currently uses a **local built-in knowledge base** that works offline.
To connect your existing `MaharashtraCollegeAssistant` Dialogflow ES agent, follow these steps:

### Option A — Dialogflow Messenger (Easiest)

1. Go to your [Dialogflow ES Console](https://dialogflow.cloud.google.com/)
2. Open your `MaharashtraCollegeAssistant` agent
3. Go to **Integrations → Dialogflow Messenger**
4. Enable it and copy your `project-id` and `agent-id`
5. In `index.html`, find the comment `<!-- DIALOGFLOW MESSENGER (Option A) -->` and uncomment the block:

```html
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.min.css">
<df-messenger
  project-id="YOUR_PROJECT_ID"
  agent-id="YOUR_AGENT_ID"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat-bubble chat-title="College Assistant">
  </df-messenger-chat-bubble>
</df-messenger>
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
```

### Option B — REST API (Custom Chat UI — Already Built)

In `index.html`, find the `getCollegeResponse()` function and replace its call with:

```javascript
async function sendToDialogflow(userMessage) {
  const sessionId = "user-" + Date.now();
  const response = await fetch(
    `https://dialogflow.googleapis.com/v2/projects/YOUR_PROJECT_ID/agent/sessions/${sessionId}:detectIntent`,
    {
      method: "POST",
      headers: {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        queryInput: {
          text: { text: userMessage, languageCode: "en" }
        }
      })
    }
  );
  const data = await response.json();
  return { text: data.queryResult.fulfillmentText, quickReplies: [] };
}
```

Then update the `sendMessage()` function to call `sendToDialogflow()` instead of `getCollegeResponse()`.

> ⚠️ **Note:** For production, never expose your access token in frontend code. Use a backend proxy (Cloud Function or Express endpoint) to secure API calls.

---

## 🌐 Deployment

### GitHub Pages
```bash
# From your repo root
git add MaharashtraCollegeAssistant/webapp/
git commit -m "Add College Assistant webapp"
git push origin main
# Enable GitHub Pages → root or /docs
```

### Netlify (drag & drop)
1. Go to [netlify.com](https://netlify.com)
2. Drag the `webapp/` folder into the deploy zone
3. Done — instant live URL!

### Vercel
```bash
npx vercel MaharashtraCollegeAssistant/webapp/
```

---

## 🗂️ College Data Included

| College | City | Type |
|---|---|---|
| COEP Technological University | Pune | Government |
| VJTI Mumbai | Mumbai | Government |
| PICT Pune | Pune | Private |
| SPIT Mumbai | Mumbai | Private |
| DJ Sanghvi Mumbai | Mumbai | Private |
| VNIT Nagpur | Nagpur | Government |
| VIT Pune | Pune | Private |
| MIT WPU Pune | Pune | Private |
| ICT Mumbai | Mumbai | Autonomous |
| Walchand Sangli | Sangli | Government |

---

## 📊 Chatbot Capabilities

The built-in chatbot handles:
- Individual college info (fees, placement, cutoff, ranking, review)
- College comparisons (`Compare COEP and VJTI`)
- Best college recommendations (CSE, placement, package)
- Government college filter
- City-wise filtering (Mumbai, Pune)
- Lowest cutoff / cheapest fees queries
- Highest package queries

---

## ⚠️ Disclaimer

Data sourced from official college websites & MHT-CET records (2024-25 cycle).
For official cutoffs visit: [cetcell.mahacet.org](https://cetcell.mahacet.org)
This chatbot is for informational purposes only.
