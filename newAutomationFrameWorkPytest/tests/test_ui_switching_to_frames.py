import time

from newAutomationFrameWorkPytest.PageObjectsUI import PageObjectsUI


def test_ui_validate_user_switches_between_frames(ui: PageObjectsUI):
    applicationUrl = "https://demo.automationtesting.in/Frames.html"
    ui.navigation.launch_application(applicationUrl)

    singleIframePaneXpath = ".//div[@class='tabpane']/ul/li/a[contains(text(),'Single Iframe')]"
    multipleIframePaneXpath = ".//div[@class='tabpane']/ul/li/a[contains(text(),'Iframe with in an Iframe')]"

    ui.navigation.scroll_middle_of_page()
    ui.navigation.switch_to_a_frame("SingleFrame")
    time.sleep(1)
    textBoxXpath  = ".//input[@type='text']"
    ui.navigation.click_button(textBoxXpath)
    ui.navigation.write_into_text_box(textBoxXpath, "Writing inside Single IFrame's textbox.")
    time.sleep(2)
    ui.navigation.switch_back_to_main_browser()
    ui.navigation.click_button(multipleIframePaneXpath)
    # ui.navigation.switch_to_a_frame("Multiple")
    # time.sleep(1)
    # ui.navigation.write_into_text_box(textBoxXpath, "Writing inside Multiple IFrame's textbox.")
    # time.sleep(2)


