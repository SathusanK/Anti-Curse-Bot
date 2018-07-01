class Sinner:
    
    def __init__(self, post, name, keyword):
        self.post = post
        self.name = name
        self.keyword = keyword
    
    def set_post(self, post):
        self.post = post
        return
    
    def get_post(self):
        return self.post
    
    def set_name(self, name):
        self.name = name
        return
    
    def get_name(self):
        return self.name
    
    def set_keyword(self, keyword):
        self.keyword = keyword
        return
    
    def get_keyword(self):
        return self.keyword
    