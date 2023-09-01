# GreatKart E-commerce Website

GreatKart is a full-fledged e-commerce website built using Python Django for the backend, SQLite for database management, and HTML as the view engine to render pages dynamically.

## Features

- Multi-product with Variations
- Registration, Login with Token-Based Verification & Message Alerts
- Online Payment Integration (Paypal)
- Order Tracking
- Admin dashboard
- Charts and Graphs
- Paginator & Search
- My Account Functionalities
- Product Gallery with Unlimited Images
- Django Security Measures

## Installation

Follow these steps to set up and run the GreatKart E-commerce Website on your local machine:

1. Install and create a virtual environment:

   ```bash
   python -m venv myenv
   ```

2. Activate the virtual environment:

   - On Windows:

     ```bash
     source myenv/bin/activate
     ```

   - On macOS and Linux:

     ```bash
     source myenv/bin/activate
     ```

3. Clone the GitHub Repository:

   ```bash
   git clone https://github.com/sree-hari-s/Ecommerce_New_Project.git
   cd greatkart
   ```

4. Install the project requirements:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project directory (similar to `.env-sample`) and fill in the required environment variables.
    ```python
    SECRET_KEY= django_secret_key
    DEBUG=True/False
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=example@gmail.com
    EMAIL_HOST_PASSWORD=password
    EMAIL_USE_TLS=True
    ```
6. Migrate the project to the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the project:

   ```bash
   python manage.py runserver
   ```

