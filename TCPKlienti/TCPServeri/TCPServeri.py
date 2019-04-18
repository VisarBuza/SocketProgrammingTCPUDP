import socket
import threading
import _thread
from socket import gethostname
import time
import random
import math
import sys

# metodat obligative
# IPADRESA
def getIpAddress(array):
    return array[0]

# NUMRIIPORTIT
def getClientPort(array):
    return array[1]

# BASHKETINGELLORE
def consonant(word):
    i = 0
    counter = 0
    while i < len(word):
        if word[i] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            counter += 1
        i += 1
    return counter

# PRINTIMI
def printo(sentence):
    return sentence.strip()

# EMRIIKOMPJUTERIT
def getComputerName():
    name = ''
    if gethostname() == None:
        name = '\nClient\'s name is unknown'
    else:
        name = str(gethostname())
    return name

# KOHA
def getTime():
    currentTime = str(time.ctime(time.time()))
    return currentTime

# LOJA
def game():
    array = []
    for i in range(7):
        array.append(random.randint(1, 49))
    return array

# FIBONACCI
def fibonacci(n): 
    a = 0
    b = 1
    if n < 1: 
        print("Incorrect input") 
    elif n == 1: 
        return a 
    elif n == 2: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b

 # KONVERTIMI
def converter(option, value):
    option=str(option)
    option=option.upper()
    
    if (option == "KILOWATTTOHORSEPOWER"):
        return int((value*1.341)*100)/100.0

    elif (option == "HORSEPOWERTOKILOWATT"):
        return int((value/1.341)*100)/100.0

    elif (option == "DEGREESTORADIANS"):
        return int((math.pi/180)*value*100)/100.0

    elif (option == "RADIANSTODEGREES"):
        return int((180/math.pi)*value*100)/100.0

    elif (option == "GALLONSTOLITERS"):
        return int(value*3.785*100)/100.0

    elif(option == "LITERSTOGALLONS"):
        return int((value/3.785)*100)/100.0

    else:
        return("Invalid expression")

# metodat e studentit
#Enkriptimi me cezar
def caesarCipherEncrypt(plaintext, offset):
    ciphertext = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if (char.isupper()):
            ciphertext += chr((ord(char)+offset-65) % 26+65)
        else:
            ciphertext += chr((ord(char)+offset-97) % 26+97)

    return ciphertext

#dekriptimi me cezar
def caesarCipherDecrypt(ciphertext, offset):
    plaintext = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if (char.isupper()):
            plaintext += chr((ord(char)-offset-65) % 26+65)
        else:
            plaintext += chr((ord(char)-offset-97) % 26+97)

    return plaintext
#socket methods

def createSocket():
    try:
        global serverSocket
        global host
        global port
        host='localhost'
        port=12000
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Creating socket...")
    except socket.error as msg:
        print("Socket creation error"+str(msg))


def bindSocket():
    try:
        global serverSocket
        global host
        global port
        print("Binding the port "+str(port))
        serverSocket.bind((host,port))
        serverSocket.listen(5)
        print("Server is listening")
    except socket.error as msg:
        print("Socket binding error"+str(msg)+"\nRetrying...")
        bindSocket()


def clientThread(connectionSocket, clientAddress):
    try:
        while True:
            try:
                option = connectionSocket.recv(128)
                option = option.decode()
            except:
                print("\nReceivng error didnt receiv option")
            
            if(option == '1'):
                data = "Ip e klientit eshte : "+str(getIpAddress(clientAddress))
                connectionSocket.send(str.encode(data))

            elif(option == '2'):
                data = "Numri i portit te klientit eshte : " + \
                    str(getClientPort(clientAddress))
                connectionSocket.send(str.encode(data))

            elif(option == '3'):
                data = (connectionSocket.recv(128)).decode()
                data1 = str(consonant(data))
                connectionSocket.send(str.encode(data1))

            elif(option == '4'):
                data = (connectionSocket.recv(128)).decode()
                data = printo(data)
                connectionSocket.send(str.encode(data))

            elif(option == '5'):
                data = "Your computer name is : "+str(getComputerName())
                connectionSocket.send(str.encode(data))

            elif(option == '6'):
                data = "The time is :"+str(getTime())
                connectionSocket.send(str.encode(data))

            elif(option == '7'):
                data = str(game())
                connectionSocket.send(str.encode(data))

            elif(option == '8'):
                n = connectionSocket.recv(128).decode()
                nthTerm = "The "+str(n)+"th term of the series is :" + \
                    str(fibonacci(int(n)))
                connectionSocket.send(str.encode(nthTerm))

            elif(option == '9'):
                mode = (connectionSocket.recv(128)).decode()
                value = float((connectionSocket.recv(128)).decode())
                data = str(converter(mode, value))
                connectionSocket.send(str.encode(data))

            elif(option == '10'):
                plainText = connectionSocket.recv(128).decode()
                shift = int(connectionSocket.recv(128).decode())
                cipherText = caesarCipherEncrypt(plainText, shift)
                cipherText = "The encrypted version is : "+cipherText
                connectionSocket.send(str.encode(cipherText))

            elif(option == '11'):
                cipherText = connectionSocket.recv(128).decode()
                shift = int(connectionSocket.recv(128).decode())
                plainText = caesarCipherDecrypt(cipherText, shift)
                plainText = "The decrypted version is : "+plainText
                connectionSocket.send(str.encode(plainText))
    except ConnectionResetError:
        print("\nClient disconnected from server ")
    except ConnectionAbortedError:
        print("\nClient disconnected from server ")

createSocket()
bindSocket()

while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print("Got connection from ", clientAddress[0], " : ", clientAddress[1])
    message="Connection established"
    connectionSocket.send(str.encode(message))
    threading.Thread(target=clientThread,args=(connectionSocket,clientAddress)).start()

connectionSocket.close()

