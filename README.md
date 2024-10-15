# page-object-model-selenium
Page Object Model  - Selenium w Python

Task 

- Visit https://useinsider.com/ and check Insider home page is opened or not
- Select “Company” menu in navigation bar, select “Careers” and check Career
page, its Locations, Teams and Life at Insider blocks are opened or not
- Go to https://useinsider.com/careers/quality-assurance/, click “See all QA
jobs”, filter jobs by Location - Istanbul, Turkey and department - Quality
Assurance, check presence of jobs list
- Check that all jobs’ Position contains “Quality Assurance”, Department
contains “Quality Assurance”, Location contains “Istanbul, Turkey”
- Click “View Role” button and check that this action redirects us to Lever
Application form page

All files in /tests folder have their own methods according to page objects and cant be run as independent isolated tests, as they're part of one E2E test.

To save the report after test run and view it in browser - please use command - pytest ./tests/suite_test.py --html=report/report1.html pytest

Report will be saved in projects /reports folder (after each run report will be overwritten)

***Note***

There is page careers_quality_assurance_page
and according test methods for it, as the source of the page is located on a separate path, which we can move to only by straight link(path) in browser

There is another way to get careers page, it leads to open positions path instead of quality assurance, so I decided to prepare a test for open_positions page and use both dropdowns for selected items to filter jobs, as when we go to qa url directly, the department drop-down item has already selected it Quality Assurance

Also, /utils folder contains locators file, as for feature changes we could keep all pages locators separately from page methods

requirements.txt file contains all python interpreter settings

*To run the E2E Test, please run suite_test.py from /tests folder*


