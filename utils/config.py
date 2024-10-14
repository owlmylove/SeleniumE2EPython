# browsers(driver): chrome, firefox,
# fixtures set-up tear-down
# mark for screenshots


from selenium import webdriver
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