class Authentication_info:
    def __init__(self, username, password, confirm, email, permitions):
        self.username = username
        self.password = password
        self.confirm = confirm
        self.email = email
        self.permitions = permitions
        
class Auth_Admin_info:
    def __init__(self, username, password, email, permitions):
        self.username = username
        self.password = password
        self.email = email
        self.permitions = permitions
class Auth_Cistomer_info:
    def __init__(self, username, password, email ):
        self.username = username
        self.password = password
        self.email = email
        