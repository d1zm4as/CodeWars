from statistics import median

def get_middle(s):
    if len(s) ==1:
        return s
    if len(s)%2==0:
        mei = round(len(s)/2)
        meio = f"{s[mei-1]}{s[mei]}"
        return meio
    if len(s)%2!=0:
        mei= len(s)//2
        return s[mei]
