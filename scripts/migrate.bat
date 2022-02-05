set message=%1
call alembic revision --autogenerate -m %message%
if %ERRORLEVEL% NEQ 0 (
    echo "Alembic revision failed"
    exit /b %ERRORLEVEL%
)
call alembic upgrade head
if %ERRORLEVEL% NEQ 0 (
    echo "Alembic upgrade failed"
    exit /b %ERRORLEVEL%
)