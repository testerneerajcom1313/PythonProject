import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")
class Read_config :
    @staticmethod
    def get_URL():
        url = config.get('admin login info','URL')
        return url
    @staticmethod
    def get_username():
        username = config.get('admin login info','username')
        return username
    @staticmethod
    def get_password():
        password = config.get('admin login info','password')
        return password
