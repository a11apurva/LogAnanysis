
def case_sensitive(w1,w2):
    if w1==w2 :
        return True
    else:
        return False


def case_insensitive(w1,w2):
    if w1.lower() == w2.lower() :
        return True
    else:
        return False




def str_cmp(w1,w2,sensitive=True):
    if sensitive == True :
        return case_sensitive(w1,w2)
    if sensitive == False :
        return case_insensitive(w1,w2)


