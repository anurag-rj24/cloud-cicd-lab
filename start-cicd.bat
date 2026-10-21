@echo off
echo ===================================================
echo   Anurag's Local CI/CD Pipeline Controller
echo ===================================================
echo.
echo Starting GitHub Actions Runner in the background...
cd /d C:\Users\Anurag\actions-runner
start "GitHub Actions Runner" cmd /k "run.cmd"

echo.
echo Checking Minikube status...
cd /d C:\Users\Anurag\Desktop\CICD
set PATH=C:\Users\Anurag\bin;C:\Users\Anurag\AppData\Local\Programs\DockerDesktop\resources\bin;%PATH%
minikube status

echo.
echo Getting live application URL...
minikube service flask-service
pause
