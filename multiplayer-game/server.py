import socket as sc

class Server :
    def __init__(self):
        self.server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        self.server.bind(('localhost', 12345))
        self.server.listen()
    
    def run(self):
        print('Server is running')
        while True:
            conn, addr = self.server.accept()
            print(f'Connection from {addr}')
            conn.send(b'Hello')
            conn.close()