
class HomePage():

    def __init__(self, driver):
        self.driver = driver

    #Locators
    _email_field = "email"
    _password_field = "password"
    _login_button = "login"

    #Get field and button
    def getEmailField(self):
        return self.driver.find_element_by_name(self._email_field)

    def getPasswordField(self):
        return self.driver.find_element_by_name(self._password_field)

    def getLoginButton(self):
        return self.driver.find_element_by_name(self._login_button)

    #Actions
    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButon(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButon()

