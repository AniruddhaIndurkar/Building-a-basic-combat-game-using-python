'''

Version: Basic game
Name: Aniruddha Indurkar
Python version: Python 3.6
Since we are given a task to implement a game, we make use of user defined function. The user defined functions are used
primarily because they are useful in breaking a task into smaller tasks and can be called to perform the necessary
operation.
Code below consists of user defined functions, while loops, for loops and pre-defined python functions.
we make use of lists to store the armies.

Assumptions:
1. Only S,A,K will be taken separated by spaces.Any other input not separated by spaces will be termed as invalid.
2. You can make multiple inputs and the order will be important. If you input more than 10 inputs only the first 10 will
 be considered.
3. All the units are of 1$ no matter what
4. Once you start the game you cannot exit. If you decide not to chose the army it is fine but once you begin the game
 you cannot exit.
'''
'''
We divide the game into 4 basic tasks with the help of user defined functions and integrate in a single function:
1. Take input from user(I decided to go with multiple inputs to make it fast. User has a choice to either input single
or multiple units). Minor function to check the input .
2. Function that takes in 2 units from armies and returns the result of the dual
3. Function that loops through the armies and passes the units to the function in point 3 and acts on this result
4. Integrate all these functions in a single function to play the game
'''

#Input checker to check input from user
#takes input as list and returns whether true or false
#Helps us decide whether to append or not to the actual army of the user.
def input_checker(list):
    #intitiate a variable to count for invalid entries
    g=0

    for i in list:
        #even if one entry is invalid return true
        if not(i=="S" or i=="K" or i=="A"):

            g=g+1

    if g>0:

        return True

    else:

        return False

#Take the input from the user
#returns a list
def combat_input():

    budget = 10
    break_out = True # this was used because the empty user lists didn't allow to breakout of first loop
    input_loop = True # for invalid inputs and continuing to buy units
    usr = []
    #initiating variables

    # we loop this until the budget is there and the inputs are valid
    while budget > 0 and budget<=10:

        while input_loop == True:

            input_usr = input("Enter units you want to buy\nUse the initials for the units\
                       \n\nSoldier=S,Knight=K,Archer=A\
                       \n\nSeparate the units you want to enter by spaces.\
                       \n\nYou have {} $ left:".format(budget)).upper()

            #Split the input on the basis of spaces in order to take multiple inputs at the same time
            '''
                Below line of code (line 76) is referred from the below link:
                https://stackoverflow.com/questions/4162815/how-to-read-two-inputs-separated-by-space-in-a-single-line
                This is cited as reference in the documentation manual
            '''
            input_usr = input_usr.split()

            #Calls the function to check the input whether valid or not.
            #limitation is that every input entry should be correct
            input_loop = input_checker(input_usr)

            #if input is invalid print invalid and since input_loop is zero it will still ask for input again
            if input_loop==True:

                print("The input is not valid please input carefully")

        print("\n",input_usr,"\n")

        #this loop appends the input in separate list and takes in only first 10 values so that the consistency is \
        # maintained
        for unit in input_usr[:10]:

            if unit == "S" or unit == "K" or unit == "A":

                usr.append(unit)
                budget = 10 - len(usr)  # dynamically calculate the budget

        #This condition is used to prompt the user for input if budget is there.
        if budget > 0:

            decsn = ''

            #This is done to check the budget and prompt the users whether to buy a unit or not(until valid entry)
            while decsn == '':

                    decsn = input("You have {} $ left . Do you want to buy units? Enter y/n ".format(budget)).upper()

                    if decsn == 'Y':

                        print("Continue to buy units")
                        input_loop = True # continuing to buy requires to go back to purchasing h

                    elif decsn == 'N':

                        print("Your battle units are ready to fight!")

                        #In case when the input is no unit and the user doesn't want to choose the input
                        break_out=False
                    else:

                        print("Unrecognised input. Please enter again")
                        #when input is unrecognised then reset the variable decsn
                        decsn = ''


        if break_out==False:

            break # we want to breakout of the input only if valid inputs are given or user wants to exit without army

    print("\nUser selections : ", input_usr, "\n")

    return usr


#To check the result of the dual
#Takes in the unit and returns result in the form of number 1=tie, 2=j wins ,0=i wins
#for understanding I kept the variable on the left reserved for user 1, thus 'i' for user 1.
def battle_check(i, j):

    # In case of a tie both lose
    if i == j:

        return 1
    # Condition to check the battle
    elif (i == 'S' and j == 'K') or (i == 'K' and j == 'A') or (i == 'A' and j == 'S'):

        return 0

    else:

        return 2

