import socket
import threading
import _thread
from socket import gethostname
import time
import random
import math
import sys


serverName='localhost'
serverPort=12000
serverSocket=(serverName,serverPort)
try:
    clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as msg:
    print("Could not create socket "+str(msg))

print(' Operations:')
print('1.IP ADDRESSA E KLIENTIT')
print('2.PORTI NUMBER I KLIENTIT')
print('3.BASHKETINGELLORE')
print('4.PRINTO')
print('5.EMRI I KLIENTIT')
print('6.KOHA')
print('7.LOJA')
print('8.FIBONACCI ')
print('9.KONVERTO ')
print('10.Caesar Cipher Encrypt')
print('11.Caesar Cipher Decrypt')

while True:
    option=input("\nChoose one of the options :")
    clientSocket.sendto(option.encode(),serverSocket)
    
    if(option == '1'):
        answer, serverAddress = clientSocket.recvfrom(128)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break
             

    elif(option == '2'):
        answer, serverAddress = clientSocket.recvfrom(2048)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    
    elif(option == '3'):
        word = input("Enter a sentence :")
        clientSocket.sendto(word.encode(),serverSocket)
        answer, serverAddress = clientSocket.recvfrom(128)
        numberOfConsonants=str(answer.decode())
        print("Number of consonants in the word is :"+numberOfConsonants)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '4'):
        word = input("Enter a sentence : ")
        clientSocket.sendto(word.encode(),serverSocket)
        newWord ,serverAddress=clientSocket.recvfrom(128)
        print("The new sentence is : "+newWord.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '5'):
        answer,serverAddress=clientSocket.recvfrom(128)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '6'):
        answer,serverAddress=clientSocket.recvfrom(128)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '7'):
        answer,serverAddress=clientSocket.recvfrom(128)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '8'):
        n = input("Enter a number : ")
        clientSocket.sendto(n.encode(),serverSocket)
        nthTerm ,serverAddress=clientSocket.recvfrom(128)
        print(nthTerm.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '9'):
       
        data = "Send a conversion and the value you want to convert\n \
            \nKilowattToHorsePower\
            \nHorsepowerToKilowatt\
            \nDegreesToRadians\
            \nRadiansToDegrees\
            \nGallonsToLiters\
            \nLitersToGallons\n"
        print(data)    
        option = input("Enter the option you want :")
        value = input("Enter the value you want :")
        clientSocket.sendto(option.encode(),serverSocket)
        clientSocket.sendto(value.encode(),serverSocket)
        finalAnswer ,serverAddress= clientSocket.recvfrom(128);
        print(finalAnswer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '10'):
        plainText = input("Enter the plain text you want to encrypt : ")
        shift = input("Enter the number of shifts : ")
        clientSocket.sendto(str.encode(plainText),serverSocket)
        clientSocket.sendto(str.encode(shift),serverSocket)
        cipherText ,serverAddress=clientSocket.recvfrom(128);
        print(cipherText.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '11'):
        cipherText = input("Enter the plain text you want to decrypt : ")
        shift = input("Enter the number of shifts : ")
        clientSocket.sendto(str.encode(cipherText),serverSocket)
        clientSocket.sendto(str.encode(shift),serverSocket)
        plainText,serverAddress=clientSocket.recvfrom(128)
        print(plainText.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break
    else:
        print("Invalid expression")