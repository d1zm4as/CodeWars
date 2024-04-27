def get_users_ids(st):
    lista = []
    for s in st.split(","):
        s = s.replace("#","")
        s = s.replace("uid","",1)
        s = s.lower()
        s = s.strip(" ")
        lista.append(s)
    return lista