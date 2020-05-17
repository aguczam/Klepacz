import random

def generateQuestion():
    questionList = []
    questionList.append(["Open a file file.txt in your existing Vim session",":e file.txt"])
    questionList.append(["Insert the file file.txt below the cursor in current buffer",":r file.txt"])
    questionList.append(["Insert the file file.txt before the first line",":0r file.txt"])
    questionList.append(["Insert result of linux command <command> below the cursor",":r !<command>"])
    questionList.append(["Open file that is under or after the cursor","gf"])
    questionList.append(["Open html link that is under or after the cursor in your deflaut browser","gx"])
    questionList.append(["Save currently opened file and exit vim",":wq"]) 
    questionList.append(["Exit vim but write only when changes have been made ",":x"]) 
    questionList.append(["Equivalent to :x","ZZ"])
    questionList.append(["Exit vim without saving currently opened file",":q!"]) 
    questionList.append(["Exit all open files in current vim session",":qa"])
    questionList.append(["Save currently opened file",":w"])
    questionList.append(["Save currently opened file as file.txt",":w file.txt"])
    questionList.append(["Save currently opened file as file.txt with overwrite option",":w! file.txt"])
    questionList.append(["Save current buffer as a new file.txt",":sav file.txt"])
    questionList.append(["Like :w for file.txt but only when the buffer has been modified",":up file.txt"])
    questionList.append(["Moves the cursor one character to the left","h"])
    questionList.append(["Moves the cursor down one line","j"])
    questionList.append(["Moves the cursor up one line","k"])
    questionList.append(["Moves the cursor one character to the right","l"])  
    questionList.append(["go to the start of the next word","w"])   
    questionList.append(["go to the start of the next Word","W"])  
    questionList.append(["go to the end of the current word","e"])  
    questionList.append(["go to the end of the current Word","E"]) 
    questionList.append(["go to the previus word","b"]) 
    questionList.append(["go to the previus Word","B"]) 
    randomNumber = random.randrange(0,len(questionList))
    question = questionList[randomNumber][0]
    answer = questionList[randomNumber][1]
    return question,answer

                                

                  