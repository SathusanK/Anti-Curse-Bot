class Sinner:
    
    def __init__(self, post, name, keyword):
        self.name = name
        self.count = 0
#         self.keyword = keyword
#         self.post = post

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
    
#     def set_post(self, post):
#         self.post = post
#         return
#     
#     def get_post(self):
#         return self.post
    
#     def set_keyword(self, keyword):
#         self.keyword = keyword
#         return
#     
#     def get_keyword(self):
#         return self.keyword
    