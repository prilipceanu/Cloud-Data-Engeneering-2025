

def este_palindrom(cuvant):
    if cuvant == cuvant [::-1]:
        return True 
    else:
        return False


def test_palindrom():
    assert este_palindrom("kayak") == True, "Acest cuvant este palidrom"
    assert este_palindrom("masina") == False, "Acest cuvant nu este palindrom"

test_palindrom()