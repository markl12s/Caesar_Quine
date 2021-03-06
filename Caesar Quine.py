def caesar_quine():
    import inspect
    plain_txt = inspect.getsource(caesar_quine)
    encrypted_msg = []
    length = len(plain_txt)

    for i in range(length): encrypted_msg.append(plain_txt[i])

    for e in range(length):
        encrypted_msg[e] = (ord(encrypted_msg[e]))
        encrypted_msg[e] = (encrypted_msg[e] + 3) % 256
        encrypted_msg[e] = bin(encrypted_msg[e])

    print(' '.join(encrypted_msg))

caesar_quine()
