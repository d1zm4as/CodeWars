from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    state = Nothing
    
    for x in lst:
        if x == state:
            state = Nothing
        else:
            state = x
    return state