


import secrets


for x in range(2):
    key = secrets.token_hex(4) # 8 bytes = 16 hex characters
    print(key)