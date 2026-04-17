from  playwright.sync_api import Page, expect
import time

def test_actions(page: Page) -> None:
    page.set_viewport_size({"width": 800, "height": 600})
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    # page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    # page.get_by_role("textbox", name="Password: (1234)").fill("1234")

    #press_sequentially
    # page.get_by_role("textbox", name="Username: (admin)").press_sequentially("admin", delay=200)
    # page.get_by_role("textbox", name="Password: (1234)").press_sequentially("1234", delay=200)
    # page.get_by_role("textbox", name="Select a date:").press_sequentially("02061998", delay=100)

    #check
    # page.get_by_role("checkbox", name="Feature 1").check()
    # expect(page.get_by_role("checkbox", name="Feature 1")).to_be_checked()
    # page.get_by_role("radio", name="Option B").check()
    # expect(page.get_by_role("radio", name="Option B")).to_be_checked()

    #select options
    #page.get_by_label("Choose an option:").select_option("Option 3")

    # click actions
    page.get_by_text("Single Click").click()
    expect(page.get_by_text("Single click button clicked successfully!")).to_be_visible()