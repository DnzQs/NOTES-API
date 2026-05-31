# Notes API

A simple RESTful Notes API built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Docker.

# Features
User registration
User authentication with JWT
Password hashing using bcrypt
Create notes
Get all notes
Get a single note
Update notes
Delete notes
User ownership protection (users can only access their own notes)
PostgreSQL database
Docker support
API documentation with Swagger UI

# Tech Stack
Python 3.11+
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
JWT (python-jose)
Passlib (bcrypt)
Docker
Pytest

# Project Structure
app/
routes/
models.py
schemas.py
db.py
utils.py
main.py

# Installation
Clone repository
git clone https://github.com/yourusername/notes-api.git
cd notes-api
Create virtual environment
python -m venv .venv
Activate virtual environment

Windows:

.venv\Scripts\activate

Linux/macOS:

source .venv/bin/activate
Install dependencies
pip install -r requirements.txt
# Environment Variables

Create a .env file:

DATABASE_URL=postgresql://your_db:your_db@localhost:5432/notes_api_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256

# Run Project
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs

# Docker

Build and run:

docker-compose up --build

Swagger documentation:

http://localhost:8000/docs

# Authentication

Protected endpoints require JWT token:

Authorization: Bearer YOUR_ACCESS_TOKEN

# Running Tests
pytest

Author: Kolesnichenko Denis
