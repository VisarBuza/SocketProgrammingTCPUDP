import socket
import time

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12000
    clientSocket.connect(('localhost', port))
except socket.error as msg:
    print("Socket creation error: "+str(msg))

print(clientSocket.recv(128).decode())
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

    option = input("\nChoose one of the options :")
    clientSocket.send(str.encode(option))

    if(option == '1'):
        answer = clientSocket.recv(128).decode()
        print(answer)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '2'):
        answer = clientSocket.recv(128).decode()
        print(answer)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '3'):
        word = input("Enter a sentence :")
        clientSocket.send(str.encode(word))
        numberOfConsonants = clientSocket.recv(128).decode()
        print("Number of consonants in the word is :"+numberOfConsonants)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '4'):
        word = input("Enter a sentence : ")
        clientSocket.send(str.encode(word))
        newWord = clientSocket.recv(128).decode()
        print("The new sentence is : "+newWord)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '5'):
        answer = clientSocket.recv(128)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '6'):
        answer = clientSocket.recv(128)
        print(answer.decode())
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '7'):
        answer = clientSocket.recv(128).decode()
        print(answer)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '8'):
        n = input("Enter a number : ")
        clientSocket.send(str.encode(n))
        nthTerm = clientSocket.recv(128).decode()
        print(nthTerm)
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
        clientSocket.send(str.encode(option))
        clientSocket.send(str.encode(value))
        finalAnswer = (clientSocket.recv(128)).decode()
        print(finalAnswer)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '10'):
        plainText = input("Enter the plain text you want to encrypt : ")
        shift = input("Enter the number of shifts : ")
        clientSocket.send(str.encode(plainText))
        clientSocket.send(str.encode(shift))
        cipherText = clientSocket.recv(128).decode()
        print(cipherText)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break

    elif(option == '11'):
        cipherText = input("Enter the plain text you want to decrypt : ")
        shift = input("Enter the number of shifts : ")
        clientSocket.send(str.encode(cipherText))
        clientSocket.send(str.encode(shift))
        plainText = clientSocket.recv(128).decode()
        print(plainText)
        breakPoint = input("Press 1 if you want to quit :")
        if breakPoint == '1':
            break
    else:
        print("Invalid expression")

clientSocket.close()
