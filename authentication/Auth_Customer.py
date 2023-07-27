class Auth_Customer:
    def __init__(self, username, password, confirm, exit):
        self.username = username
        self.password = password
        self.confirm = confirm
        self.exit = exit
class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class logout:
    def __init__(self, confirm, exit):
        self.confirm = confirm
        self.exit = exit