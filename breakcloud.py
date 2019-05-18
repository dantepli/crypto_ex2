from cloud import *


def breakcloud(cloud):
    """
    receives 'cloud', an object of type Cloud.
    creates a file with the name 'plain.txt' that stores the current text that is encrypted in the cloud.
    you can use only the Read/Write interfaces of Cloud (do not use its internal variables.)
    """
    with open('plain.txt', 'wb') as f:
        file_len = cloud.Length()
        for i in range(file_len):
            prev_byte = cloud.Write(i, b'\0')
            encrypted_byte = cloud.Read(i)
            decrypted = chr(ord(prev_byte) ^ ord(encrypted_byte))
            f.write(decrypted)


