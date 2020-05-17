import sys, os
import termios, fcntl
import select
from question import generateQuestion
import time
import playsound
import sys
import io
from contextlib import redirect_stdout
fd = sys.stdin.fileno()
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON
newattr[3] = newattr[3] & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldterm = termios.tcgetattr(fd)
oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
os.system('clear')
question,answer = generateQuestion()


    
inputString = ''
def getAnswer(answer):
    inputString = ''
    while select.select([sys.stdin], [], [], 0.10) == ([sys.stdin], [], []):
        sys.stdin.read()
    inputString = ''
    while len(inputString)<len(answer):
        inp, outp, err = select.select([sys.stdin], [], [])
        c = sys.stdin.read()
        sys.stdout.write(c)
        sys.stdout.flush()
        inputString = inputString + c
    print('')
    return inputString


while True:
    print(question)
    userAnswer = getAnswer(answer)
    if userAnswer==answer:
        print("ok")
        question,answer = generateQuestion()
        time.sleep(1)
        sys.stdout.flush()
        c = ''
        inputString = ''
        os.system('clear')
    else:
        print("bad : %s" % (answer))
        time.sleep(1)
        sys.stdout.flush()
        c = ''
        inputString = ''
        os.system('clear')

# Reset the terminal:
termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)