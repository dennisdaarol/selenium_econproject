import configparser

config = configparser.ConfigParser()
path = "/Users/dennisdaarol/PycharmProjects/ecomProject/Configurations/config.ini"
config.read(path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        email = config.get("common", "username")
        return email

    @staticmethod
    def getPassword():
        password = config.get("common", "password")
        return password


