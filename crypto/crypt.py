import os

import gnupg

gpg = gnupg.GPG()

def generate_keypair(key_name, key_size=2048):
    keys = gpg.gen_key(key_name, key_size, key_type='RSA', expire_days=0)
    return keys


def encrypt_message(message, public_key):
    encrypted_data = gpg.encrypt(message, public_key, always_trust=True)
    return encrypted_data.data


def decrypt_message(encrypted_message, private_key):
    decrypted_data = gpg.decrypt(encrypted_message, private_key, always_trust=True)
    return decrypted_data.data


def sign_message(message, private_key):
    signed_data = gpg.sign(message, private_key, clearsign=True)
    return signed_data.data


def verify_signature(signed_message, public_key):
    verified_data = gpg.verify(signed_message, public_key)
    return verified_data.valid
