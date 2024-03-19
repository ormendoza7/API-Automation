# Automated API Testing Project

This project provides a suite of automated tests for API endpoints, utilizing Python with the `requests` library for making HTTP requests and `pytest` for running the tests. 

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.6 or newer
- Git (for cloning the repository)

## Setup Instructions

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Clone the project repository from GitHub to your local machine:

```bash
git clone https://github.com/ormendoza7/API-Automation.git
cd API-Automation/asana_api
```

### 2. Create a Virtual Environment

Create a virtual environment in the project directory. This environment will contain all the necessary Python packages for your project and keep them isolated from other projects.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment. Activation commands vary depending on your operating system:

- On Windows:

  ```bash
  .\venv\Scripts\activate
  ```

- On Git console, macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

You should now see `(venv)` at the beginning of your command line prompt, indicating that the virtual environment is active.

### 4. Install Dependencies

With the virtual environment activated, install the project dependencies using:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file in your project directory and installs all the listed packages.

### 5. Running Tests

To run the automated tests, ensure you're still in the project root directory and your virtual environment is activated. 

Use the following command to start the tests:

```bash
pytest
```

`pytest` will automatically find all files named `test_*.py` or `*_test.py` and run any functions prefixed with `test_` within them.

## Deactivating the Virtual Environment

When you're done working in the virtual environment, you can deactivate it by simply running:

```bash
deactivate
```

This command will return your terminal to the normal system environment.
