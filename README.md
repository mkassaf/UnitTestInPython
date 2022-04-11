# Testing in Python: Unit Tests

This repo conatins an exmaple how to write a unit tests in python. In this repo, I show how to run the unit tests, I also go through a process of achieving 100% test coverage by demonstrating:
- **unittest** 
- **pytest**
- **coverage.py**
- **pytest-cov** 
With all these things I achieve 100% Test Coverage in Python.


# Setup
- Create a dirctory for the app: ie **mkdir project**
- Clone the project: **git clone git@github.com:mkassaf/UnitTestInPython.git**
- Go to the app: **cd UnitTestInPython**
- Creating virtual environments: **python3 -m venv vnev**
- Activate virtual environment: **source vnev/bin/activate**
- install the dependanceies: **pip3 install -r requirements.txt**

# Steps 

## run test using pytest
- **pytest test_calculatorApp.py**
## Code coverage
- To analyses file, Run: **coverage run calculatorApp.py** 
- To generate outputs anaylsys and shows covered lines, Run: **coverage report -m**
- To create a more concise html version of the report, Run: **coverage html**  

## Run the test and generate code coverage
- Run the following command to run the tests and print the code coverage:
   - **pytest --cov=calculatorApp**
- Run the following command to run the tests and generate html report for the code coverage: 
   - **pytest --cov=calculatorApp --cov-report=html**


## Refernces 
- https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
- https://coverage.readthedocs.io/en/6.3.2/
- https://realpython.com/python-testing/
- https://docs.python.org/3/library/venv.html
- https://www.datacamp.com/community/tutorials/unit-testing-python
- https://docs.python.org/3/library/unittest.html
- https://geekflare.com/unit-testing-with-python-unittest/
- https://www.youtube.com/watch?v=7BJ_BKeeJyM&ab_channel=SBCODE
