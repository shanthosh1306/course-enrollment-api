# Course Enrollment System – Django REST API

## Overview
This project is a simple **Course Enrollment System** built using **Django** and **Django REST Framework**. It allows creating courses, students, and enrolling students into courses through RESTful APIs.

## Setup
1. Clone repository
2. Create virtual environment
3. Install dependencies:
   pip install django djangorestframework
4. Run migrations:
   python manage.py migrate
5. Start server:
   python manage.py runserver

## API Endpoints
- POST /api/courses/
- GET /api/courses/
- POST /api/students/
- POST /api/enrollments/
- GET /api/enrollments/list/

## Tech Stack
- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- Git & GitHub

## Notes
- Postgresql was used 
- Admin panel enabled
