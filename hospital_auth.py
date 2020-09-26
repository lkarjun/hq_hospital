from cryptography.fernet import Fernet
from typing import Union
import yaml

fileName = 'credential/cred.yaml'
keyName = 'credential/Key.bin'


class Securing:

    def genKey(self):
        '''Generate key'''
        key = Fernet.generate_key()
        with open(keyName, 'wb') as key_to_file:
            key_to_file.write(key)

    def keyLoading(self) -> Union[bytes, str]:
        '''load key from file'''
        return open(keyName, 'rb').read()

    def encrypt_data(self) -> None:
        '''encrypt the credential file'''
        key = self.keyLoading()
        f = Fernet(key)
        with open(fileName, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)
        with open(fileName, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_data(self) -> None:
        '''decrypt the credential file'''
        key = self.keyLoading()
        f = Fernet(key)
        with open(fileName, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(fileName, 'wb') as file:
            file.write(decrypted_data)

if __name__ == '__main__':
    s = Securing()
    s.genKey
    s.encrypt_data()
    s.decrypt_data()