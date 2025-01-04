from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_NEW_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_CREATE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_RES_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=5)
        text = error_field.text
        logging.info(f"We find text '{text}' in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user_text(self):
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=5)
        text = user_field.text
        logging.info(f"We find text '{text}' in field {TestSearchLocators.LOCATOR_HELLO[1]}")
        return text

    def click_new_post_btn(self):
        logging.info("Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send {word} to title field {TestSearchLocators.LOCATOR_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Send {word} to description field {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send {word} to content field {TestSearchLocators.LOCATOR_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def click_save_btn(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BTN).click()

    def get_res_text(self):
        res_title = self.find_element(TestSearchLocators.LOCATOR_RES_TITLE, time=15)
        text = res_title.text
        logging.info(f"We find text '{text}' in title {TestSearchLocators.LOCATOR_RES_TITLE[1]}")
        return text

    def click_contact_link(self):
        logging.info("Click Contact link")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

    def get_contact_title_text(self):
        title = self.find_element(TestSearchLocators.LOCATOR_CONTACT_TITLE, time=7)
        text = title.text
        logging.info(f"We find text '{text}' in title {TestSearchLocators.LOCATOR_CONTACT_TITLE[1]}")
        return text

    def enter_contact_name_field(self, word):
        logging.info(f"Send {word} to contact title field {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}")
        contact_name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        contact_name_field.clear()
        contact_name_field.send_keys(word)

    def get_contact_name_text(self):
        contact_name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        text = contact_name_field.get_attribute("value")
        logging.info(f"We find text '{text}' in contact name field {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}")
        return text

    def enter_contact_email_field(self, word):
        logging.info(f"Send {word} to contact email field {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}")
        contact_email_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        contact_email_field.clear()
        contact_email_field.send_keys(word)

    def get_contact_email_text(self):
        contact_email_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        text = contact_email_field.get_attribute("value")
        logging.info(
            f"We find text '{text}' in contact email field {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}")
        return text

    def enter_contact_content_field(self, word):
        logging.info(f"Send {word} to contact content field {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}")
        contact_content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        contact_content_field.clear()
        contact_content_field.send_keys(word)

    def get_contact_content_text(self):
        contact_content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        text = contact_content_field.get_attribute("value")
        logging.info(
            f"We find text '{text}' in contact content field {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}")
        return text

    def click_contact_btn(self):
        logging.info("Click 'contact us' button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def switch_to_alert_contact(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"We find text {text} in alert")
        return text
