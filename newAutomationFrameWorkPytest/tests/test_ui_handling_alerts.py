from selenium.webdriver import Keys

from newAutomationFrameWorkPytest.PageObjectsUI import PageObjectsUI


def test_ui_validate_user_clicks_on_alert(ui: PageObjectsUI):
    applicationUrl = "https://demo.automationtesting.in/Alerts.html"
    ui.navigation.launch_application(applicationUrl)
    alertWithOKButtonXpath = ".//*[@id='OKTab']/button"
    ui.navigation.click_button(alertWithOKButtonXpath)
    ui.navigation.accepts_alert()


def test_ui_validate_user_accepts_alert(ui: PageObjectsUI):
    applicationUrl = "https://demo.automationtesting.in/Alerts.html"
    ui.navigation.launch_application(applicationUrl)
    okCanceltabPaneXpath = ".//div[contains(@class, 'tabpane')]/ul/li/a[@href='#CancelTab']"
    ui.navigation.click_button(okCanceltabPaneXpath)
    alertWithOKCancelButtonXpath = ".//*[@id='CancelTab']/button"
    ui.navigation.click_button(alertWithOKCancelButtonXpath)
    ui.navigation.accepts_alert()


def test_ui_validate_user_rejects_alert(ui: PageObjectsUI):
    applicationUrl = "https://demo.automationtesting.in/Alerts.html"
    ui.navigation.launch_application(applicationUrl)
    okCanceltabPaneXpath = ".//div[contains(@class, 'tabpane')]/ul/li/a[@href='#CancelTab']"
    ui.navigation.click_button(okCanceltabPaneXpath)
    alertWithOKCancelButtonXpath = ".//*[@id='CancelTab']/button"
    ui.navigation.click_button(alertWithOKCancelButtonXpath)
    ui.navigation.rejects_alert()


def test_ui_validate_user_writes_into_alert_textbox(ui: PageObjectsUI):
    applicationUrl = "https://demo.automationtesting.in/Alerts.html"
    ui.navigation.launch_application(applicationUrl)
    textBoxtabPaneXpath = ".//div[contains(@class, 'tabpane')]/ul/li/a[@href='#Textbox']"
    ui.navigation.click_button(textBoxtabPaneXpath)
    alertWithTextboxButtonXpath = ".//*[@id='Textbox']/button"
    ui.navigation.click_button(alertWithTextboxButtonXpath)
    # ui.navigation.writes_into_alert(Keys.DELETE)
    ui.navigation.writes_into_alert("Hello")
    ui.navigation.accepts_alert()

