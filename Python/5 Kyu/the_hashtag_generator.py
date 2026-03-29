def generate_hashtag(s):
    #your code here
    if not s:
        return False
    copy = "".join([x.title() for x in s.split()])
    
    copy = "#" + copy
    
    if len(copy) >140:return False
    
    return copy