# def word_count(s):
#     nop = set(["a", "the", "on", "at", "of", "upon", "in" ,"as"])

#     copy = ""

#     cont = 0

#     for x in s.lower():
    
#         if x.isalpha() and x !=" ":
#             copy+=x
#         else:
#             if copy  not in nop and copy!= "":
                
#                 cont+=1
#                 copy = ""
#     if copy  not in nop and copy!= "":
#         cont+=1
#     return cont

nop = set(["a", "the", "on", "at", "of", "upon", "in" ,"as"])
# s = "%^&abc!@# wer45tre"
s = """
        I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.
        """

copy = ""

cont = 0

for x in s.lower():
    print(x)
    if x.isalpha() and x !=" ":
        copy+=x
    else:
        if copy  not in nop and copy!= "":
            print(copy)
            cont+=1
            copy = ""
if copy  not in nop and copy!= "":
    cont+=1
print(copy)
print(cont)