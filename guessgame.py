#imports
                      
#title screen

print("██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗")
print("██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝")
print("██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ")
print("██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ")
print("╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗")
print(" ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝")
print("                                                              ")

#Rules/Procedure to be followed
print()
print()
print("**Following are the rules and procedure of how to play this game :- **")
print()
print("~ You need 2 single / 2 differnt groups of people , eg:- A and B . But dont get confused , you guys are not going to fight each other in the game , what you are going to fight are the restrictions made by the gamemaster to keep you from guessing the word .")
print()
print("~ In guess game basically one person/group of people decide on a word to input in the code , and the second person/ group of people would have to guess the word . Now , if you can or can not guess the required words depends on how smart you are (which belive me you arent smarter than the game master , you aint smarter than nobody and u know dat shit so just bet on your chemistry now.) or how good of a chemistry you have.")
print()
print("~ Now , for them to guess the word the group one can leave 3 sentences worth of clues , the word to be guessed should be a singular word , you can chose a multi word string to be guessed too if you want but guessing those might be difficult with just 3 sentences , so stick to singular words/things or common short phrases which can be heard around . Also , dont make the guessing word as easy as like amovie you watched 2 hours ago , because then the game would be too easy to beat with even a dumb clue , rather think about challanging yourselves , if you want to play and win a game that easy you can go and play cod for god sakes .")
print()
print("~ To reduce the confusion between each other only type in lowercase and choose words you both know the correct spellings to , the program is casesensitive and cannot detect and correct your dumb spelling mistakes , so beware . Also do not leave in idle spaces at random places .")
print()
print("~ Now , if the guesser guesses the word correctly decided by the word selector you win ! , but if not , the game master wins .")
print()
print("~ Well , ive told you about how to chose the words to be guess but now we are going to talk about the clues you can give , the code will ask you for 3 clues , in each clue you can give 1 sentence worth of ambiguous stuff thatll helo the guesser guess , dont be too obvious , again if you want to win an easy game go play cod , try and make it both ambigous and fun at the same time !")
print()
print("~ Dont be restriceted to what the code asks you to do , you can chose and decide on chosing a words of a certain theme , like from a certain show or a game you both play , you can reduce the number of clues you want to have to make the game harder , it all depends on you , this is inherently a word guessing sandbox for you to enhance to your choice !")
print()
print("~ Now , the mechanics of the game , at when the game starts the guesser decided should not be looking at the screen , the other person will be asked to write in all the clues and the decided word , after that they will be asked if they have entered all the things they needed to , when they answer that the guesser can come back and take the spot , now look at your clock and the guesser has 1 minute (u can lower this for more dificulty if you want to) of time to guess the word , if they cant , boom , uve lost ! , move on the the next word with sides switched .")
print()
print("~ To end the game once the timer runs out the guesser must choose n on the /want to guess again screen/ .")
print()
print("~ If you actually want to have fun , please dont cheat , well even if you do yerr just wasting your own time so who cares , do whatever brings you joy !")
print()
print()

#Starting the game
start1 = input("The game will start once you type and enter anything ! So ask the guesser to be not looking at the screen going forward until asked : ")
print()
print()

#Inputs from the word decider
Word = input("Enter the word to be guessed :")
Clue1 = input("Enter the first clue : ")
Clue2 = input("Enter the second clue : ")
Clue3 = input("Enter the third and last clue : ")

