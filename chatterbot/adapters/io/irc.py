from chatterbot.adapters.io import IOAdapter
from chatterbot.utils.read_input import input_function
import socket

class IRCAdapter(IOAdapter):
    def __init__():
        """
        Connects to IRC
        """
        server = input_function("Server: ")
        channel = input_function("Channel: ")
        
        ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ircsock.connect((server, 6667))
        
        ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Connected!\n") # user authentication
        ircsock.send("NICK "+ botnick +"\n") # assign the nickname
        ircsock.send("JOIN "+ channel +"\n") # connect to channel
    
    def process_input(self):
        """
        Read the user's input from the channel.
        """
        self.ircmsg = ircsock.recv(2048) # receive data from the server
        self.ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
        
        if ircmsg.find("PING: " != -1:
            self.ircsock.send("PONG :pingis\n")
        
        return self.ircmsg

    def process_response(self, statement):
        print(statement.text)
        return statement.text
