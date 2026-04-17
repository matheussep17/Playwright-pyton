from  playwright.sync_api import Page, expect
import time

def test_all_locators(page: Page) :
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")

    #get by role
    #expect(page.get_by_role("button", name="Explicit Role Button")).to_be_visible()
    #expect(page.get_by_role("link", name="Explicit Role Link")).to_be_visible()
    #expect(page.get_by_role("img", name="robot icon")).to_be_visible()
    #expect(page.get_by_role("button", name="Implicit Button")).to_be_visible()
    #expect(page.get_by_role("link", name="Implicit Link")).to_be_visible()


    #get by text
    #expect(page.get_by_text("Locate elements by their visible text content.", exact=True)).to_be_visible()

    #get_by_label
    # page.get_by_label("Email Address").click()
    # expect(page.get_by_label("Email Address", exact=True)).to_be_visible()
    # page.get_by_label("Accept Terms and Conditions").click()
    # expect(page.get_by_label("Accept Terms and Conditions", exact=True)).to_be_visible()


    #get_by_placeholder
    #page.get_by_placeholder("Search for items...").click()
    # time.sleep(2)
    #page.get_by_placeholder("Enter your password").fill("MinhaSenha")

    #get_by_alt_text
    # expect(page.get_by_alt_text("python logo")).to_be_visible()
    # expect(page.get_by_alt_text("javascript logo")).to_be_visible()

    #get_by_title
    # expect(page.get_by_title("Save your changes")).to_be_visible()
    # expect(page.get_by_title("Go to homepage")).to_be_visible()

    #get_by_test_id
    expect(page.get_by_test_id("submit-button")).to_be_visible()
    expect(page.get_by_test_id("status-message")).to_be_visible()