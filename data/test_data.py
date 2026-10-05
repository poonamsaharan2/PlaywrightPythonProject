LOGIN_DATA = {
    "USERNAME": "standard_user",
    "PASSWORD": "secret_sauce"
}
BASE_URL = "https://www.saucedemo.com/"
CUSTOMER_DATA = {
    "FIRST_NAME": "Poonam",
    "LAST_NAME": "Saharan",
    "ZIP_CODE": "125001"
}

NEGATIVE_LOGIN_DATA = [
    ("standard_user", "wrong_password"),
    ("wrong_user", "secret_sauce"),
    ("wrong_user", "wrong_password"),
]