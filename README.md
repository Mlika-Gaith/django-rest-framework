# Django Rest API Tutorial

This repository contains a simple Django project that serves as a starting point for building a RESTful API using Django. Follow the steps below to run the project and explore the basics of creating a Django REST API.

## Getting Started

1. **Clone this repository to your local machine:**

    ```bash
    git clone https://github.com/Mlika-Gaith/django-rest-framework.git
    ```

2. **Change into the project directory:**

    ```bash
    cd django-rest-api-tutorial
    ```

3. **Install the required dependencies using pip:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser to access the Django admin panel:**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up your superuser account.

6. **Run the development server:**

    ```bash
    python manage.py runserver 8080
    ```

    The Django Rest API will be accessible at `http://localhost:8080/`.

## Exploring the API

- **Django Admin Panel:** Visit `http://localhost:8000/admin/` and log in with the superuser credentials to explore the Django admin panel.

- **API Endpoints:** The API endpoints are available at `http://localhost:8000/api/products`.

- **Running files inside py_client:**

1. **Change into the project directory:**

    ```bash
    cd py_client
    ```
2. **Try running a .py file:**
    For example:
    ```bash
   python list.py
    ```

