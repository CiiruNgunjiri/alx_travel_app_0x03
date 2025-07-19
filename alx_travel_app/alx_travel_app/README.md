# alx_travel_app_0x00

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

Saturday, July 19, 2025
---
*Made with ♥ by ciiru_ngunjiri*