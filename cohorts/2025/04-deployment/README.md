# Setting Up Python Virtual Environment with Pipenv

## Prerequisites
- Python installed on your system
- pip (Python package installer)

## Installation Steps

### 1. Install Pipenv
```bash
pip install --user pipenv
```

### 2. Create Virtual Environment
Navigate to your project directory and run:
```bash
pipenv install
```
This creates a Pipfile and sets up the virtual environment.

### 3. Activate Virtual Environment

**Linux/macOS:**
```bash
source $(pipenv --venv)/bin/activate
```

**Windows:**
```bash
pipenv shell
```

### 4. Save Depedencies

```bash
pipenv lock
```

### 5. Run Python Scripts
Once the environment is activated:
```bash
python my_script.py
```
Note: Replace `my_script.py` with your actual script name.

### 6. Deactivate Environment
To exit the virtual environment:
```bash
deactivate
```

### 7. Docker Commands

```bash
docker build -t deployment_image .
```

```bash
docker run -it deployment_image
```