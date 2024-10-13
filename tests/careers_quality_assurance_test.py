import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.careers_quality_assurance_page import QualityAssurancePage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_careers_quality_assurance(driver):
    quality_assurance_page = QualityAssurancePage(driver)
    quality_assurance_page.open_page("https://useinsider.com/careers/quality-assurance/")
    time.sleep(1)
    quality_assurance_page.click_button_all_qa_jobs()
    time.sleep(1)
    quality_assurance_page.check_department_is_qa()
    time.sleep(1)
    quality_assurance_page.open_location_dropdown()
    time.sleep(2)
    quality_assurance_page.select_location_turkey()
    time.sleep(1)
    quality_assurance_page.check_jobs_list()
    time.sleep(1)
    quality_assurance_page.check_position_title()
    time.sleep(1)
    quality_assurance_page.check_position_department()
    time.sleep(1)
    quality_assurance_page.check_position_location()
