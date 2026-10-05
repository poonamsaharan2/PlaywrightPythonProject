class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.get_by_role("button", name="login")
        self.login_error = page.get_by_text(
            "Epic sadface: Username and password do not match any user in this service"
        )

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()


