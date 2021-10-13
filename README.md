# api_tests

API tests

[![tests](https://github.com/grsln/api_tests/actions/workflows/tests.yml/badge.svg)](https://github.com/grsln/api_tests/actions/workflows/tests.yml)

The project uses:

1. Python
2. Requests
3. Allure for reports
4. CI (GitHub actions)

Testing application (write with Flask):

url: https://stores-tests-api.herokuapp.com

swagger: https://app.swaggerhub.com/apis/berpress/flask-rest-api/1.0.0

### How to start

Create and navigate to folder

```
mkdir api_tests && cd api_tests
```

Clone project from GitHub

```
git clone https://github.com/grsln/api_tests.git
```

Use python 3.8 + Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

and add pre-commit

```
pre-commit install
```

### Run all tests

```
pytest
```
