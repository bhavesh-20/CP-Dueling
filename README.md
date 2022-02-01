# CP-Dueling
Dueling Platform for Competitive Programming. Learn through Games.

# Setting Up
- Minimum Python version needed = 3.9.9
- Install Virtualenv and use `virtualenv venv` on the root directory.
- Access the created virtual environment using `venv/scripts/activate` for powershell and `Source venv/bin/activate` for linux/bash.
- `pip install -r requirements.txt`
- Download postgresql and create credentials.
- Download .env file from wiki page of this repo and replace your credentials wherever required. Place the .env file on the root directory.
- Run the server using `uvicorn main:app --reload`. The server should be running on PORT 8000.

# Running Migrations
- Create migrations using command `alembic revision --autogenerate -m "message"`
- Run `alembic upgrade head` to apply migrations.

# Access Swagger API
- Navigate to `localhost:8000/docs`, i.e, /docs route to view the SWAGGERAPI.
