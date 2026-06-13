# 🤖 AI HelpDesk

An AI-powered Customer Support Ticket Management System built using Django REST Framework and Groq AI.

---

## 📖 Overview

AI HelpDesk is a smart complaint management platform that allows customers to create support tickets and receive AI-generated categorization and response suggestions. Administrators can manage tickets, monitor complaint statistics, and update ticket statuses through a dedicated admin dashboard.

---

## ✨ Features

### Customer Features

* User Registration
* User Login (Username or Email)
* JWT Authentication
* Create Support Tickets
* View Personal Tickets
* Track Ticket Status
* AI-Powered Ticket Categorization
* AI-Generated Response Suggestions

### Admin Features

* View All Tickets
* Dashboard Statistics
* Update Ticket Status
* Manage Customer Complaints

### AI Features

* Automatic Complaint Categorization
* Intelligent Response Suggestions
* Groq LLM Integration

---

## 🛠️ Tech Stack

### Backend

* Python
* Django
* Django REST Framework
* Simple JWT

### Frontend

* HTML
* CSS
* JavaScript

### AI

* Groq API
* Llama 3.3 70B Versatile

### Database

* SQLite

### Documentation

* Swagger (drf-spectacular)

---

## 🚀 Project Workflow

Customer

→ Register

→ Login

→ Create Ticket

→ AI Categorization

→ AI Suggestion Generation

→ View Ticket

↓

Admin

→ Login

→ View All Tickets

→ Update Ticket Status

↓

Customer

→ View Updated Status

---

## 📂 Project Structure

```text
ai_helpdesk/

├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── tickets/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── ai.py
│   └── client.py
│
├── frontend/
│   ├── templates/
│   └── views.py
│
├── static/
│   ├── css/
│   └── js/
│
├── manage.py
└── requirements.txt
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Aswana001/AI_HELPDESK.git

cd ai-helpdesk
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env

```env
GROQ_API_KEY=your_groq_api_key
```

### Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint                |
| ------ | ----------------------- |
| POST   | /api/accounts/register/ |
| POST   | /api/accounts/login/    |

### Tickets

| Method | Endpoint                         |
| ------ | -------------------------------- |
| POST   | /api/tickets/create/             |
| GET    | /api/tickets/my-tickets/         |
| GET    | /api/tickets/all/                |
| PATCH  | /api/tickets/<id>/update-status/ |
| GET    | /api/tickets/dashboard/          |

---

## 📚 API Documentation

Swagger Documentation:

```text
http://127.0.0.1:8000/api/docs/
```

---

## 🔐 Authentication

The project uses JWT Authentication.

After login:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

Use the access token:

```http
Authorization: Bearer <access_token>
```

---

## 🎯 Future Enhancements

* Email Notifications
* File Attachments
* Ticket Priority Prediction
* Sentiment Analysis
* Real-Time Notifications
* Advanced Analytics Dashboard

---

## 👩‍💻 Author

**Aswana Ashok**

B.Tech Computer Science Engineering

AI HelpDesk Project