#Transistion
print("⠀⠀⠀⠀⠀   ⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠛⠿⠿⣿⣿⣷⣄⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⠀⠀")
print("⠀⠀⢀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀")
print("⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⡿⠀")
print("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀")
print("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀")
print("⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
print("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
print("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀")
print("⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀")
print("⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀")
print("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀")
print("⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀")
print("⠀⠀⠀⠙⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⣟⣯⣿⠟⡉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣽⣿⣿⣿⠿⠿⠟⠒⠉⠉⠉⠉⠉⠉⠉⠙⠋⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠋⠉⢀⣠⣤⣤⡔⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠾⠛⠋⠉⠀⢀⣀⠐⣤⣶⣶⡤⢤⣤⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣰⣶⣾⣿⣿⣿⣆⠀⣀⣀⡀⣀⡀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⢀⢀⣀⠀⣀⣈⡿⠿⠿⠽⠃⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠿⠿⠿⠿⠾⠟⢁⣀⡴⣦⠆⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣤⣀⣀⠀⠀⠀⠀⢘⣿⣍⡷⠆⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣄⠈⠉⠛⠛⠿⠓⠀⠉⠋⠉⣀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡀⠙⠻⢶⣶⡤⠀⠀⠛⠶⠾⠼⠋⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠈⠻⣶⣤⡀⠀⠀⢸⠿⣶⣦⣤⣠⣾⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠙⢷⣤⣀⠈⠁⠀⠀⢠⣤⣀⠈⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⢧⣀⠉⠛⠃⠀⠀⠀⠀⠉⠛⠿⠿⠻⠃⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢳⣄⠙⠛⢋⠁⠀⠀⠀⠘⠿⣴⣤⣄⣤⡄⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⡙⠛⠋⠀⠀⠀⠀⠀⠰⣤⣀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⡈⠉⠉⠀⠀⠀⠀⠀⠀⢀⡈⠙⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡉⠛⡁⠀⠀⠀⠀⠀⠀⠈⠻⠷⣶⣦⡆⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢠⡈⢷⣌⠙⠛⠁⠀⠀⠀⠀⠀⠀⠰⣦⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⡉⠛⠛⠀⠀⠀⠀⠀⠀⠀⢀⠈⠙⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢦⣀⠉⠛⠷⠖⠀⠀⠀⠀⠀⠀⠀⠘⠿⣶⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⣠⣀⠙⠳⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣶⣤⣤⠀⠀⠀⠀⠀⠀⠀⢠⠛⠛⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠰⣦⣄⠈⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀⠺⠿⠿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠟⠁⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣀⣀⣀⣀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣞⣻⣿⣿⣔⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠉⠉⠁⠀⠀⠀⠀")
print()
print()
print()

print("------------------------------------------------------------------------------------------------------------------------------------")
print("Word Deciders job is done.")
print("Guesser should now be the one playing.")
print("------------------------------------------------------------------------------------------------------------------------------------")
start2 = input("Guessers time limit must start after you type and enter anything , so get your stopwatch ready.")
print()
print()

#Predefined Variables
Guess = ""
x=0
z=0
i=0
m=0

#Telling the clues
print("The first clue is :- ", Clue1)
print("The second clue is :- ", Clue2)
print("The last clue is :- ", Clue3)
print()


#Main Code Body
while (x<1):
     Guess = input("Guess the word based on the clues !: ")
     if(Word == Guess):
         x += 1
         print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗")
         print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║")
         print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║")
         print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝")
         print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗")
         print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝")
         print()
     else:
         print("You guessed wrong !")
         m=0
         while(m<1):
             print("You want to continue guessing ? Ans as (y/n or Y/N) :- ")
             z = input("")
             i=0
             while(i<1):
                 if(z=="y" or z=="Y"):
                     i+=1
                     m+=1
                 elif(z=="n" or z=="N"):
                     print()
                     print()
                     print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗    ██╗")
                     print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝    ██║")
                     print(" ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗      ██║")
                     print("  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝      ╚═╝")
                     print("   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗    ██╗")
                     print("   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝")
                     print()
                     
                     i+=1
                     x+=1
                     m+=1
                 else:
                     m=0
                     i+=1
                     print("You didnt give a valid answer you troglodyte , one thing was asked of you and you failed , epic ! Give the right answer this time . That moment when you dont know how to click a single alphabet lmao .")

#Ending screen 
print()
print()
print("_________________________________________________________________________________________________________________________________")
print()
print("████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗")
print("╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║")
print("   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║")
print("   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║")
print("   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝")
print("   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ")
print()
print("_________________________________________________________________________________________________________________________________")
print()
print()
print("⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌")
print("⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌")
print("⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌")
print("⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪")
print("⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡")
print("⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐")
print("⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔")
print("⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘")
print("⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎")
print("⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗")
print("⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷")
print("⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟")
print("⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰")
print("⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊")
print("⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌")
print("⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁")
print("⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀")
print("⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀")
print("⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟")
print("⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾")
print("⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽")
print()
strax = input("Enter anything to exit the terminal dogma moi forendo : ")