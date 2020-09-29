with open('p059_cipher.txt', 'r') as f:
    encrypted = [int(i) for i in f.read().split(',')]

# loop over all possible password containing 3 lowercase letters
for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        for k in range(ord('a'), ord('z') + 1):
            password = chr(i) + chr(j) + chr(k)
            # inflate password to the length of the text
            pos = 0
            while len(password) < len(encrypted):
                password = password + password[pos]
                pos += 1
            # turn password into a key
            keys = [ord(c) for c in password]

            # decrypt message with current key
            decrypted = [encrypted[i] ^ keys[i] for i in range(len(keys))]
            # create a string out of the decrypted message
            message = ''.join((chr(i) for i in decrypted))
            # check for common english words
            if 'the' in message and 'of' in message and 'and' in message:
                print(password)
                print(message)
                print(sum(decrypted))
