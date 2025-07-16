from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestFunctional(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000')

    def tearDown(self):
        self.driver.quit()

    def test_homepage(self):
        self.driver.get('http://127.0.0.1:5000')
        self.assertIn('EmoTunes', self.driver.title)

    def test_get_recommendation(self):
        self.driver.get('http://127.0.0.1:5000')
        recommend_button = self.driver.find_element(By.ID, 'recommendButton')
        recommend_button.click()
        try:
            # Wait until the emotion result is updated and contains the word "Emotion:"
            WebDriverWait(self.driver, 30).until(
                EC.text_to_be_present_in_element((By.ID, 'emotionResult'), 'Emotion:')
            )
            emotion_result = self.driver.find_element(By.ID, 'emotionResult').text
            weather_result = self.driver.find_element(By.ID, 'weatherResult').text
            self.assertIn('Emotion:', emotion_result)
            self.assertIn('Weather:', weather_result)
        except selenium.common.exceptions.UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            print("Unexpected alert present:", alert.text)
            alert.accept()
            self.fail(f"Test failed due to unexpected alert: {alert.text}")
        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == '__main__':
    unittest.main()