#Below function takes in armies of two users and returns a string of who the winner is!
#initialise 2 variables to iterate through the loop
#the function takes in input from the two users and passes the units to battle check function to check the result
# after getting the result of the dual the function acts accordingly
def combat_battle(usr1, usr2):
    i = 0   #User 1
    j = 0   #User 2
    winner=''
    GameRound=1
    #These variables are taken to loop through the armies of each player separately and get a result

    #I made use of while loops instead of 'for' because it gives me greater control on iteration
    while (i < len(usr1) and j < len(usr2)):

        print("=====================================================")
        print('Battle Round {}'.format(GameRound))
        print("=====================================================")
        GameRound=GameRound+1 # variable taken to display the round and increments with the loop

        # Battle when it is a tie, increment both the units, i.e. 'i' and 'j'
        if battle_check(usr1[i], usr2[j]) == 1:

            print("It is a tie in the dual\n")

            print("We move on to the next units\n")

            i = i + 1
            j = j + 1

        # Battle when User 1 wins the dual, we move to next unit of user 2 i.e. increment j
        elif battle_check(usr1[i], usr2[j]) == 0:

            print("User 1 wins over User 2 in this the dual")

            print("{} defeats the {}\n".format(usr1[i], usr2[j]))

            j = j + 1

        # Battle when User 2 wins the dual, increment for user 1 i.e. increment i
        elif battle_check(usr1[i], usr2[j]) == 2:

            print("User 2 wins over User 1 in this the dual")

            print("{} defeats the {}\n".format(usr2[j], usr1[i]))

            i = i + 1

        # Final result of the battle of armies
        if (i >= len(usr1)) and (j >= len(usr2)):

            print("It's a tie")
            winner = "It's a tie and no one "

        if i > len(usr1) - 1 and j<=len(usr2) - 1:

            print("User 1 lost")
            winner = "User 2"

        if j > len(usr2) - 1 and i<=len(usr1) - 1:

            print("User 2 lost")
            winner = "User 1"

    #Handling the cases where one of the armies is empty or both
    if usr1==[] and usr2==[]:

        print("=====================================================")
        print("You both lose! You guys are too scared to fight.\n")
        winner='No one'
        print("=====================================================")


    elif usr1==[] and usr2!=[]:

        print("=====================================================")
        winner="User 2"
        print("User 1 was defeated as he did not select the units\n")
        print("=====================================================")


    elif usr2==[] and usr1!=[]:

        print("=====================================================")
        winner="User 1"
        print("User 2 was defeated as he did not select the units\n")
        print("=====================================================")

    return winner


#The functions integrated into a structure for a Gameplay!

def Game_play():

        print("User 1 goes first!\n\n")

        #take input for user 1
        usr1 = combat_input()


        print("\n\nUser 2 please select your army\n")

        #take input from user 2
        usr2 = combat_input()

        print("\nYour units have waged a war!")

        print("\nBattle of the demigods is going on!\n Battle updates:")

        print("........")

        winner = combat_battle(usr1, usr2)
        print("=====================================================")
        print("{} won the battle!".format(winner))
        print("=====================================================")



#Function to begin the game with a few instructions

def game_start():

    Game_On=''

    #Print the instructions for the users
    print('\nWelcome to the combat game!\n')
    print("\nGAME RULES")
    print("==============================================================================================")

    print('We have 3 units, Soldier(S), Knight(K),Archer(A)')
    print('Soldier defeats the Knight. Knight defeats the Archer. Archer defeats Soldier')
    print('It is a two player game.')
    print('Each player gets to choose an army. Select the army and fight against each other.')
    print('Each unit costs 1 $ and each player is given a budget of 10$.\n')
    print('Enter the initials of the unit separated by spaces if you want to make multiple inputs')
    print('For example: S S A K A ')
    print("Thus, the above selection implies :['Soldier','Soldier','Archer','Knight','Archer']")
    print("The order is important as the units will fight in the same order")
    print('Invalid initials are not accepted and the user will have to input again.')
    print('User having the last unit standing will win')
    print("==============================================================================================")
    #loop only for the prompt to begin the game or not
    while Game_On!='Y' and Game_On!='Yes' and Game_On!='N' and Game_On!='No':

        Game_On = input("\nDo you want to play the game? (Enter y/n):").upper()

        if Game_On == 'Y' or Game_On == 'YES':

            print("\nAlright let's begin!\n")
            print("=====================================================")
            #we begin the game here
            Game_play()

        elif Game_On == 'N' or Game_On == 'NO':

            print('\nScared mate? Go home!')

        else:

            print('Invalid input. Please enter again\n')
            Game_On=''
    print("=====================================================")

#Start the game from here
game_start()



