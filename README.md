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

1. Clone the GitHub Repository:

   ```bash
   git clone https://github.com/sree-hari-s/Ecommerce_New_Project.git
   ```

2. Install and create a virtual environment:

   ```cmd
   virtualenv env
   ```

3. Activate the virtual environment:
   - On Windows:

     ```cmd
     env\Scripts\activate
     ```

4. Install the project requirements:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` File and Fill in Required Environment Variables
   In your project directory, create a `.env` file (similar to `.env-sample`) and fill in the required environment variables as follows:

   ```python
   SECRET_KEY=django_secret_key
   DEBUG=True/False
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=example@gmail.com
   EMAIL_HOST_PASSWORD=password
   EMAIL_USE_TLS=True
   ```

      5.1 Generate Secret Key in Django Using `get_random_secret_key()` Function

      Django provides a convenient function called `get_random_secret_key()` to generate a secret key. This function returns a string of 50 random characters, making it the official way to generate a secret key in Django. Here are the steps to generate a Django secret key:
      1. **Access the Python Interactive Shell:**
         To access the Python Interactive shell, run the following command in the terminal of your Django project:

         ```bash
         (env) $ python manage.py shell
         ```

         You'll know you're in the shell when each new line is prefixed with `>>>`.
      2. **Import `get_random_secret_key()` from `django.core.management.utils`:**
         Before generating the secret key, import the `get_random_secret_key()` function from `django.core.management.utils`. Run the following command and press Enter:

         ```python
         >>> from django.core.management.utils import get_random_secret_key
         ```

      3. **Generate the Secret Key in the Terminal:**
         Now, you can use the `get_random_secret_key()` function to generate the secret key. Execute the following command:

         ```python
         >>> print(get_random_secret_key())
         ```

         A random secret key will be generated and displayed on the next line. Your generated key will be different from the example shown above, as it is entirely random.

6. Migrate the project to the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the project:

   ```bash
   python manage.py runserver
   ```
