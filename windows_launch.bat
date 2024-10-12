@echo off

IF ! "test" "-d" "venv" (
  echo "Creating virtual environment"
  python3 "-m" "venv" "venv"
  echo "Done"
)
source "venv\bin\activate"
python3 "%CD%\splitter.py"