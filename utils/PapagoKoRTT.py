from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PapagoKoRTT:
    def __init__(self, sentence):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get('https://papago.naver.com')

        self.input_box = self.driver.find_element(By.XPATH, '//*[@id="txtSource"]')
        self.output_box = self.driver.find_element(By.XPATH, '//*[@id="txtTarget"]')
        self.button = self.driver.find_element(By.CSS_SELECTOR,'button#btnTranslate')
        self.x_button = self.driver.find_element(By.CLASS_NAME,'btn_text_clse___1Bp8a')
        self.button_change_src_tgt = self.driver.find_element(By.CLASS_NAME,'btn_switch___x4Tcl')

        self.sentence = sentence

    def translation(self, input):
        try:
            self.input_box.clear()
            self.input_box.send_keys(input)
            self.button.click()
            
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="targetEditArea"]/p')))
        except Exception as e:
            print('='*30)
            print('ERROR translation ', '\n', 'ERROR IS :::::::', e)

    def backTranslation(self):
        try:
            self.button_change_src_tgt.click()
            
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="sourceEditArea"]/p')))

            output = self.driver.find_element(By.CSS_SELECTOR,'div#txtTarget').text
            self.x_button.click()

            return output
        except Exception as e:
            print('='*30)
            print('ERROR backTranslation', '\n', 'ERROR IS :::::::', e)

    def roundTripTranslation(self):
        try:
            self.translation(self.sentence)
            output = self.backTranslation()

            return output
        except Exception as e:
            print('='*30)
            print('ERROR backTranslation', '\n', 'ERROR IS :::::::', e)

            return self.sentence
