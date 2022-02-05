call pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo "Pip install failed"
    exit /b %ERRORLEVEL%
)
call alembic upgrade head
if %ERRORLEVEL% NEQ 0 (
    echo "Alembic upgrade failed"
    exit /b %ERRORLEVEL%
)