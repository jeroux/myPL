# myPL
Use case on project Geronte

## Installation
Go in the project folder and create a virtual environment
```bash
python -m venv venv
```

Create .env file and add the following variables:

```text
SECRET_KEY=your_secret_key
```

Install dependencies
```bash
pip install -r requirements.txt
```

## Run
```bash
python mange.py migrate
python manage.py runserver
```

No need to create a new user, the database is already populated with a user with the following informations:
```text
username: John Doe
age: 45
```

You can go to the dashboard with the following url:
```text
http://127.0.0.1:8000/
```

