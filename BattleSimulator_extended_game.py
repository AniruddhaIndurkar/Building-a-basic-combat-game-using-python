'''
Student ID- 29389429
Version: Extended game  
Name: Aniruddha Indurkar
Tasks implemented: Medics and Expanded armies
Since we are given a task to implement a game, we make use of user defined function. The user defined functions are used
primarily because they are useful in breaking a
task into smaller tasks and can be called to perform the necessary operation.
Code below consists of user defined functions, while loops, for loops and pre-defined python functions.
we make use of lists to store the armies.

Assumptions:
1. Only S,W,E,A,K will be taken separated by spaces.Any other input not separated by spaces will be termed as invalid.
2. You can make multiple inputs and the order will be important. If you input more than the allocated budget you will be
 asked to adjust the units.
3. All the units are of 1$ except for wizard which costs 2$. Since we implemented medics and expanded armies, wizard has
 advantage
4. If a unit dies in a dual and you have budget remaining then the medics will come into play and append the lost unit
at the back of the army.
5. Resurrecting a wizard requires 1 $ for medics pack. All units require 1$ which is consistent with 1$/1 medic per
 death
6. Once you start the game you cannot exit. If you decide not to chose the army it is fine but once you begin the game
you cannot exit.
'''
'''
We divide the game into 4 basic tasks with the help of user defined functions:
1. Take input from user(I decided to go with multiple input to make it faster). Minor function to check the input and 
append to new list.
2. Function that takes in 2 units from armies and returns the result of the dual
3. Function that loops through the armies and passes the units to the function in point 3 and acts on this result
4. Integrate all these functions in a function to play the game

For extended game , we make use of expanded armies and medics. 

Since ,the prices are readjusted, I used the below formula to calculate the budget:
budget= 10 - (length of the list + count of wizards)
Here, the wizard has 2 $ price , thus we are substracting additional 1$ for the number of wizards in the army. 

However, for medics we are making use of the remaining budget only and 1$ is deducted for appending every unit in army.
Additional feature: In the case of inputting, if the user exceeds the budget , I prompted the user to readjust the 
armies in order to stay within the budget by popping the units out of list. (**clarified with the tutor)
'''

#Input checker that checks if the entered units are valid or not
#Takes in the list from the user and returns whether true or false
#Helps us to decide whether to append or not

def input_checker(list):

    g=0

    for i in list:

        if not(i=="S" or i=="K" or i=="A" or i=="E" or i=="W"):

            g=g+1
    if g>0:
        #if any of the input is invalid this will become true
        return True

    else:

        return False

#Take the input from the user
#function returns a list of army based on the user selection

