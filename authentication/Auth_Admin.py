class Auth_Admin:
    def __init__(self, username, password, confirm, twostep, exit):
        self.username = username
        self.password = password
        self.confirm = confirm
        self.twostep = twostep
        self.exit = exit

    def login(self, username, password, twostep):
        self.username = username
        self.password = password
        self.twostep =twostep
        

    def logout(self, confirm, exit):
        self.confirm = confirm
        self.exit = exit