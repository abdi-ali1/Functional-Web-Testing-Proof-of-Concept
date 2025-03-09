from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FunctionalWebTester:
    def __init__(self, url: str):
        """Initialize with the target URL (no need for driver path)."""
        self.url = url
        self.driver = None

    def setup(self):
        """Set up the Selenium WebDriver using webdriver-manager."""
        """Set up the Selenium WebDriver using webdriver-manager."""
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
        chrome_options.add_argument("--no-sandbox")  
        chrome_options.add_argument("--disable-gpu")  
        chrome_options.add_argument("--disable-dev-shm-usage")  
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        chrome_options.add_experimental_option("useAutomationExtension", False) 
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)


    def perform_search(self, search_query: str) -> bool:
        """Perform a search on the website and return True if search results are found."""
        self.driver.get(self.url)

        try:
  
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Alles accepteren']"))
            )
            cookie_button.click()
        except Exception:
            print("Geen cookie-popup gevonden. Doorgaan met zoeken.")

        try:

            search_box = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.RETURN)

  
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
            )
            results = self.driver.find_elements(By.CSS_SELECTOR, "div.g")
            return len(results) > 0
        except Exception as e:
            print(f"Error tijdens zoeken: {e}")
            return False

    def teardown(self):
        """Tear down the WebDriver session."""
        if self.driver:
            self.driver.quit()

    def run(self, search_query: str) -> bool:
        """Execute the complete test."""
        try:
            self.setup()
            return self.perform_search(search_query)
        finally:
            self.teardown()
