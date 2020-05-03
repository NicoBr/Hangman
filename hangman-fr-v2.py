# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:58:56 2020

@author: nico
"""
import sys
import os
def getword():
    """
    This function reads the vocabulary-file and gives back the word and
    his traduction
    """
    import csv
    import random
    vocGer=[]
    vocFre=[]
    lines=0
    x=0
    with open ("vocU8.csv", mode = "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            vocFre.append(row[0])
            vocGer.append(row[1])
            lines += 1
    #print(vocFre)
    #print(vocGer)
    #print(lines)
    x = random.randint(1,lines-1)
    #print(x)
    #print("Selected:")
    #print(vocFre[x], vocGer[x])
    return [vocFre[x], vocGer[x]]
    
def createStartString(s):
    """
    create the start-string with the lines
    as it is for french the spaces and hyphens (Bindestrich)
    """
    t = ""
    for l in s:
        if l==" ":
            t = t+" "
        elif l=="-": 
            t = t+"-"
        else:
            t = t+"_"
    #print(t)
    return(t)

def HangmanOutput():
    os.system('cls')
    print('\33[31m')
    print (" H A N G M A N")
    print ("- - - - - - - - -\x1b[0m")
    print ("\nDu hast: ",str(points)," Punkte")
    print("Was heisst -",vocToGuess[1],"- auf französisch?")
    if lives > 0:
        print (hangmanPics[6-lives])
        print("Leben: ",str(lives))
        s = " ".join(guessedLetters)
        print("schon versucht:",s)
        s = " ".join(wordToGuess)
        print("zu finden: ",s)
    else:
        print (hangmanPics[6-lives])
        print("Leben: ",str(lives))
        s = " ".join(guessedLetters)
        print ("G A M E - O V E R")
        # To Do ENDE
        sys.exit()
    
"""
Main program
"""

# Definition of variables

hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
vocToGuess=getword()
lives=6
guessed = False
guessedLetters = {""}
points=0


#print(vocToGuess)
print("Was heisst -",vocToGuess[1],"- auf französisch?")

wordToGuess=createStartString(vocToGuess[0])
wordToGuess=list(wordToGuess)
#print(wordToGuess)
# HangmanOutput()

while guessed != True:
    HangmanOutput()
    # Asking for a letter:
    guessLetter = input("wähle einen Buchstaben: ")[0]
    guessLetter = guessLetter.lower()
    
    guessedLetters.add(guessLetter) 
    
    checkLetter = False
    i=0
    print (vocToGuess[0])
    for l in vocToGuess[0]:
        if l == guessLetter:
            #print (l, guessLetter)
            checkLetter = True
            #print("Richtig!")
            
    if checkLetter==True:
        for i in range (len(vocToGuess[0])):
            print(len(vocToGuess[0]))
            if vocToGuess[0][i]==guessLetter:
                print("--->",vocToGuess,guessLetter,wordToGuess)
                wordToGuess[i]=guessLetter
                print(wordToGuess)
    if checkLetter == False:
        print("Na das war nicht so gut...")
        lives -= 1
        print("Du hast nur noch ",str(lives), " Leben")
        
    if "_" in str(wordToGuess):
        guessed = False
        print ("Du hast das Wort ", vocToGuess[0]," nicht erraten.")
    else:
        guessed = True
        print("Super! Du hast es geschafft!")
        print("Du hast noch ",str(lives), " Leben")
        # the game continues
        vocToGuess=getword()
        lives=6
        guessed = False
        guessedLetters = {""}
        print("Was heisst -",vocToGuess[1],"- auf französisch?")
        wordToGuess=createStartString(vocToGuess[0])
        wordToGuess=list(wordToGuess)
        guessed = False
        points += 1
    # Ende
    

