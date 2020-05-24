## What is this project? ##
This project is a simple version of a TV quiz game show. There is a host and 3 participants. The host
randomly chooses a question, ensuring that they
are not repeated. The first participant to press the buzzer gets a
chance to answer the question. If the answer is correct, the participant gets 1
point. Otherwise, no points are awarded.

## How to execute the Project? ##
- There are 2 files : client.py and server.py
- Open a terminal and execute the command :
servr.py 127.0.0.1 8008
- Open three other terminals and execute the
command : client.py 127.0.0.1 8008
- The server broadcasts a question to all 3 clients.
If any of the clients know the answer, they must
enter the word ‘buz’. Once a client presses the buzzer, no other clients will be allowed to press
the buzzer.
- The client who entered ‘buz’ now needs to type
the answer.
- The game ends when either of the clients gets 5
points or if the 20 questions that the server has
are exhausted.
- This program works only when there are 3 clients.

### Reference: https://www.geeksforgeeks.org/socket-programming-python/ ###
