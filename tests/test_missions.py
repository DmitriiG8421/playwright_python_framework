import pytest
from playwright.sync_api import Page, expect
from pages.home_page import HomePage

EXPECTED_TITLE = "Playwright, Selenium & Cypress Practice | Interactive Automation Testing Playground"

@pytest.fixture
def homepage(page: Page):
    homepage = HomePage(page)
    page.goto(homepage.URL)
    assert page.title() == EXPECTED_TITLE
    return homepage

@pytest.mark.smoke
class TestMissionSession:

    def test_m1_dropdown(self, page: Page, homepage: HomePage):
        homepage.M1_Dropdown_Menu()
        expect(page.locator("#dropdown-result strong")).to_contain_text("small")

    def test_m2_checkbox(self, page: Page, homepage: HomePage):
        homepage.M2_Checkbox()
        expect(page.locator("#checkbox-result strong")).to_contain_text("Cheese")

    def test_m3_radio_buttons(self, page: Page, homepage: HomePage):
        homepage.M3_Radio_buttons()
        expect(page.locator("#radio-result strong")).to_contain_text("credit")

    def test_m4_date_picker(self, page: Page, homepage: HomePage):
        homepage.Mission4_Date_Picker()
        expect(page.locator("#date-result strong")).to_contain_text("Saturday, May 17, 2025")

    def test_m5_drag_and_drop(self, page: Page, homepage: HomePage):
        homepage.M5_Drag_and_Drop()
        expect(page.locator("#drag-result strong")).to_contain_text("Success!")
        
    

    def test_m6_button_interaction(self, page: Page, homepage: HomePage):
        homepage.M6_Button_Interaction()
        result_text = page.locator("#button-result strong").text_content()
        valid_responses = [
            "Click-tastic work!",
            "You clicked the button!",
            "Button clicks are fun!",
            "You're a natural button clicker!",
            "Great job clicking!"
        ]
        assert result_text in valid_responses

    def test_m7_search(self, page: Page, homepage: HomePage):
        homepage.M7_Search_Functionality()
        expect(page.locator("#search-result strong")).to_contain_text("Margherita")

    def test_m8_hide(self, page: Page, homepage: HomePage):
        homepage.M8_M9_click_button("#hide-element .primary-button")
        strong_M8_hide = page.locator("#hide-result strong")
        expect(strong_M8_hide).to_contain_text("Mission 7 is now hidden!")

        homepage.M8_M9_click_button("#hide-element .primary-button")
        strong_M8_show = page.locator("#hide-result strong")
        expect(strong_M8_show).to_contain_text("Mission 7 is now visible!")



    def test_m9_hide(self, page: Page, homepage: HomePage):


        homepage.M8_M9_click_button("#persistent-hide .primary-button")
        strong_M9_hide = page.locator("#persistent-hide strong")
        expect(strong_M9_hide).to_contain_text("Mission 7 is now permanently hidden!")

        homepage.M8_M9_click_button("#persistent-hide .primary-button")
        strong_M9_show = page.locator("#persistent-hide strong")
        expect(strong_M9_show).to_contain_text("Mission 7 is now visible!")
