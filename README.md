# Death by AI - Django Web Interface

A Django web application that provides a web interface for AI interactions using Ollama.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/xMokiii/DisAIster.git
cd DisAIster
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
.venv\Scripts\Activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
```bash
python manage.py migrate
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Project Structure
```
deathbyai/
├── manage.py
├── deathbyai_web/          # Main project settings
├── game/                   # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
└── .gitignore            # Git ignore rules
```

## Development Commands

### Run Tests
```bash
python manage.py test game
```

### Check for Issues
```bash
python manage.py check
```

### Create New Migrations
```bash
python manage.py makemigrations
```

## Requirements
- Python 3.8+
- Django 5.2+
- Ollama (for AI functionality)

## Contributing
1. Create a virtual environment
2. Install dependencies from requirements.txt
3. Run migrations
4. Make your changes
5. Run tests before committing