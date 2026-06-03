# 🎫 Issue Tracker & Support Ticket System

A Jira-style Issue Tracker web application built with Python Flask and SQLite.

🌐 **Live Demo:** [https://issue-tracker-6uwh.onrender.com](https://issue-tracker-6uwh.onrender.com)
📂 **GitHub:** [https://github.com/BKeerthi975/issue-tracker](https://github.com/BKeerthi975/issue-tracker)

---

## 📌 About
This project simulates a real-world support ticket management system where issues can be created, tracked, and resolved — similar to enterprise tools like Jira used by software teams worldwide. Built as a portfolio project to demonstrate full-stack Python web development skills.

---

## ✨ Features
- ✅ Create tickets with title, description, priority and assignee
- ✅ Track ticket status — Open, In Progress, Resolved
- ✅ Color-coded priority badges — High (red), Medium (yellow), Low (green)
- ✅ Update ticket status in real time
- ✅ Delete resolved tickets with confirmation
- ✅ Dashboard with live bar charts showing ticket statistics
- ✅ Responsive UI using Bootstrap 5
- ✅ Fully deployed and accessible online 24/7

---

## 🛠️ Tech Stack
| Technology | Usage |
|---|---|
| Python 3 | Backend logic |
| Flask | Web framework |
| SQLite | Database |
| HTML5 + CSS3 | Frontend structure and styling |
| Bootstrap 5 | Responsive UI components |
| Chart.js | Dashboard bar charts |
| Render | Cloud deployment |
| Git + GitHub | Version control |

---

## 📁 Project Structure
issue_tracker/
├── app.py                  ← Main Flask application
├── database.py             ← Database connection and setup
├── requirements.txt        ← Python dependencies
├── templates/
│   ├── base.html           ← Common navbar and layout
│   ├── index.html          ← All tickets list page
│   ├── create.html         ← Create new ticket form
│   ├── update.html         ← Update ticket status page
│   └── dashboard.html      ← Charts and statistics
└── static/
└── style.css           ← Custom CSS styles
---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/BKeerthi975/issue-tracker.git
cd issue-tracker

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser and go to: **http://127.0.0.1:5000**

---

## 📸 Screenshots

### All Tickets Page
Shows all tickets in a table with color-coded priority and status badges.

### Dashboard
Live bar chart showing ticket counts by status — Open, In Progress, Resolved.

---

## 🌐 Live Demo
👉 [https://issue-tracker-6uwh.onrender.com](https://issue-tracker-6uwh.onrender.com)

> Note: Hosted on Render free tier — may take 30-50 seconds to load on first visit after inactivity.

---

## 👩‍💻 Author
**B Keerthi**
- 📧 bkeerthi975@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/b-keerthi-245449332)
- 🐙 [GitHub](https://github.com/BKeerthi975)

---

## 📄 License
This project is open source and available for learning purposes.
