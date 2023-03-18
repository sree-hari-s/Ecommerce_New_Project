
# GreatKart E-commerce Website

An ecommerce website build using Python Django in the backend, sqlite for database management and HTML as view engine to render pages dynamically.
## Features


- Multi-product with Variations
- Registration, Login with Token Based Verification & Message Alerts

- Online Payment Integration (Paypal)

- Order Tracking

- Admin dashboard

- Charts and Graphs

- Paginator & Search

- My Account Functionalities

- Product Gallery with Unlimited Images

- Django Security Measures
## Installation

- Install and Create Virtual Environment
- Activate the virtual environment and verify it
- Clone the GitHub Repository 
- Install the requirements
```bash
  pip install -r requirements.txt
```
- Create a .env file inside the directory where manage.py file is (comparing the *.env-sample*)
```bash
  $ nano .env
```
- Migrate Project to the Database
```bash
python manage.py makemigrations app
python manage.py migrate
```
- Run the Project
```bash
python manage.py runserver
```
