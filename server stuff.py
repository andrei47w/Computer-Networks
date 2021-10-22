import socket
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
HOST = '193.231.20.3'
PORT = 1277

WIN = 0
while True:
    past_tries = []
    if WIN:
        exit(0)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        n = s.recv(4)
        print(int.from_bytes(n, 'big'))

        i = 0
        poss = 0
        word = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        while i < int.from_bytes(n, 'big'):
            poss = random.randrange(26)
            while poss in past_tries:
                poss = random.randrange(26)
            past_tries.append(poss)
            letter = letters[poss]
            s.send(letter.encode())
            response = s.recv(4)
            # print("response: ", int.from_bytes(response, 'big'), "from letter: ", letter)

            if int.from_bytes(response, 'big') == 0:
                pass
            elif int.from_bytes(response, 'big') == 1:
                i += 1
                frecv = int.from_bytes(s.recv(4), 'big')
                # print("frecv: ", frecv)
                for i in range(frecv):
                    poz = int.from_bytes(s.recv(4), 'big')
                    word[poz] = letter
            elif int.from_bytes(response, 'big') == 2:
                word.append(letters)
                print("word was: ", ''.join(map(str, word)))
                s.close()
                break
            else:
                print(''.join(map(str, word)))
                print("game over")
                s.close()
                break
