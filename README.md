# CP-Dueling
Dueling Platform for Competitive Programming. Learn through Games.

# Setting Up
- Minimum Python version needed = 3.9.9
- Install Virtualenv and use `virtualenv venv` on the root directory.
- Access the created virtual environment using `venv/scripts/activate` for powershell and `Source venv/bin/activate` for linux/bash.
- `pip install -r requirements.txt`
- Run the server using `uvicorn main:app --reload`. The server should be running on PORT 8000.

# Access Swagger API
- Navigate to `localhost:8000/docs`, i.e, /docs route to view the SWAGGERAPI.
