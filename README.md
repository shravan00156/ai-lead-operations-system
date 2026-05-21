# AI Lead Operations System

AI-powered backend operations system built using FastAPI, PostgreSQL, AI lead scoring workflows, and operational automation architecture.

---

# Project Overview

This project is designed to simulate a real-world lead operations backend system used by startups, agencies, and SaaS businesses.

The system handles:

- Lead management
- AI-based lead scoring
- Priority classification
- PostgreSQL data storage
- API-based operations
- Dashboard analytics
- Notification workflows

This project focuses on backend engineering + automation system architecture.

---

# Features

## Backend API
- FastAPI backend
- REST API endpoints
- CRUD operations
- Modular architecture

## Database Layer
- PostgreSQL integration
- Table initialization
- Persistent lead storage
- SQL queries

## AI Workflow Layer
- AI lead scoring
- Priority classification
- Operational intelligence

## Automation Layer
- Telegram notification workflow
- Operational processing flow

## Dashboard
- Streamlit dashboard
- Lead visualization
- Priority analytics

---

# Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | PostgreSQL |
| Language | Python |
| Dashboard | Streamlit |
| AI Logic | OpenAI-style scoring workflow |
| API Testing | Swagger UI |
| Version Control | Git + GitHub |

---

# Folder Structure

```txt
ai_lead_operations_system/
│
├── database/
│   ├── connection.py
│   ├── init_db.py
│   ├── models.py
│   └── queries.py
│
├── routes/
│   └── lead_routes.py
│
├── services/
│   ├── ai_service.py
│   └── telegram_service.py
│
├── utils/
│   └── helpers.py
│
├── dashboard.py
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

---

# System Architecture

```txt
Client
   ↓
FastAPI API Layer
   ↓
Service Layer
   ↓
PostgreSQL Database
   ↓
AI Scoring + Notification Layer
   ↓
Dashboard Analytics
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/leads` | Create lead |
| GET | `/leads` | Get all leads |
| GET | `/leads/{id}` | Get single lead |
| DELETE | `/leads/{id}` | Delete lead |

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/shravan00156/ai-lead-operations-system.git
```

---

## 2. Move Into Project

```bash
cd ai-lead-operations-system
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure PostgreSQL

Create PostgreSQL database:

```sql
CREATE DATABASE ai_lead_ops;
```

Update database password inside:

```txt
database/connection.py
```

---

## 5. Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

## 6. Open Swagger Docs

```txt
http://127.0.0.1:8000/docs
```

---

## 7. Run Dashboard

```bash
streamlit run dashboard.py
```

---

# Example Lead Payload

```json
{
  "name": "Shravan",
  "email": "shravan@gmail.com",
  "company": "AI FinTech",
  "source": "linkedin"
}
```

---

# Future Improvements

- APScheduler integration
- Follow-up automation
- Retry workflows
- Docker deployment
- Render/Railway deployment
- Authentication system
- AI memory/context layer

---

# Learning Outcomes

This project helped develop understanding of:

- Backend engineering
- API architecture
- Database integration
- Operational workflows
- AI automation systems
- Service-based architecture
- CRUD operations
- System debugging

---

# Author

Shravan

GitHub:
https://github.com/shravan00156
