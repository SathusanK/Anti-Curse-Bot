class Offender:
    
    def __init__(self, name, count):
        self.name = name
        self.count = 0
        return

    def set_name(self, name):
        self.name = name
        return
    
    def get_name(self):
        return self.name
    
    def set_count(self, count):
        self.count = count
        return
    
    def get_count(self):
        return self.count
    
    def add_count(self):
        self.count += 1
        return