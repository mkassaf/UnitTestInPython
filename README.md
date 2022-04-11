# Testing in Python: Unit Tests

This repo conatins an exmaple how to write a unit tests in python. In this repo, I show how to run the unit tests, I also go through a process of achieving 100% test coverage by demonstrating:
- **unittest** 
- **pytest**
- **coverage.py**
- **pytest-cov**
<br/>
With all these things I achieve 100% Test Coverage in Python.


# Setup
- Create a dirctory for the app: ie  ```bash mkdir project ```
- Clone the project:  ```bash git clone git@github.com:mkassaf/UnitTestInPython.git ```
- Go to the app:  ```bash cd UnitTestInPython ```
- Creating virtual environments:  ```bash python3 -m venv vnev ```
- Activate virtual environment:  ```bash source vnev/bin/activate ```
- install the dependanceies:  ```bash pip3 install -r requirements.txt ```

# Steps 

## Run test using pytest

```bash
pytest test_calculatorApp.py 
```

## Result summary report in python nosetests

- You can run tests for your project using this **nosetests** : ```bash nosetests ```
- For help with nosetests’ many command-line options, try : ```bash nosetests -h ```
- For example, ```bash nosetests --with-xunit  ``` generates a xml file conatin the test cases run report.
## Code coverage
- To analyses file, Run: ```bash coverage run calculatorApp.py ```
- To generate outputs anaylsys and shows covered lines, Run:  ```bash coverage report -m ```
- To create a more concise html version of the report, Run:  ```bash coverage html ```

## Run the test and generate code coverage
- Run the following command to run the tests and print the code coverage:
    - ```bash pytest --cov=calculatorApp ```
- Run the following command to run the tests and generate html report for the code coverage: 
    - ```bash pytest --cov=calculatorApp --cov-report=html ```


# Refernces 
- https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
- https://coverage.readthedocs.io/en/6.3.2/
- https://realpython.com/python-testing/
- https://docs.python.org/3/library/venv.html
- https://www.datacamp.com/community/tutorials/unit-testing-python
- https://docs.python.org/3/library/unittest.html
- https://geekflare.com/unit-testing-with-python-unittest/
- https://www.youtube.com/watch?v=7BJ_BKeeJyM&ab_channel=SBCODE
- https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
- https://realpython.com/python-mock-library/#patch