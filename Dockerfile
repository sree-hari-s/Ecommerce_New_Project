FROM python:3.10

WORKDIR /Ecommerce

COPY requirements.txt /Ecommerce/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /Ecommerce/
ENV DJANGO_SETTINGS_MODULE=Ecommerce.settings

EXPOSE 8000

# Run database migrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]