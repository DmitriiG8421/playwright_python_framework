from playwright.sync_api import Page, expect
import time
import random

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    URL = "https://faruk-hasan.com/automation/playwright-selenium-cypress-practice.html"

    def M1_Dropdown_Menu(self):
        self.page.select_option("select#pizza-size", "small")
        self.page.locator("button", has_text="Confirm Selection").click()

    def M2_Checkbox(self):
        self.page.locator("input[type='checkbox'][value='cheese']").check()
        self.page.locator("button", has_text="Confirm Toppings").click()

    def M3_Radio_buttons(self):
        self.page.locator("input[type='radio'][value='credit']").check()
        self.page.locator("button",has_text="Confirm Payment").click()


    def Mission4_Date_Picker(self):
        self.page.locator("input[type='date']").fill("2025-05-17")
        self.page.locator("button",has_text="Confirm Date").click()

    def M5_Drag_and_Drop(self):
        source = self.page.locator("#draggable")
        target = self.page.locator('#drop-container')
        target.scroll_into_view_if_needed()
        source.drag_to(target)
        print("HELLLLLLOOOOOOOOOO")

    def M6_Button_Interaction(self):
        self.page.locator("button",has_text="Click to Complete").click()


    def M7_Search_Functionality(self):
        location = self.page.locator("#search-input")
        location.fill("Margherita")
        self.page.locator("button",has_text="Search").click()

    def M8_hide_M7_function(self):
        self.page.locator("#hide-element .primary-button").click()


    def M9_persistant_hide_M7_function(self):
        self.page.locator("#persistent-hide .primary-button").click()

    def M8_M9_click_button(self,location):
        self.page.locator(location).click()

        




