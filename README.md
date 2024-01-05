# Project Description

This project utilizes Playwright and pytest to create automated tests for various features of a web application. The tests are organized using pytest markers to allow selective execution based on specific features such as login, products, contact_us, subscribe, or individual test cases.

# Requirements

Before running the tests, ensure the following dependencies are installed:

- Python (3.12 or higher)
- Pip (23.2.1 or higher)

# Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/drevinskiyvlad/Task_9_Playwright_Pytest.git
   cd repository
   ```

2. Install environment:

   ```bash
   python -m pip install --upgrade pip
   pip install pipenv
   pipenv install --system
   playwright install chromium
   ```

# Steps to Run Tests

To run the entire test suite, use the following command:

```bash
pytest
```

To run one particular test, use the following command, replacing `<test_name>` with the name of the test (e.g., test_login):

```bash
pytest -k <test_name>
```

To run tests for a specific feature, use the following command, replacing `<feature>` with the desired feature (e.g., login, products, contact_us, subscribe, testCases):

```bash
pytest -m <feature>
```

# Steps to Generate Report

The test report is generated automatically after running the tests. However, if you want to generate the report manually, use the following command:

```bash
pytest --alluredir=./reports --clean-alluredir
```

To view the generated report, use the following command:

```bash
allure serve reports
```

This will launch a local server and open the report in your default web browser. The report provides detailed information about test execution, including test results, duration, and any failures or errors encountered during the testing process.