# Built-in libraries
# import time
import pickle

#External libraries for Reddit use
# import praw
# from praw.models import MoreComments

# Personal scripts and files
# import sinner

# def check(author, value_exists):
def check(author):
    '''
    Iterates through all the sinners and adds them to the text file list if they do not exist.
    
    Returns whether or not the sinner is a repeat offender (variable: value_exists)
    
    Variables:
    sinners - text files of sinners
    sinner_list - array of sinners
    value_exists - boolean value of whether or not the sinner exists in the txt file
    '''
    value_exists = False
    sinners = open('sinners.txt', "r+")
    
    line = sinners.readline()
    while line.strip() != '':
        if str(author) in line:
            value_exists = True
            break
        else:
            line = sinners.readline()
    
    if value_exists == False:
        sinners.write(str(author) + '\n')
        
    sinners.close()
        
    return value_exists

def update_count(author):
    '''
    Updates the sin count of the author
    **IMPORTANT** In this context, the author variable is an object
    
    Variables:
    author - author object from Reddit API
    '''
    return

def srch(subreddit, KEYWORDS):
    '''
    Checks the 20 "hot" submissions in a subreddit for a keyword.
    Then, it will send the data to another function where a sinner
    class will be created and user data is stored.
    
    Variables:
    value_exists - boolean value of whether or not the sinner exists in the txt file
    author - string of the author's username
    '''
    
    for submission in subreddit.hot(limit=20):
        submission.comments.replace_more(limit=None)
        submission.comments_sort = 'hot'
        for comment in submission.comments.list():
            author = comment.author
            split_comment = comment.body.lower().split(' ')
            
#             print(author)
#             print(split_comment)
            
            for word in split_comment:
                if word in KEYWORDS:
                    value_exists = check(author)
#                     print(author)
#                     print(split_comment)
                    
                    if value_exists == True:
                        continue
                    else:
#                         update_count(comment.author) #function that checks the sin count
                        return
            
    return