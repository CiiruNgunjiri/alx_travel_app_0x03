# alx_travel_app_0x03

A Django-based travel booking applica
asynchronous task processing configur
Celery with RabbitMQ. This project ha
sending booking confirmation emails 
asynchronously via background tasks.

---

## Setup Instructions

### 1. Prerequisites

- Python 3.13+ installed  
- RabbitMQ server installed and runni
- Virtual environment tool (`venv` or
- Redis is NOT required for this vers
(RabbitMQ is used as broker)  

---

### 2. Clone and Prepare the Project

git clone https://github.com/youruser
alx_travel_app_0x03.git
cd alx_travel_app_0x03/alx_travel_app

python -m venv env

Activate the virtual environment:
Windows:
env\Scripts\activate

Linux/macOS:
source env/bin/activate

pip install -r requirements.txt

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
  See [RabbitMQ Download](https://www
com/download.html) for instructions

---

### 4. Project Configuration

Review `alx_travel_app/settings.py`:

CELERY_BROKER_URL = 'amqp://
guest:guest@localhost//'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

Email backend configuration example:
EMAIL_BACKEND = 'django.core.mail.bac
EmailBackend'
EMAIL_HOST = 'smtp.yourmailserver.com
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example
EMAIL_HOST_PASSWORD = 'your-password'
DEFAULT_FROM_EMAIL = 'your-email@exam

---

### 5. Running Django and Celery

Open terminals for each process.

- Start RabbitMQ server if not runnin

sudo systemctl start rabbitmq-server

- Start Django development server:

python manage.py runserver

- Start Celery worker:

celery -A alx_travel_app worker -l in

- Optionally start Celery Beat schedu

celery -A alx_travel_app beat -l info

---

### 6. Creating a Booking and Verifyi

- Create bookings via UI or API.
- The booking triggers an async email
- Check Celery worker terminal logs f
processing.
- Confirm receipt of booking confirma
emails.

---

### 7. Logs and Debugging

- Celery logs output in worker termin
- Email sending failures will appear 
- Check Django logs for backend issue

---

### 8. Project Structure Highlights

alx_travel_app/
│
├── alx_travel_app/ # Django project 
and celery.py
├── listings/ # App with booking mode
and tasks
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

Please open an issue or pull request 
GitHub repository for questions or 
contributions.

---

> _Developed and maintained using Vis
Code._

## 🤝 Contributing

Contributions, issues, and feature re
welcome!  
Feel free to fork the repository and 
pull requests.
---

## 📄 License

This project is licensed under the MI
---

## 📅 Last Updated

Sunday, August 31st, 2025
---
*Made with ♥ by ciiru_ngunjiri*