def combat_input():

    budget = 10
    break_out = True # this was used because the empty user lists didn't allow to breakout of first loop
    input_loop = True # for invalid inputs and continuing to buy units
    usr = []
    #initiating variables to loop through

    # we loop this until the budget is there
    while budget > 0 :

        while input_loop == True:

            #convert to upper case to generalise
            input_usr = input("Enter units you want to buy\nUse the initials for the units\
            \n\nSoldier=S,Knight=K,Archer=A, Siege equipment=E, Wizard=W.\
            \n\nSeparate the units you want to enter by spaces.\
            \n\nYou have {} $ left:".format(budget)).upper()

            #Split the input on the basis of spaces in order to take multiple inputs at the same time
            '''
            Below line of code (line 93) is referred from the below link:
            https://stackoverflow.com/questions/4162815/how-to-read-two-inputs-separated-by-space-in-a-single-line
            This is cited as reference in the documentation manual
            '''
            input_usr = input_usr.split()

            #Calls the function to check the input is one of the unit.
            input_loop = input_checker(input_usr)
            #Output of this helps us to break out of the loop
            #if input is invalid print invalid and since input_loop is zero it will still ask for input after checking \
            # budget

            if input_loop==True:

                print("The input is not valid!Please input carefully!\n\n")

        #this loop appends the input in separate list and takes in only first 10 values so that the consistency is \
        # maintained
        for unit in input_usr[:10]:

            if unit == "S" or unit == "K" or unit == "A" or unit=="W" or unit=="E":

                usr.append(unit)
                budget = 10 - len(usr)-usr.count('W')  # dynamically display the budget, adjusted for wizard price 2$

        #Now for the tricky part we ask the user to adjust the units if the budget is more than the given one.
        #We take the index from the user and this runs until the budget is less than 0
        while budget < 0:

            print("You have used more than allocated budget\n")
            print("You have exceeded the budget please remove the units\n")
            print("User selections: ",usr, '\n')
            '''
                Use of try and except in Below line of code(126-138) is referred from the below mentioned site:
                https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
                This is cited as reference in the manual
            '''
            i = None

            while i == None:

                try:
                    print("Enter the index number of the unit you want to remove")
                    i = int(input("Please enter the index of the unit starting from 1 on left to 10 :")) - 1
                    #I have substracted 1 to make the index user friendly
                    usr.pop(i)
                    budget = 10 - len(usr) - usr.count('W')

                except:
                    print("Please enter a valid input\n")


        if budget > 0:

            decsn = ''

            #This is done only to check the budget and prompt the users whether to buy a unit or not
            while decsn == '':

                    decsn = input("You have {} $ left . Do you want to buy units? Enter y/n :".format(budget)).upper()

                    if decsn == 'Y':

                        print("Continue to buy units\n")
                        input_loop = True #Since the user wants to buy the units we want to go back to the input loop.

                    elif decsn == 'N':

                        print("Your battle units are ready to fight!\n")

                        #In case when the input is no unit and the user doesn't want to choose the input
                        break_out=False

                    else:

                        print("Unrecognised input. Please enter again\n")
                        #when input is unrecognised then reset the variable decsn
                        decsn = ''


        if break_out==False:

            break

    print("\nUser selections : ", input_usr, "\n")

    return usr


# Function to check the outcome of one battle/dual
#The function takes in 2 units and gives the outcome of the dual
#1 for tie, 0 for i wins and 2 for j wins
#Implementing the additional task of Siege equipment
def battle_check(i, j):
    # In case of a tie both lose

    if i == j:

        return 1
    # Condition to check the battle
    # these conditions were modified from the basic game, otherwise there would be too many if-else statements
    elif (i == 'S' and (j != 'W' and j != 'E' and j != 'A')):

        return 0

    elif (i == 'K' and (j != 'W' and j != 'S')):

        return 0

    elif (i == 'A' and (j != 'K' and j != 'E')):

        return 0

    elif (i == 'W' and (j != 'A')):

        return 0

    elif (i == 'E' and (j != 'K' and j != 'W')):

        return 0

    else:

        return 2

# Battle continued as a loop between 2 armies
#This function takes in lists of both the users and loops in using while loop.
#Each of the unit is passed on to the Battle_check function to check the result of the individual dual and act \
# accordingly.

