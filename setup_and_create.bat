@echo off

REM Set the virtual environment name
set venv_name=mlSolution-env
 
REM Check if the virtual environment exists
if not exist "%venv_name%" (
    echo Creating virtual environment "%venv_name%"...
    py -m venv "%venv_name%"
    if errorlevel 1 (
        echo Error: Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Activate the virtual environment
call "%venv_name%\Scripts\activate"

REM Install base dependencies for the project generator
pip install pyyaml argparse datetime

REM Run the project creation script (adjust paths and config file name if needed)
python create_project.py -c project_config.yaml

REM Deactivate the virtual environment (optional)
call deactivate

echo.
echo Project setup complete!
pause