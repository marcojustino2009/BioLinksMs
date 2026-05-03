Write-Host "Starting BioLink MS Backend..." -ForegroundColor Green

$backendPath = "C:\Users\i5\Desktop\biolink_ms\backend"

if (!(Test-Path $backendPath)) {
    Write-Error "Backend not found"
    exit 1
}

Set-Location $backendPath

$python = "C:\Program Files\Python312\python.exe"

if (!(Test-Path $python)) {
    Write-Error "Python not found"
    exit 1
}

if (!(Test-Path "requirements.txt")) {
    Write-Error "requirements.txt missing"
    exit 1
}

# Create venv
if (!(Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    & $python -m venv venv
}

# Activate venv
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
pip install "uvicorn[standard]"

# Run server
Write-Host "Server running at http://127.0.0.1:8000" -ForegroundColor Cyan
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000