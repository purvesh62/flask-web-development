# Flask forms

--- 

### Project setup

Clone project

`git clone https://github.com/purvesh62/flask-web-development.git`

Create virtual environment

`python -m venv venv`

Activate virtual environment

`source venv\bin\activate` for Linux OS

`venv\Script\activate` for Windows OS

Install requirements

`pip install -r requirements.txt`

Execute the **[flask migration](#flask-migrate)** steps before running the application.

Run application

`python app.py`

---

### Flask Migrate

1. Create the initial migration repository with the following command

   `flask db init`

2. Create the initial migration of the models with the following command

   `flask db migrate -m "First Migration"`

3. Apply the migration to the database with the following command

   `flask db upgrade`