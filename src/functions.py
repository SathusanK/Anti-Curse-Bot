# Built-in libraries
# import time

#External libraries for Reddit use
# import praw
# from praw.models import MoreComments

# Personal scripts and files
# import sinner

def check(author, check_value):
    sinners = open('sinners.txt', "r+")
                    
    sinner_list = []
    for line in sinners.readlines():
        if line not in sinner_list:
            sinner_list.append(line.strip())
        
    if str(author) not in sinner_list:
        sinners.write(str(author) + '\n')
        check_value = True

    sinners.close()
    return check_value

def srch(subreddit, KEYWORDS):
    '''
    Checks the 20 "hot" submissions in a subreddit for a keyword.
    Then, it will send the data to another function where a sinner
    class will be created and user data is stored.
    '''
    
    check_value = False
    
    for submission in subreddit.hot(limit=20):
        submission.comments.replace_more(limit=None)
        submission.comments_sort = 'hot'

        for comment in submission.comments.list():
            author = comment.author
            split_comment = comment.body.lower().split(' ')
            
            for word in split_comment:
                if word in KEYWORDS:
                    check_value = check(author, check_value)
                    print(author)
                    print(split_comment)
                    
                    if check_value == False:
                        continue
                    else:
                        break
                    
    return