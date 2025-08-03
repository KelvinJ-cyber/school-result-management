# EduScore University School Result Management System

A web-based application for managing student results, built with Flask, HTML, and CSS.

## Features

- Student registration and login
- Staff (admin) login and dashboard
- Upload and manage courses
- View registered students and their courses
- Add and manage student results
- Calculate and display student GPA
- Responsive user interface

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy (SQLite database)
- HTML5 & CSS3

## Getting Started

### Prerequisites

- Python 3.x installed
- `pip` for package management

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/school-result-management.git
    cd school-result-management
    ```

2. Install dependencies:
    ```sh
    pip install flask flask_sqlalchemy
    ```

3. Run the application:
    ```sh
    python app.py
    ```

4. Open your browser and go to [http://localhost:5000](http://localhost:5000)

### Project Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates
- `static/` - CSS and static files
- `instance/database.db` - SQLite database

## Usage

- Register as a student or staff
- Staff can upload courses, view students, and manage results
- Students can view their dashboard, courses, and GPA

## License

This project is licensed under the MIT License.