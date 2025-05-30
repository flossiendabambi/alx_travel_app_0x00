# ALX Travel App 

A backend travel application built with Django and Django REST Framework as part of the ALX Backend Pro Dev program.

## 🔍 Overview

This project provides RESTful API endpoints to manage users, conversations, and messages for a travel-related application. It uses custom user models, viewsets, and nested routes to organize chat-based interactions.

## ⚙️ Features

- ✅ Custom `User` model using UUID
- 💬 Create and manage Conversations
- 📨 Send and view Messages in Conversations
- 🔒 Token-based Authentication with `IsAuthenticated` permissions
- 🔁 Nested routing for clean URL structure
- 📄 DRF Serializers with nested relationships

## 🛠️ Tech Stack

- Python 3
- Django 4
- Django REST Framework
- drf-nested-routers
- MySQL (or SQLite for dev)
- Docker (optional setup)

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/<your-username>/alx-travel-app.git
cd alx-travel-app

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
