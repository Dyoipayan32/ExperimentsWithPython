from newAutomationFrameWorkPytest.PageObjectsUI import PageObjectsUI


def test_ui_validate_user_switches_to_new_browser_window(ui: PageObjectsUI):
    applicationUrl = "https://demo.automationtesting.in/Windows.html"
    ui.navigation.launch_application(applicationUrl)
    clickButtonXpath = ".//*[@id = 'Tabbed']/a/button[contains(text(), 'click')]"
    ui.navigation.click_button(clickButtonXpath)
    currentWindowHandleId = ui.navigation.get_current_window_handle_id()
    print("Parent window handle id", currentWindowHandleId)
    openedBrowserWindows = ui.navigation.get_opened_window_handles()
    ui.navigation.print_window_handle_ids(openedBrowserWindows)
    ui.navigation.print_browser_window_titles(openedBrowserWindows)

    # Recommended to perform maximum ONE close operation
    # as DRIVER.QUIT is already being performed in tear down
    # # closes parent window by handle id
    # ui.navigation.close_a_browser_window_by_handleId(openedBrowserWindows, currentWindowHandleId)

    # closes a parent window
    ui.navigation.close_a_browser_window_by_title(openedBrowserWindows, "Frames & windows")

    # # closes newly opened window
    # ui.navigation.close_a_browser_window_by_title(openedBrowserWindows, "Selenium")
