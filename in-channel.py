import socket
import re
if(text.find(':.in-oper') != -1):         # Gets triggered when a user types .in-oper
            nick_pattern = ":(.*?)\!"     # Defines how to search for a nickname
            nick_substring = re.search(nick_pattern, text)  # Finds the users nickname
            conn.send(bytes('WHO #bot\n', "UTF-8"))         # Gets a list of users in a channel
            count = 0
            done = False                                    # Makes the count not set to done
            who = conn.recv(2048).decode("UTF-8")           # Recive data
            print('Lenth is: ' + str(len(who.encode('utf-8')))) # Print the lenth of the data (Debugging purposes)
            if(nick_substring):                             # Checks if th nickname is valid
                nick = nick_substring.group(1)              # Gets the nickname
            if(who.find('#bot ' + nick + ' ') != -1):       # Finds if the user is in #bot
                conn.send(bytes("PRIVMSG " + '#channel' + " Your in #bot\n", 'UTF-8')) # Alerts the channel that your in #bot
            else:       # Finds if the user is not in #bot
                conn.send(bytes("PRIVMSG " + '#channel' + " Your not in #bot\n", 'UTF-8'))  # Sends that your not in #bot
            who = None  # Sets bot to None to avoid old data
            
            # I think I need to loop through fetching data to get the whole /WHO list I don't know how to do this though.
