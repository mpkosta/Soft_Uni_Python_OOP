class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    #shortcut props + 'Tab'
    @property #getter
    def username(self):
        return self.__username

    @username.setter #setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_correct = len(value) >= 8
        is_digit = any([el for el in value if el.isdigit()])
        is_upper = any([el for el in value if el.isupper()])

        if not is_length_correct or not is_digit or not is_upper:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username","Passw0rd")
print(correct_profile)