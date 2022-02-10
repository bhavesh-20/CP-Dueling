set commitmessage=%1
call black .
if %ERRORLEVEL% NEQ 0 (
    echo "Black failed"
    exit /b %ERRORLEVEL%
)
call isort .
if %ERRORLEVEL% NEQ 0 (
    echo "Isort failed"
    exit /b %ERRORLEVEL%
)
call pip freeze > requirements.txt
call git add .
call git commit -m %commitmessage%
if %ERRORLEVEL% NEQ 0 (
    echo "Git commit failed"
    exit /b %ERRORLEVEL%
)