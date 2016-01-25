# -*- coding: utf-8 -*-
from selenium.webdriver import Firefox
import time, re, json, unicodedata, pytest
from selenium.webdriver.support.ui import Select
@pytest.fixture()
def webdriver(request):
    driver = Firefox()
    driver.get("http://www.12bet.com/")
    driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return driver
def test_CountryCode(webdriver):
    webdriver.find_element_by_css_selector("a > img").click()
    webdriver.switch_to_frame('topFrame')
    webdriver.find_element_by_xpath("//img[contains(@src,'http://pic.12bet.com/template/deposit/en/images/join-now-btn.gif')]").click()
    webdriver.switch_to_window(webdriver.window_handles[1])

    with open('document.json', 'r') as f:
        data = f.read()
        json_data = json.loads(data)
    for i in range(2,136):
        Select(webdriver.find_element_by_id("selCountry")).select_by_index(i)
        print webdriver.find_element_by_id("selCountry").get_attribute("value")
        webdriver.find_element_by_id("countryCode").click()
        for MobileCountryItems in json_data['MobileCountryItems']:
            if MobileCountryItems['CountryID'].encode('raw_unicode_escape') == webdriver.find_element_by_id("selCountry").get_attribute("value"):
                assert  MobileCountryItems['MobileCountryCode'].encode('raw_unicode_escape') == webdriver.find_element_by_id("countryCode").get_attribute("value")
                print webdriver.find_element_by_id("selCountry").get_attribute("value"),webdriver.find_element_by_id("countryCode").get_attribute("value")

if __name__ == "__main__":
    pytest.main()