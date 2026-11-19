@echo off
REM Runs the job bot once and appends output to logs\jobbot.log
cd /d "%~dp0"

if not exist logs mkdir logs

set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

echo. >> "logs\jobbot.log"
python main.py >> "logs\jobbot.log" 2>&1
