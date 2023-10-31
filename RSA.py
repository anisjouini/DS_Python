import os
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


class RSAClass:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def gen_keys(self, folder):
        key_pair = RSA.generate(1024)
        self.public_key = key_pair.publickey()
        self.private_key = key_pair
        public_key_file = os.path.join(folder, "public.pub")
        private_key_file = os.path.join(folder, "private.pem")

        with open(public_key_file, 'wb') as f:
            f.write(self.public_key.export_key('PEM'))
        f.close()
        with open(private_key_file, 'wb') as f:
            f.write(self.private_key.export_key('PEM'))
        f.close()

    def get_public_key(self):
        return binascii.hexlify(self.public_key.exportKey(format='PEM')).decode('ascii')

    def get_private_key(self):
        return binascii.hexlify(self.private_key.exportKey(format='PEM')).decode('ascii')

    def encrypt(self, word):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_text = cipher.encrypt(word.encode())
        return encrypted_text.hex()

    def decrypt(self, encrypted_word):
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted_message = cipher.decrypt(bytes.fromhex(encrypted_word))
        return decrypted_message

    def create_sig(self, word):
        signer = pkcs1_15.new(RSA.import_key(
            binascii.unhexlify(self.get_private_key())))
        hashed_word = SHA256.new(word.encode())
        return binascii.hexlify(signer.sign(hashed_word)).decode('ascii')

    def verify_sig(self, word, sig):
        try:
            hashed_word = SHA256.new(word.encode())
            pkcs1_15.new(RSA.import_key(binascii.unhexlify(self.get_public_key()))).verify(
                hashed_word, binascii.unhexlify(sig))
            return True
        except (ValueError, TypeError) as e:
            return False
