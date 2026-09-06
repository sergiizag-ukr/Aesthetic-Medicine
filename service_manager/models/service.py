class Service():

    def __init__(self, client):
        self.client = client
        self.service = ""
        self.date = ""
        self.price = 1000

    def __str__(self):
        return f"{self.service} - {self.price}"