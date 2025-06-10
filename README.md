# Django Authentication

An Authentication application built with Django, featuring user authentication.that works seamlessly across all devices.

## Features

- **User Authentication**: Secure registration, login, and logout functionality

- **Clean Interface**: Intuitive and user-friendly design


## Technologies Used

- **Backend**: Django 4.2+
- **Database**: SQLite (default) 
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django's built-in authentication system
- **Version Control**: Git

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Django

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/exoncodex/Auth_project.git
   cd Auth
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create a .env file in the root directory
   cp .env.example .env
   
   # Edit .env with your configuration
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your web browser and navigate to `http://127.0.0.1:8000/`



## Usage

1. **Register a new account** or **login** with existing credentials
2  Then you can **logout**


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/exoncodex/Auth_project/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the problem

## Acknowledgments

- Django documentation and community
- Bootstrap for responsive design components


**Happy Authentication! 📝✅**