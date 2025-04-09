# 📝 Task Management API (Backend Only)

A simple backend-only RESTful API for managing personal tasks, built with Flask and MongoDB.

---

## 🚀 Project Overview

This project is a backend API that allows users to:
- Register and log in with JWT-based authentication
- Create, read, update, and delete personal tasks
- Authenticate requests using JWT tokens

---

## 🧰 Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB
- **Authentication:** JWT (JSON Web Tokens)
- **Deployment:** Render

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/tarun00710/task-management-BE
   cd task-management-BE
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following content:
   ```env
   MONGO_URI=<your_mongodb_uri>
   JWT_SECRET_KEY=<your_jwt_secret>
   ```

5. **Run the server locally**
   ```bash
   python app.py
   ```
   The server will start at `http://localhost:5000`

---

## 🌐 Deployed API

- **Base URL:** [`https://task-management-be-a7mn.onrender.com/`](https://task-management-be-a7mn.onrender.com/)

---

## 🔐 Authentication

- Register to get an account
- Login to get a JWT access token

### Sample Token (Valid for 15 mins)
```bash
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDIwOTE4MiwianRpIjoiMGM5YmQ1NzgtOTAxZi00MDc5LTg1ZDctN2JjNWMwMWUxNjk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY3ZjY4NTEwZTAzOWUzZTkyNjU1ZTU4YiIsIm5iZiI6MTc0NDIwOTE4MiwiY3NyZiI6ImM1YTIxNWI5LWQ1MjEtNDQ4ZC04ZGE3LTM3NjE0YmJkYjk0MSIsImV4cCI6MTc0NjgwMTE4Mn0.WruEfMoaMPBtzu_Z8lbqw1P7EUvQ33_aWb5O1it9wlY
```

### Sample User
```json
{
  "email": "sample@example.com",
  "password": "123456"
}
```

---

## 📮 API Endpoints (with examples)

### ✅ Register
**POST** `/api/auth/register`
```json
{
  "email": "sample@example.com",
  "password": "123456"
}
```
**Response**
```json
{
  "msg": "User registered",
  "user_id": "<mongo_object_id>"
}
```

### 🔓 Login
**POST** `/api/auth/login`
```json
{
  "email": "sample@example.com",
  "password": "123456"
}
```
**Response**
```json
{
  "access_token": "<JWT token>"
}
```

### 📝 Create Task
**POST** `/tasks`
- Headers:
```bash
Authorization: Bearer <JWT token>
```
- Body:
```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending"
}
```

### 📋 Get All Tasks
**GET** `/tasks`
- Headers:
```bash
Authorization: Bearer <JWT token>
```
**Response**
```json
[
  {
    "_id": "...",
    "user_id": "...",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "status": "pending"
  }
]
```

### ✏️ Update Task
**PUT** `/tasks/<task_id>`
```json
{
  "title": "Buy veggies",
  "description": "Carrots and onions",
  "status": "completed"
}
```

### ❌ Delete Task
**DELETE** `/tasks/<task_id>`

---

## 📫 Postman Collection

- Download or import from this link:
[Postman Collection Link](https://.postman.co/workspace/My-Workspace~edf3b47b-f1a0-4cac-8f60-1e74ea90dd8f/collection/20770043-ed91a689-57bf-432d-9d27-795202e8b2d8?action=share&creator=20770043&active-environment=20770043-9917f726-8662-4469-bba4-44f3a43ffaaf)

✅ Be sure to include the Bearer token in the `Authorization` header when testing protected routes or Click environment variables and select Flask_test and then run the protected apis as I have already created and attached required token in this.

---

## ☁️ Deployment Details

- Hosting: [Render](https://render.com)
- Auto-deployed via GitHub repo: [`https://github.com/tarun00710/task-management-BE`](https://github.com/tarun00710/task-management-BE)
- Start command (used by Render): `gunicorn app:app`

---