def combat_battle(usr1, usr2):

    i = 0
    j = 0
    winner=''
    GameRound=1

    #This addition is to take into account 1$ per death of the medic
    budget1=10-len(usr1)-usr1.count('W')
    budget2=10-len(usr2)-usr2.count('W')
    #These variables are taken to loop through the armies of each player separately and get a result
    #While loop is used because it gives me more control over the iterations
    while (i < len(usr1) and j < len(usr2)):

        # break out of the loop if the iteration for any one of the loop is more than given length
        print("=====================================================")
        print('Battle Round {}'.format(GameRound))
        print("=====================================================")

        GameRound=GameRound+1

        # Battle when it is a tie
        if battle_check(usr1[i], usr2[j]) == 1:

            print("It is a tie in the dual\n")

            print("We move on to the next units\n")

            #below lines perform the task of appending the units at the back of army by checking the budget(medics task)
            #below condition takes care of exception of not appending a wizard when budget is 1$
            if budget1>0:

                    usr1.append(usr1[i])
                    print("{} is resurrected at the back of the army for User 1\n".format(usr1[i]))
                    budget1=budget1-1

            if budget2>0:

                    usr2.append(usr2[j])
                    print("{} is resurrected at the back of the army for User 2\n".format(usr2[j]))
                    budget2=budget2-1

            i = i + 1
            j = j + 1

        # Battle when User 1 wins the dual
        elif battle_check(usr1[i], usr2[j]) == 0:

            print("User 1 wins over User 2 in this the dual")

            print("{} defeats the {}\n".format(usr1[i], usr2[j]))
            #medics task
            if budget2 >0:

                    usr2.append(usr2[j])
                    print("{} is resurrected at the back of the army for User 2\n".format(usr2[j]))
                    budget2=budget2-1
            j = j + 1

        # Battle when User 2 wins the dual
        elif battle_check(usr1[i], usr2[j]) == 2:

            #medics task
            if budget1>0:

                    usr1.append(usr1[i])
                    print("{} is resurrected at the back of the army for User 1\n".format(usr1[i]))
                    budget1=budget1-1

            print("User 2 wins over User 1 in this the dual")

            print("{} defeats the {}\n".format(usr2[j], usr1[i]))

            i = i + 1

        # Final result of the battle of armies
        if (i >= len(usr1)) and (j >= len(usr2)):

            print("It's a tie")
            winner = "It's a tie"

        if i > len(usr1) - 1 and j<=len(usr2)-1:

            print("User 1 lost")
            winner = "User 2"

        if j > len(usr2) - 1 and i<=len(usr1)-1:

            print("User 2 lost")
            winner = "User 1"

    #Handling the cases where one of the armies is empty
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
        #User 1 army is selected and stored in variable
        usr1 = combat_input()

        print("\n\nUser 2 please select your army\n")
        #User 2 army is selected and stored in second variable
        usr2 = combat_input()

        print("\nYour units have waged a war!")

        print("\nBattle of the demigods is going on!\nBattle update:")

        print("........")

        winner = combat_battle(usr1, usr2)

        print("=====================================================")
        print("Winner is :{} \n".format(winner))
        print("=====================================================")


#Function to begin the game with a few instructions

def game_start():

    Game_On=''

    #Print the instructions for the users
    print('\nWelcome to the combat game!\n')
    print("\nGAME RULES")
    print("==============================================================================================")

    print('We have 5 units, Soldier(S), Knight(K),Archer(A),Siege Equipment(E),Wizard(W)')
    print('Soldier defeats the Knight. Knight defeats the Archer. Archer defeats Soldier')
    print('Wizard can only be defeated by an archer.')
    print('Siege equipment can be defeated by wizards and knights while they win against the rest.')
    print('Each player gets to choose an army. Select the army and fight against each other.')
    print('Each unit costs 1 $ except the Wizard which costs 2 $ and each player is given a budget of 10$.\n')
    print('Enter the initials of the unit separated by spaces if you want to make multiple inputs')
    print('For example: S W A K E ')
    print("Thus, the above selection implies :['Soldier','Wizard','Archer','Knight','Siege Equipment']")
    print('The unused money will be used for Medics and units lost will be resurrected in the last.')
    print('Wizards require 1 $ for resurrection.')
    print('All units require 1$ for resurrection irrespective of their buying price')
    print('User having the last unit standing will win')
    print("==============================================================================================")

    while Game_On!='Y' and Game_On!='Yes' and Game_On!='N' and Game_On!='No':

        Game_On = input("\nDo you want to play the game? (Enter y/n):").upper()

        if Game_On == 'Y' or Game_On == 'YES':

            print("\nAlright let's begin!\n")
            print("=====================================================")

            Game_play()

        elif Game_On == 'N' or Game_On == 'NO':

            print('\nScared mate? Go home!')

        else:

            print('Invalid input. Please enter again\n')
            Game_On=''
    print("=====================================================")

#Start the game from here
game_start()
