# HyperSchool

HyperSchool is a Django-based web application designed for managing school schedules and user authentication. This project uses a unique method for user authentication, redirecting users to the login page for authentication rather than authenticating during sign-up.

## Features

- User authentication and registration
- Schedule management
- Admin interface for managing users and schedules

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AstronauticalCodes/hyperSchool.git
   cd hyperSchool
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Admin interface is available at `http://127.0.0.1:8000/admin/`

## Project Structure

- `HyperSchool/asgi.py`: ASGI configuration for the project.
- `HyperSchool/settings.py`: Settings for the Django project.
- `HyperSchool/urls.py`: URL routing for the project.
- `HyperSchool/views.py`: Views for handling requests and rendering responses.
- `HyperSchool/wsgi.py`: WSGI configuration for the project.
- `manage.py`: Django's command-line utility for administrative tasks.

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License.

---
