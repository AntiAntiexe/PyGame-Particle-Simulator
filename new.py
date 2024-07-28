import numpy as np

'''def encryptionFunction():
    # Variables
    ciphertext = []
    ascii_values = []

    # Prompt to enter plaintext to be encrypted
    plaintext = input('Please enter text to be encrypted: ')

    # Each letter in the message is converted to ASCII and
    # appended to a list
    for character in plaintext:
        ascii_values.append(ord(character))

    # Each ASCII character is multiplied by 3
    for element in ascii_values:
        ciphertext.append(element * 3)

    # Ciphertext is returned
    return ciphertext


while True:
    print(encryptionFunction())

'''
''''
def decryptionFunction():
    ciphertext = input('Please enter ciphertext to be decrypted: ')
    ascii_values = []
    deciphertext = []


    for i in ciphertext:
        
    for i in ciphertext:
        deciphertext.append(i/3)
        print(deciphertext)


while True:
    print(decryptionFunction())





phi =
v_1x = v_1* numpy.cos(theta_1-)'''
rate = 60 # fps
dt = 1/rate # times step between frames
velocity1 = 150
gravity1 = 50


pos_1 = np.array([125, 125], dtype=float)

#pos_1[1] = np.add(pos_1[1], (gravity1 * dt))

#pos_1[1] = pos_1[1]*dt + gravity1

#pos_1[1] = float(pos_1[1]) + 50 * (1/rate)

'''pos_1[1] = float(pos_1[1])

x = pos_1[1] + 50 * (1/rate)'''

pos_1[1] = pos_1[1] + velocity1 * dt


#print(x)
print(pos_1[1])



