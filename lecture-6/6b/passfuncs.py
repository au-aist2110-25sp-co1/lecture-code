from hashlib import md5

def _hash_it(password):
    return md5(password.encode()).hexdigest()

_default_password = 'password123'
_password_hash = _hash_it(_default_password)

def check_password(password):
    return _hash_it(password) == _password_hash

def change_password(old_password, new_password):
    if check_password(old_password):
        global _password_hash
        _password_hash = _hash_it(new_password)
        print("Password changed!")
        return True
    else:
        print("Old password is incorrect. Password not changed.")
        return False
