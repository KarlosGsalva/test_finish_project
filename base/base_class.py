import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url", get_url)

    """method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = "screenshot_" + now_date + "_.png"
        self.driver.save_screenshot("C:\\chromedriver\\QA_project\\test_finish_project\\screen\\" + screenshot_name)

    """method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("url is correct")
