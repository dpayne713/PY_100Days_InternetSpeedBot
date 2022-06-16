from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class SpeedTest:
    def __init__(self):
        self.chrome_driver_location = "/Users/davidpayne/Documents/Python/chromedriver"
        self.service = Service(self.chrome_driver_location)
        self.options= webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service)
        self.site = None



    def run_test(self):
        self.driver.get("https://www.speedtest.net")
        self.go_button = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test")
        self.go_button.click()

        self.driver.implicitly_wait(60)
        self.result_button = self.driver\
            .find_element(by=By.CLASS_NAME, value="result-area-nav-right")\
            .find_element(by=By.CSS_SELECTOR, value="a")

        self.result_button.click()
        self.results = self.driver\
            .find_element(by=By.XPATH, value= "//table[@id='results-history-table']")\
            .find_element(by=By.TAG_NAME, value="tbody")
        self.speed_data = {
            "date_time": self.results.find_element(by=By.CLASS_NAME, value="test-date").text.split('\n'),
            "ping": self.results.find_element(by=By.CLASS_NAME, value="ping-speed").text,
            "download_speed": self.results.find_element(by=By.CLASS_NAME, value="download-speed").text,
            "upload_speed": self.results.find_element(by=By.CLASS_NAME, value="upload-speed").text,
            "isp_info": self.results.find_element(by=By.CLASS_NAME, value="isp-info").text.split('\n')
        }

        self.export_results = self.driver.find_element(by=By.ID, value="export-results-button").click()


        return self.speed_data



