# alx_travel_app_0x01

An Airbnb-inspired travel backend platform built with Django.  
Manage listings, bookings, and reviews via RESTful APIs.
---

## 🚀 Project Overview

This project provides a foundation for managing travel accommodations, with models for Listings, Bookings, and Reviews. It includes serializers for API data handling and a management command to seed the database with sample data.
---

## ⚙️ Features

- **Listings:** Create and manage rental properties with details.
- **Bookings:** Users can book listings by selecting availability.
- **Reviews:** One review per user per listing with ratings.
- **API Serializers:** Convert models to/from JSON for API responses.
- **Seeder Command:** Easily populate DB with realistic sample listings.
---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.x  
- MySQL Server (or adjust to your preferred DB backend)  
- Git

### Clone the repository

git clone <your-repo-url>
cd alx_travel_app_0x00

### Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Configure environment variables

Create a `.env` file in the project root with the following variables:

DJANGO_SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

MYSQL_DATABASE=your_database_name
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306

> **Note:** Replace values with your actual settings.  
> The `.env` file is loaded by the project (make sure to configure `django-environ` or similar).
---

### Database setup

Ensure your MySQL server is running and the database exists:

CREATE DATABASE your_database_name;
---

### Apply migrations

Generate and apply migrations for the models:

python manage.py makemigrations listings
python manage.py migrate
---

### Seed the database with sample data

Run the custom seeder command:

python manage.py seed

This creates sample listings linked to a default host user.
---

### Run the development server

python manage.py runserver

Open [http://localhost:8000](http://localhost:8000) to explore your API.
---

## 📖 API Documentation
Interactive API documentation is auto-generated with Swagger/OpenAPI using drf-yasg:

Swagger UI: http://localhost:8000/swagger/
Try out endpoints interactively with clear request/response details.

ReDoc UI: http://localhost:8000/redoc/
Alternative clean API docs presentation.

### OpenAPI Spec:

JSON: /swagger.json

YAML: /swagger.yaml

You can download the OpenAPI spec above to import into tools like Postman.

### 🔧 Usage
Interact with your API endpoints, e.g.:

| Endpoint             | HTTP Method | Description                     |
|----------------------|-------------|---------------------------------|
| /api/listings/       | GET         | List all listings               |
| /api/listings/{id}/  | GET         | Get details for a single listing|
| /api/bookings/       | POST        | Create a new booking            |
| /api/reviews/        | POST        | Submit a listing review         |

>Use authentication via Django REST Framework's session login available at /api-auth/login/.

### 🧪 Testing the API with Postman
Download your API specification:
http://localhost:8000/swagger.json or swagger.yaml.

Open Postman → Click Import → Upload the spec file.

Postman generates a fully functional collection with all API endpoints.

Customize requests, add authentication if needed, and run test calls.

Save requests in collections and automate tests by adding JavaScript in the Tests tab.

For manual requests, for example a GET request to list all listings:
URL: http://localhost:8000/api/listings/
Method: GET
Click Send and verify the JSON response.

### 🎯 Best Practices for API Documentation
>Keep your Swagger/OpenAPI docs up to date with every API change.

>Add meaningful docstrings and operation descriptions in your viewsets (swagger_auto_schema decorator).

>Provide example requests and responses to improve usability.

>Document authentication flows clearly (token/session).

>Group endpoints logically with tags in your API docs.

>Use clear, jargon-free language to assist all users.

## 📦 Usage

Interact with the API endpoints (to be added via Django REST Framework views):

- CRUD operations on Listings  
- Create and manage Bookings  
- Submit and view Reviews  

Test API calls using tools like [Postman](https://www.postman.com/) or `curl`.
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repository and submit pull requests.
---

## 📄 License

This project is licensed under the MIT License.
---

## 📅 Last Updated

Friday, August 1st, 2025
---
*Made with ♥ by ciiru_ngunjiri*