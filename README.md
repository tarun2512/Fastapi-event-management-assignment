# 📅 Event Management API (FastAPI + PostgreSQL)

A clean and scalable backend microservice for managing events and attendees using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

---

## 🚀 Overview

This microservice allows:

- Creating and listing events
- Registering attendees with email uniqueness
- Enforcing event capacity limits
- Viewing event attendees with pagination

The architecture uses SQLAlchemy for ORM, PostgreSQL for data storage, and FastAPI for building modern, asynchronous APIs.

---

## 🧱 Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy (with `create_all()` for auto-table generation)
- **Driver**: `psycopg2-binary`
- **Validation**: Pydantic
- **Docs**: Swagger (auto-generated by FastAPI)

---

## 📦 Folder Structure

```
.
├── app.py                  # 🚀 Entry point of the microservice
├── main.py                 # 🧩 Registers middlewares and API routers
├── requirements.txt        # 📦 Python dependencies
├── README.md               # 📘 Project documentation

├── scripts/                # 📂 Core application directory
│   ├── api/                # 📡 Endpoint declarations (FastAPI routers)
│   ├── config/             # ⚙️  Environment variable management and settings
│   ├── constants/          # 📌 Constant values and response messages
│   ├── db/                 # 🛢️  DB engine creation, session, and model declarations
│   ├── handlers/           # 🧠 Core business logic and reusable service functions
│   ├── logger/             # 📜 Logging configuration and utilities
│   ├── schema/             # 📐 Pydantic models for request/response validation
│   ├── services/           # 🛠️  High-level API logic calling handler functions

```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/event-management-api.git
cd event-management-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Ensure PostgreSQL is running.

Create database manually or using:

```bash
createdb event_db
```

Update your `POSTGRES_URL` (used in `.env`):

```bash
export DATABASE_URL="postgresql://#:#@localhost/event_db"
```

For Windows (CMD):

```cmd
set DATABASE_URL=postgresql://postgres:password@localhost/event_db
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

Access the API:

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## 🔁 Auto Table Creation

SQLAlchemy auto-generates tables when the app starts using:

```python
Base.metadata.create_all(bind=engine)
```

No separate migration command is required for initial setup.

---

## ✅ API Endpoints

### 🎉 Create Event

```http
POST /events
Content-Type: application/json

{
  "name": "Hackathon 2025",
  "location": "Chennai",
  "start_time": "2025-08-15T09:00:00",
  "end_time": "2025-08-15T17:00:00",
  "max_capacity": 200
}
```

### 📋 List Events

```http
GET /events
```

### 👤 Register Attendee

```http
POST /events/1/register
Content-Type: application/json

{
  "name": "Tarun",
  "email": "tarun@example.com"
}
```

If event is full or email already registered, it returns an error.

### 👥 List Attendees

```http
GET /events/1/attendees?limit=5&offset=0
```

Supports pagination using `limit` and `offset`.

---

## ⚠️ Assumptions

- An email can register for an event only once.
- Event capacity is strictly enforced.
- Timezones are assumed to be UTC (you can extend for full timezone support).
- Events are listed in ascending order by start time.

---

## 🧪 Testing

You can manually test using:

- Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Postman / curl

Unit testing with `pytest` can be added.

---

## 🧠 Future Enhancements

- JWT-based authentication
- Email confirmations
- Celery integration for async tasks
- Role-based access
- Docker support

---