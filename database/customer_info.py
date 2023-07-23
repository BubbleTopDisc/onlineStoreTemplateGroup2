class Customer_info:
    def __init__(self, name, email, address, membership, user_history, reports, ratings ):
        self.name = name
        self.email = email
        self.address = address
        self.membership = membership
        self.user_history = user_history
        self.reports = reports
        self.ratings = ratings

class Customer_histoy:
    def __init__(self, name, user_history, reports) :
        self.name = name
        self.user_history = user_history
        self.reports = reports

class user_rattings:
    def __init__(self,name, email, user_history,reports ,ratings ):
        self.name = name
        self.email = email
        self.user_history = user_history
        self.reports = reports
        self.ratings = ratings