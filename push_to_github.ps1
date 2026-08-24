# PowerShell script to push project to GitHub (Narasimha755)
Set-Location "C:\Users\lucky\.gemini\antigravity\scratch\cdm_recruitment_dashboard"

Write-Host "Initializing Git repository..." -ForegroundColor Cyan
git init

Write-Host "Setting Git commit identity..." -ForegroundColor Cyan
git config user.name "Lakshmi Narasimha Chowdary Machineni"
git config user.email "luckymachineni755@gmail.com"

Write-Host "Staging all dashboard files..." -ForegroundColor Cyan
git add .

Write-Host "Creating initial commit..." -ForegroundColor Cyan
git commit -m "Initial release of CDM Talent Intelligence Dashboard"

Write-Host "Setting default branch to main..." -ForegroundColor Cyan
git branch -M main

Write-Host "Adding GitHub remote repository..." -ForegroundColor Cyan
git remote remove origin 2>$null
git remote add origin https://github.com/Narasimha755/cdm-talent-intelligence-dashboard.git

Write-Host "Pushing code to GitHub..." -ForegroundColor Cyan
git push -u origin main

Write-Host "Successfully pushed to https://github.com/Narasimha755/cdm-talent-intelligence-dashboard" -ForegroundColor Green
