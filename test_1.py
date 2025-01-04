from testpage import OperationsHelper
import logging
import yaml, time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata["username"]
passwd = testdata["password"]
email = testdata["email"]


class TestNegative:
    def test_step1(self, browser):
        logging.info("Test1 Starting")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.enter_login("test")
        testpage.enter_pass("test")
        testpage.click_login_button()
        assert testpage.get_error_text() == "401"


class TestPositive:
    def test_step2(self, browser):
        logging.info("Test2 Starting")
        testpage = OperationsHelper(browser)
        testpage.enter_login(name)
        testpage.enter_pass(passwd)
        testpage.click_login_button()
        time.sleep(7)
        assert testpage.get_user_text() == f"Hello, {name}"

    def test_step3(self, browser):
        logging.info("Test3 Starting")
        testpage = OperationsHelper(browser)
        testpage.click_new_post_btn()
        testpage.enter_title("testtitle")
        testpage.enter_content("testcontent")
        testpage.enter_description("testdesc")
        testpage.click_save_btn()
        time.sleep(20)
        assert testpage.get_res_text() == "testtitle"

    def test_step4(self, browser):
        logging.info("Test4 Starting")
        testpage = OperationsHelper(browser)
        testpage.click_contact_link()
        time.sleep(20)
        assert testpage.get_contact_title_text() == "Contact us!"
        testpage.enter_contact_name_field(name)
        assert testpage.get_contact_name_text() == name
        testpage.enter_contact_email_field(email)
        assert testpage.get_contact_email_text() == email
        testpage.enter_contact_content_field("Content for contact")
        assert testpage.get_contact_content_text() == "Content for contact"
        testpage.click_contact_btn()
        time.sleep(7)
        assert "Form successfully submitted" in testpage.switch_to_alert_contact()
