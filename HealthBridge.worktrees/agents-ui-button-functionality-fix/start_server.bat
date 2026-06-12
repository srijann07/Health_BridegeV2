@echo off
REM Start HealthBridge Django Server

echo ============================================
echo     Starting HealthBridge Application
echo ============================================
echo.

cd /d "C:\Users\srija\HealthBridge.worktrees\agents-ui-button-functionality-fix"

echo Running Django server on port 8000...
echo.
echo Opening in browser in 3 seconds...
echo.

python manage.py runserver 8000

pause
