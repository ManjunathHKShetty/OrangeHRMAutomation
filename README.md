Tech Stack
Python, PyTest
Selenium
html Report
Parallel Run with xdist

Install the dependencies
pip install selenium
pip install pytest
pip install pytest html

To run the Framework
pytest -s -v tests/test_case.py

To generate html Report
pytest -s -v --html=Reports/reports.html tests/test_case.py