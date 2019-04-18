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


#krijimi i soketit
def createSocket():
    global serverSocket
    global serverPort
    global serverName
    try:
        serverPort=12000
        serverName='localhost'
        serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print("Creating socket...")
    except socket.error as msg:
        print("Socket could not be created "+str(msg))
#soket binding
def bindSocket():
    try:
        global serverName
        global serverSocket
        global serverPort
        serverSocket.bind((serverName,serverPort))
        print("Binding the socket "+str(serverPort))
        print("The socket is ready to receive")
    except socket.error as msg:
        print("Socket could not be created "+str(msg))

createSocket()
bindSocket()

while True:
    message,clientAddress=serverSocket.recvfrom(128)
    option=message.decode()
    
    print("Got request "+str(option)+" from |IP: "+str(clientAddress[0])+" |Port: "+str(clientAddress[1]))
    if(option == '1'):
        data = "Ip e klientit eshte : "+str(getIpAddress(clientAddress))
        serverSocket.sendto(data.encode(),clientAddress)

    elif(option == '2'):
        data = "Numri i portit te klientit eshte : " +str(getClientPort(clientAddress))
        serverSocket.sendto(data.encode(),clientAddress)
    
    elif(option == '3'):
        data ,clientAddress=serverSocket.recvfrom(128)
        data1 = str(consonant(data.decode()))
        serverSocket.sendto(data1.encode(),clientAddress)

    elif(option == '4'):
        data ,clientAddress=serverSocket.recvfrom(128)
        data = printo(data.decode())
        serverSocket.sendto(data.encode(),clientAddress)

    elif(option == '5'):
        data = "Your computer name is : "+str(getComputerName())
        serverSocket.sendto(data.encode(),clientAddress)

    elif(option == '6'):
        data = "The time is :"+str(getTime())
        serverSocket.sendto(data.encode(),clientAddress)

    elif(option == '7'):
        data = str(game())
        serverSocket.sendto(data.encode(),clientAddress)

    elif(option == '8'):
        n ,clientAddress=serverSocket.recvfrom(128)
        nthTerm = "The "+str(n.decode())+"th term of the series is :" + \
            str(fibonacci(int(n.decode())))
        serverSocket.sendto(nthTerm.encode(),clientAddress)

    elif(option == '9'):
        mode ,clientAddress=serverSocket.recvfrom(128)
        value ,clientAddress=serverSocket.recvfrom(128)
        data = str(converter(mode.decode(),float(value.decode())))
        serverSocket.sendto(data.encode(),clientAddress)

    elif(option == '10'):
        plainText,clientAddress=serverSocket.recvfrom(128)
        shift,clientAddress=serverSocket.recvfrom(128) 
        cipherText = caesarCipherEncrypt(plainText.decode(), int(shift.decode()))
        cipherText = "The encrypted version is : "+cipherText
        serverSocket.sendto(cipherText.encode(),clientAddress)

    elif(option == '11'):
        cipherText ,clientAddress=serverSocket.recvfrom(128)
        shift ,clientAddress=serverSocket.recvfrom(128)
        plainText = caesarCipherDecrypt(cipherText.decode(), int(shift.decode()))
        plainText = "The decrypted version is : "+plainText
        serverSocket.sendto(plainText.encode(),clientAddress)