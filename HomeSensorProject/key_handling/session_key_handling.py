from rsa.key import PrivateKey

#THIS METHOD EXPORTS PRIVATE KEYS FROM THE STORAGE
def read_session_PrivKey():
    f = open("session_priv_key", "rb")
    key = f.read()
    cipher = PrivateKey.load_pkcs1(key)
    f.close()
    return cipher