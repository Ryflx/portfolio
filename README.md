# Personal Portfolio Website

A modern, responsive portfolio website built with Django. This website showcases projects, skills, and blog posts in a clean and professional manner.

## Features

- Responsive design
- Project showcase
- Skills section
- Blog functionality
- Contact form
- Dark/Light mode
- Admin dashboard for content management

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd portfolio
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the website.

## Tech Stack

- Django 4.2+
- Bootstrap 5
- SQLite (development)
- HTML5/CSS3
- JavaScript

## Project Structure

- `portfolio/` - Main project directory
- `core/` - Main application
- `blog/` - Blog application
- `projects/` - Projects application
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `media/` - User uploaded content 