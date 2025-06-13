import string



USERNAME_CHARACTERS = string.ascii_letters + string.digits + ".@_-"
EXTENSION_CHARACTERS = string.ascii_letters
DOMAIN_CHARACTERS = string.ascii_uppercase

def este_valid(email):
    if "@" not in email:
        return False
    
    if "." not in email:
        return False

    username = email.split("@")[0]

    if not username: 
        return False
    
    if any(ch not in USERNAME_CHARACTERS for ch in email):
        return False
    
    if len(username) > 64:
        return False
    
    extensie = email.split(".") [-1]
    if len(extensie) < 2:
        return False
    
    if any ([ch not in EXTENSION_CHARACTERS for ch in extensie]):
        return False
    
    split_by_point_list = email.split(".")
    if any([not part for part in split_by_point_list]):
        return False
    
    if email.count("@") > 1:
        return False

    email.replace('@', ' ').replace('.', ' ').replace('-', ' ').replace('_', ' ').split(" ")

    return True




