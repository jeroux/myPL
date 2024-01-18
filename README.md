# myPL
Use case on project Geronte for myPL

## Installation
Go in the project folder and create a virtual environment
```bash
python -m venv venv
```

install TailwindCSS and Flowbite
```bash
npm install tailwindcss
npm install flowbite
```

Go to myPL/myPL folder
```bash
cd PATH_TO_YOUR_FOLDER/myPL/myPL
```

Create a postgresql database for the project

Create .env file in the folder myPL/myPL, where the settings.py file is, and add the following variables:

```text
SECRET_KEY=your_secret_key
DB_NAME=dbname
DB_USER=dbuser
DB_PASSWORD=dbpassword
```

Install dependencies
```bash
pip install -r requirements.txt
```

## Run
```bash
python manage.py migrate
python manage.py runserver
```

No need to create a new user, the database is already populated with a user with the following informations:
```text
username: John Doe
age: 45
```

You can go to the dashboard with the following url:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


