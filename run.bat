@echo off
echo Starting QR Code Generator...
if not exist .venv (
    echo Error: Virtual environment .venv not found.
    echo Please make sure you are in the project root and .venv exists.
    pause
    exit /b
)
.venv\Scripts\python app.py
pause
