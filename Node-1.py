import socket 
import sys

class AESCipher(object):
   
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')


# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to given address and port
server_address = ('', 8000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    print('waiting for connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('Message: 'data)
                new_cipher = AESCipher(key='mykey')
                decrypt1 = new_cipher.decrypt(data)
                print('First decryption: ', decrypt1)

                

s.sendall("GET / HTTP/1.1/r/n/r/n")
print s.recv()

