import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # handling the requests
    def handle(self, client):
        try:
            with client:
                data = ""
                incoming = client.recv(1024)
                while len(incoming):
                    data += incoming
                    incoming = client.recv(1024)
                print(f"data recieved at port:{self.port} \n{data}")
                response = "Response back from server " + data
                client.sendall(response.encode('utf-8'))

        except Exception as e:
            print(f"error - {e}")

        finally:
            client.close()

    # start the server

    # end the server