from twisted.internet.protocol import Protocol

class Echo(Protocol):
    def dataRecieved(self, dat):
        self.transport.write(data)
        
