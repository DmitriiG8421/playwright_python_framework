import pytest
from playwright.sync_api import Page, expect
import time

from pages.home_page import HomePage

# Matches what you set in test_signup_and_save_session
EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

@pytest.mark.smoke
def test_mission_session(page: Page):

    homePage = HomePage(page)
    page.goto(homePage.URL)


    homePage.M1_Dropdown_Menu()
    strong_M1 = page.locator("#dropdown-result strong")
    expect(strong_M1).to_contain_text("small")

    homePage.M2_Checkbox()
    strong_M2 = page.locator("#checkbox-result strong")
    expect(strong_M2).to_contain_text("Cheese")

    homePage.M3_Radio_buttons()
    strong_M3 = page.locator("#radio-result strong")
    expect(strong_M3).to_contain_text("credit")

    homePage.Mission4_Date_Picker()
    strong_M4 = page.locator("#date-result strong")
    expect(strong_M4).to_contain_text("Saturday, May 17, 2025")


    homePage.M5_Drag_and_Drop()
    strong_M5 = page.locator("#drag-result strong")
    expect(strong_M5).to_contain_text("Success!")


    homePage.M6_Button_Interaction()
    strong_M6 = page.locator("#button-result strong")
    possible_lines = ["Click-tastic work!","You clicked the button!","Button clicks are fun!","You're a natural button clicker!","Great job clicking!"]
    found = False
    strong_M6_text_contents = strong_M6.text_content()
    if strong_M6_text_contents in possible_lines:
        found = True
    assert found is True


    homePage.M7_Search_Functionality()
    strong_M7 = page.locator("#search-result strong")
    expect(strong_M7).to_contain_text("Margherita")


    homePage.M8_M9_click_button("#hide-element .primary-button")
    strong_M8_P1 = page.locator("#hide-result strong")
    expect(strong_M8_P1).to_contain_text("Mission 7 is now hidden!")


    homePage.M8_M9_click_button("#hide-element .primary-button")
    strong_M8_P1 = page.locator("#hide-result strong")
    expect(strong_M8_P1).to_contain_text("Mission 7 is now visible!")


    homePage.M8_M9_click_button("#persistent-hide .primary-button")
    strong_M9_P1 = page.locator("#persistent-hide strong")
    expect(strong_M9_P1).to_contain_text("Mission 7 is now permanently hidden!")

    homePage.M8_M9_click_button("#persistent-hide .primary-button")
    strong_M9_P2 = page.locator("#persistent-hide strong")
    expect(strong_M9_P2).to_contain_text("Mission 7 is now visible!")


    print(f"\n[TEST] Verified mission session with title: {page.title()}")
    time.sleep(5)