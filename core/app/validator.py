
class Validator():
    def __init__(self, data):
        self.data = data
    def validate(self):
        count = len(self.data)
        if count != 3:
            return False
        else:
            return True
    def valid(self):
        return self.validate()
