# Last modified: 7 May 2019

# you don't have to use the packages below, it is only a suggestion. 
# do not use any other python module unless it is explicitly permitted by the instructor.
from Crypto import Random
from Crypto.Util import Counter
import Crypto.Cipher.AES as AES


class Cloud:
    """
    the cloud stores your content encrypted.
    you can add variables and methods to this class as you want.
    """

    def __init__(self, filename, key=Random.get_random_bytes(32), nonce=Random.get_random_bytes(8)):
        """
        Encrypt the content of 'filename' and store its ciphertext at self.ciphertext
        The encryption to use here is AES-CTR with 32 byte key.
        The counter should begin with one.
        """
        self.key = key
        self.nonce = nonce
        with open(filename, mode='rb') as f:
            self.pt = f.read()
            self.countf = Counter.new(64, self.nonce)
            self.crypto = AES.new(self.key, AES.MODE_CTR, counter=self.countf)
            self.ciphertext = self.crypto.encrypt(self.pt)

    def Length(self):
        """
        Returns the length of the plaintext/ciphertext (they are of the same length).
        This is necessary so one would not read/write with an invalid position.
        """
        return len(self.ciphertext)

    def Read(self, position=0):
        """
        Returns one byte at 'position' from current self.ciphertext.
        position=0 returns the first byte of the ciphertext.
        """
        return self.ciphertext[position]

    def Write(self, position=0, newbyte='\x33'):
        """
        Replace the byte in 'position' from self.ciphertext with the encryption of 'newbyte'.
        Remember that you should encrypt 'newbyte' under the appropriate key (it depends on the position).
        Return the previous byte from self.ciphertext (before the re-write).
        """
        old_byte = self.ciphertext[position]
        # easy mode
        self.pt = self.pt[:position] + newbyte + self.pt[position + 1:]
        self.countf = Counter.new(64, self.nonce)
        self.crypto = AES.new(self.key, AES.MODE_CTR, counter=self.countf)
        self.ciphertext = self.crypto.encrypt(self.pt)
        return old_byte

        # countf = Counter.new(64, self.nonce, initial_value=position)
        # encrypted_byte = self.crypto.encrypt().
        # self.ciphertext = self.ciphertext[:position] + encrypted_byte + self.ciphertext[position + 1:-1]
        # return old_byte
