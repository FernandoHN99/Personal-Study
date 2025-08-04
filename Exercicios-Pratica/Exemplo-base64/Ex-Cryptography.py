from cryptography.fernet import Fernet
import codecs
from src.util import Util

Util.clean_terminal()

key = Fernet.generate_key()
fernet = Fernet(key)
message = "o"
print('message:', message)
# ----------------------------------------------------------
encode_message = message.encode()
encrypted = fernet.encrypt(encode_message)
print('encode_message:', encode_message)
print('key_encrypted:', key)
print('encrypted:', encrypted)
# ----------------------------------------------------------
str_encrypted = codecs.decode(encrypted)
str_key = codecs.decode(key)
str_key = str_key.encode()
print('str_encrypted:', str_encrypted)
print('key_encrypted:', str_key)
# ----------------------------------------------------------
encrypted = bytes(str_encrypted, encoding='utf-8')
print('encrypted:', encrypted)
encode_message = fernet.decrypt(str_encrypted)
print('encode_message:', encode_message)
print('message:', encode_message.decode())
