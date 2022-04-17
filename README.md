# Testing in Python: Unit Tests


This repo conatins an exmaple how to write a unit tests in python. In this repo, I show how to run the unit tests, I also go through a process of achieving 100% test coverage by demonstrating:
- **unittest** 
- **pytest**
- **coverage.py**
- **pytest-cov**
<br/>
With all these things I achieve 100% Test Coverage in Python.

# Unit test in python slides in the below link 

- https://bit.ly/3uOmny9

# Setup
- Create a dirctory for the app: ie  
```console
mkdir project 
```
- Clone the project: 
```console
git clone git@github.com:mkassaf/UnitTestInPython.git 
```
- Go to the app:  
```console 
cd UnitTestInPython 
```
- Creating virtual environments:  
```console
python3 -m venv vnev
```
- Activate virtual environment: 
```console
source vnev/bin/activate 
```
- install the dependanceies:  
```console
pip3 install -r requirements.txt 
```

# Steps 

## Run test using pytest

```console
pytest test_calculatorApp.py 
```

## Result summary report in python nosetests

- You can run tests for your project using this **nosetests** : 
```console
    nosetests 
```
- For help with nosetests’ many command-line options, try : 
```console
    nosetests -h 
```
- For example, 
```console 
nosetests --with-xunit 
``` 
generates a xml file conatin the test cases run report.
## Code coverage
- To analyses file, Run: 
```console  
    coverage run calculatorApp.py 
```
- To generate outputs anaylsys and shows covered lines, Run:  
```console  
    coverage report -m 
```
- To create a more concise html version of the report, Run:  
 ```console 
    coverage html 
 ```

## Run the test and generate code coverage
- Run the following command to run the tests and print the code coverage:
    - 
    ```console 
    pytest --cov=calculatorApp 
    ```
- Run the following command to run the tests and generate html report for the code coverage: 
    - 
    ```console 
    pytest --cov=calculatorApp --cov-report=html 
    ```


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
