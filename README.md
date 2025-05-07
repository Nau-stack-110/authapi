# Authapi

APIAuth is a secure authentication API built with Django REST Framework, utilizing JSON Web Tokens (JWT) for authentication, CORS headers for cross-origin requests, and SQLite3 as the database. This project provides a robust foundation for user authentication and authorization in web applications, allowing users to log in using their email or phone number and password.

## Features
- User registration and login with JWT-based authentication
- Secure token-based access control
- Cross-Origin Resource Sharing (CORS) support for frontend integration
- Lightweight SQLite3 database for easy setup and development
- RESTful API endpoints for user management

## Technologies Used
- **Django REST Framework**: For building the API
- **JWT (JSON Web Tokens)**: For secure authentication
- **django-cors-headers**: To handle CORS requests
- **SQLite3**: Default database for simplicity and portability
- **Python**: Core programming language

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nau-stack-110/authapi.git
   cd authapi
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000`.

## Configuration

- **JWT Settings**: Configure JWT settings in `settings.py` (e.g., token expiration, secret key).
- **CORS**: Adjust allowed origins in `settings.py` under `CORS_ALLOWED_ORIGINS` for your frontend.
- **Database**: SQLite3 is used by default. For production, consider switching to PostgreSQL or another database.

## API Endpoints

| Endpoint               | Method | Description                     |
|------------------------|--------|---------------------------------|
| `/api/register/`       | POST   | Register a new user             |
| `/api/login/`          | POST   | Login and receive JWT tokens    |
| `/api/token/refresh/`  | POST   | Refresh JWT access token        |
| `/api/me/`             | GET    | List user (authenticated)  |   


Example request for login:
```bash
curl -X POST http://localhost:8000/token/ -d "username=youremailortel&password=yourpassword"
```

## Requirements
See `requirements.txt` for a full list of dependencies. Key packages include:
- `django`
- `djangorestframework`
- `djangorestframework-simplejwt`
- `django-cors-headers`

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
