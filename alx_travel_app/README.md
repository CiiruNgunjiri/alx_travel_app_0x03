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

# alx_travel_app_0x03

A Django-based travel booking application with asynchronous task processing configured using Celery with RabbitMQ. This project handles sending booking confirmation emails asynchronously via background tasks.

---

## Setup Instructions

### 1. Prerequisites

- Python 3.13+ installed  
- RabbitMQ server installed and running  
- Virtual environment tool (`venv` or similar)  
- Redis is NOT required for this version (RabbitMQ is used as broker)  

---

### 2. Clone and Prepare the Project

git clone https://github.com/yourusername/alx_travel_app_0x03.git
cd alx_travel_app_0x03/alx_travel_app

python -m venv env

Activate the virtual environment:
Windows:
env\Scripts\activate

Linux/macOS:
source env/bin/activate

pip install -r requirements.txt

text

---

### 3. RabbitMQ Setup

Install and start RabbitMQ server:

- **Ubuntu/Debian:**

sudo apt update
sudo apt install rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server

text

- **Windows / macOS:**  
  See [RabbitMQ Download](https://www.rabbitmq.com/download.html) for instructions.

---

### 4. Project Configuration

Review `alx_travel_app/settings.py`:

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

Email backend configuration example:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourmailserver.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'

---

### 5. Running Django and Celery

Open terminals for each process.

- Start RabbitMQ server if not running:

sudo systemctl start rabbitmq-server

- Start Django development server:

python manage.py runserver

- Start Celery worker:

celery -A alx_travel_app worker -l info

- Optionally start Celery Beat scheduler:

celery -A alx_travel_app beat -l info

---

### 6. Creating a Booking and Verifying Email

- Create bookings via UI or API.
- The booking triggers an async email task.
- Check Celery worker terminal logs for task processing.
- Confirm receipt of booking confirmation emails.

---

### 7. Logs and Debugging

- Celery logs output in worker terminal.
- Email sending failures will appear as errors.
- Check Django logs for backend issues.

---

### 8. Project Structure Highlights

alx_travel_app/
│
├── alx_travel_app/ # Django project settings and celery.py
├── listings/ # App with booking models, views, and tasks
├── manage.py
├── requirements.txt
└── README.md

---

### 9. Dependencies

Django>=4.0
celery[rabbitmq]>=5.0
rabbitmq-server
requests
gql

---

## Contact and Support

Please open an issue or pull request on the GitHub repository for questions or contributions.

---

> _Developed and maintained using Visual Studio Code._

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repository and submit pull requests.
---

## 📄 License

This project is licensed under the MIT License.
---

## 📅 Last Updated

Sunday, August 31st, 2025
---
*Made with ♥ by ciiru_ngunjiri*