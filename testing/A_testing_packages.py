class TestConstructors:
    def test_constructor(self, TAuth, TData, TCore):
        
        self.TAuth = TAuth
        self.TData = TData
        self.TAuth = TCore

class Auth_testing:
    def __init__(self, TAuth):
        self.TAuth = TAuth
class Core_testing:
    def __init__(self, TCore ):
        self.TAuth = TCore
class DB_testing:
    def __init__(self, TData):
        self.TData = TData