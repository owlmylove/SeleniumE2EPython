# browsers(driver): chrome, firefox,
# fixtures set-up tear-down
# mark for screenshots


from selenium import webdriver
import sys
from pytest import fixture, mark

@mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail_state = hasattr(report, 'wasxfail')
        if (report.skipped and xfail_state) or (report.failed and not xfail_state):
            mydriver = item.funcargs['driver']
            screenshot = mydriver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
    report.extra = extra


import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        item.instance.driver.save_screenshot('screenshot_on_failure.png')