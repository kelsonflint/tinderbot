from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self):
        self.driver.get('https://tinder.com')
        sleep(3)

    def googleLogin(self):
        login_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        login_btn.click()
        sleep(1)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = bot.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys('example@mail.com')
        next_btn = bot.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn.click()
        sleep(2)

        pass_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_in.send_keys('password')
        next2_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next2_btn.click()
        self.driver.switch_to.window(base_window)
        sleep(8)

    def phone(self):
        phone_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        phone_in.send_keys('1234567890')
        sleep(1)
        next3_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        next3_btn.click()


    def swipe(self):
        allow_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_btn.click()
        sleep(1)
        nope_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        nope_btn.click()
        accept_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/button')
        accept_btn.click()
        sleep(4)
        self.autoswipe()

    def autoswipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.start()
#bot.swipe()
