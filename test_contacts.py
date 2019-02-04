# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contacts import Contacts

class TestContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.open_add_new_page(wd)
        self.create_new_contact(wd, Contacts(firstname="Kseniya", lastname="Kalenik", title="Tester", company="GoodCompany Inc.",
                                address="Chicago, Il", phonenumber="3121111111", email="test@gmail.com", bday="18",
                                bmonth="January", byear="1985", notes="testwww"))
        self.enter_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def enter_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def create_new_contact(self, wd, Group):
        self.contact_name(Group, wd)
        self.contact_title(Group, wd)
        self.contact_company(Group, wd)
        self.contact_address(Group, wd)
        self.contact_phonenumber(Group, wd)
        self.contact_email(Group, wd)
        self.contact_birthsday(Group, wd)
        self.contact_notes(Group, wd)

    def contact_notes(self, Group, wd):
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Group.notes)

    def contact_birthsday(self, Group, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Group.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Group.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Group.byear)

    def contact_email(self, Group, wd):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Group.email)

    def contact_phonenumber(self, Group, wd):
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Group.phonenumber)

    def contact_address(self, Group, wd):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Group.address)

    def contact_company(self, Group, wd):
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Group.company)

    def contact_title(self, Group, wd):
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Group.title)

    def contact_name(self, Group, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Group.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Group.lastname)

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.get("http://localhost/addressbook/delete.php?part=1;")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
