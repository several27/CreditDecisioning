from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, Year: str=None, user_email: str=None):
        self.spark = None
        self.update(Year, user_email)

    def update(self, Year: str="2018", user_email: str="please_enter_your_email_address"):
        self.Year = Year
        self.user_email = user_email
        pass
