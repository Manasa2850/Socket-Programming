import socket
import select
from thread import *
import sys
import time
import random


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients=[]

Q = ["Which was the first network? (a)ARPANET (b)ASAPNET", "Which protocol is used for email? (a)SMTP (b)UDP", "How many addresses are there in IPv4? (a)2^8 (b)2^4", "Combination of two or more networks are called (a)LAN (b)Internetwork", "Which topology covers security, robust and eliminating traffic factor? (a)Mesh (b)Star", "Multipoint topology is (a)Bus (b)Ring", "A switch in a datagram network uses a (a)Destination address (b)Routing Table", "An applet is a program written in Java on the (a)Server (b)Client", "To create Web Pages we use a term, called (a)WWW (b)HTML", "Each packet is routed independently in (a)Datagram Subnet (b)Virtual Circuit", "What is the full form of RAM? (a)Read accept memory (b)Random access memory", "Which TCP port is used by Telnet to connect server applications (a)Port 23 (b)Port 43", "A Circuit-Switched Network is made of a set of switches connected by physical (a)Links (b)Nodes", "Routing processor searching for routing table is called (a)Switch Fabric (b)Table Lookup", "Domain, which is used to map an address to a name is called (a)Generic Domain (b)Inverse Domain", "Both station can transmit and receive data simultaneously in (a)Half Duplex (b)Full Duplex", "Information can be represented as a sequence of (a)Characters (b)Bit Patterns", "How many bits in data unit has changed in single bit error? (a)1 (b)2", "In Asynchronous Balanced Mode (ABM), link is (a)Unidirectional (b)Point to Point", "Parameter that refers to recording and broadcasting of picture is (a)Video (b)Image"]
A = ['a', 'a', 'b', 'b', 'a', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'a', 'b', 'b', 'b', 'b', 'a', 'b', 'a']
Count=[]
cll = ["manasa",-1]
buz =[0, 0]
p = [-1]
def clientthread(conn, addr):
    conn.send("Welcome to this Quiz!\n")

    while True:

            message = conn.recv(2048)
            if message:
                if buz[0]==0:
                    cll[0] = conn
                    buz[0] = 1
                    i = 0
                    while i < len(list_of_clients):
                        if list_of_clients[i] == conn:
                            break
                        i +=1
                    cll[1] = i+1

                elif buz[0] ==1 and conn==cll[0]:

                        print (p[0])
                        print A[p[0]]

                        if message[0] == A[p[0]]:
                            broadcast("player" + str(cll[1]) + " +1" + "\n")
                            Count[i] += 1
                            if Count[i]==5:
                                print("\n")
                                broadcast("Player" + str(cll[1]) + " is the winner!! \n")
                                broadcast("GAME OVER!! \n")
                                for i in range(len(list_of_clients)):
                                    broadcast("Player "+ str(i+1) + " scored "+ str(Count[i])+ "\n")

                                buz[1]=1




                        else:
                            broadcast("player" + str(cll[1]) + " 0" + "\n")
                            Count[i] = Count[i]
                        A.pop(p[0])
                        if len(Q)!=0:
                            Q.pop(p[0])
                        buz[0]=0


                        if len(Q)==0 and buz[1]==0:

                            buz[1]=1
                            j = Count.index(max(Count))
                            broadcast("player " + str(j+1)+ " wins!! \n")
                            broadcast("GAME OVER \n")
                            for i in range(len(list_of_clients)):
                                    broadcast("Player "+ str(i+1) + " scored "+ str(Count[i]))
                                    broadcast("\n")

                        if buz[1]==0:
                            quiz()
                else:
                    conn.send("Player "+str(cll[1])+" has already pressed buzzer!")


            else:
                    remove(conn)


def broadcast(message):
    for clients in list_of_clients:
        try:
            clients.send(message)
        except:
            clients.close()
            remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def quiz():
    if len(Q) != 0:
        ques = random.choice(Q)
        print len(Q)
        for i in range(len(Q)):
            if ques==Q[i]:
                p[0] = i

        for connection in list_of_clients:
            connection.send(ques)

while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)
    Count.append(0)
    print addr[0] + " connected"

    start_new_thread(clientthread,(conn,addr))
    if(len(list_of_clients)==3):
        time.sleep(1)
        quiz()

conn.close()
server.close()
