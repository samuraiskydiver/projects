from time import *
import random


def rock():
    print("""









        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)












    """)


def paper():
    print("""










         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)









    """)


def scissors():
    print("""










        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)









    """)


def lizard():
    print("""










                  ___   
           )/_  ,@  /   
           |(_,' _@/    
           |    /       
      \)/ /    (_)/     
      ((_/   ,----~     
       \    (_)/        
       / ,-----~        
      (('  _,-.         
       \\=//    









    """)


def spock():
    print("""
         :                                 :
       :                                   :
       :  RRVIttIti+==iiii++iii++=;:,       :
       : IBMMMMWWWWMMMMMBXXVVYYIi=;:,        :
       : tBBMMMWWWMMMMMMBXXXVYIti;;;:,,      :
       t YXIXBMMWMMBMBBRXVIi+==;::;::::       ,
      ;t IVYt+=+iIIVMBYi=:,,,=i+=;:::::,      ;;
      YX=YVIt+=,,:=VWBt;::::=,,:::;;;:;:     ;;;
      VMiXRttItIVRBBWRi:.tXXVVYItiIi==;:   ;;;;
      =XIBWMMMBBBMRMBXi;,tXXRRXXXVYYt+;;: ;;;;;
       =iBWWMMBBMBBWBY;;;,YXRRRRXXVIi;;;:;,;;;=
        iXMMMMMWWBMWMY+;=+IXRRXXVYIi;:;;:,,;;=
        iBRBBMMMMYYXV+:,:;+XRXXVIt+;;:;++::;;;
        =MRRRBMMBBYtt;::::;+VXVIi=;;;:;=+;;;;=
         XBRBBBBBMMBRRVItttYYYYt=;;;;;;==:;=
          VRRRRRBRRRRXRVYYIttiti=::;:::=;=
           YRRRRXXVIIYIiitt+++ii=:;:::;==
           +XRRXIIIIYVVI;i+=;=tt=;::::;:;
            tRRXXVYti++==;;;=iYt;:::::,;;
             IXRRXVVVVYYItiitIIi=:::;,::;
              tVXRRRBBRXVYYYIti;::::,::::
               YVYVYYYYYItti+=:,,,,,:::::;
               YRVI+==;;;;;:,,,,,,,:::::::
    """)


def win():
    print("""
     __   __           __        __          _ 
     \ \ / ___  _   _  \ \      / ___  _ __ | |
      \ V / _ \| | | |  \ \ /\ / / _ \| '_ \| |
       | | (_) | |_| |   \ V  V | (_) | | | |_|
       |_|\___/ \__,_|    \_/\_/ \___/|_| |_(_)

        """)
    print("your wins:")
    print(user_wins)
    print("your opponent wins:")
    print(comp_wins)
    print("Thank you for playing")
    sleep(3)


def draw():
    print("""
      ____                     _ 
     |  _ \ _ __ __ ___      _| |
     | | | | '__/ _` \ \ /\ / | |
     | |_| | | | (_| |\ V  V /|_|
     |____/|_|  \__,_| \_/\_/ (_)

        """)


def gameover():
    print("""

       __ _  __ _ _ __ ___   ___  _____   _____ _ __ 
      / _` |/ _` | '_ ` _ \ / _ \/ _ \ \ / / _ | '__|
     | (_| | (_| | | | | | |  __| (_) \ V |  __| |   
      \__, |\__,_|_| |_| |_|\___|\___/ \_/ \___|_|   
      |___/                                                                              
        """)
    print("your wins:")
    print(user_wins)
    print("your opponent wins:")
    print(comp_wins)
    print("Thank you for playing")
    sleep(3)


def main():
    global user_wins
    global comp_wins
    comp_wins = user_wins = 0
    sleep(1)
    rock()
    sleep(1)
    paper()
    sleep(1)
    scissors()
    sleep(1)
    lizard()
    sleep(1)
    spock()
    sleep(1)

    print("""Welcome to The " Rock, Paper, Scissors, Lizard, Spock" Game!!!""")
    choice = input("""           SELECT A AND ENTER TO START              """)

    if choice == "a" or "A":
        menu()
    else:
        print("You must choose a valid option.")
        print("Please try again.")
        main()


def hiddengem():
    numpool2 = ["1", "2", "3"]
    op_throw = random.choice(numpool2)
    print("")
    print("")
    print("")
    p1_throw = input("""         welcome to plain old rock paper scissors...
                        good job i guess, you found it...neato burrito
     
      
                                     1. Rock
                                     2. Paper
                                     3. Scissors
                       Enter your choice I guess: """)
    print("""         enter "m" to return to the main menu: """)
    if p1_throw == op_throw:
        print("ya tied")
        sleep(1)
        hiddengem()
    elif p1_throw == "m":
        menu()
    elif p1_throw == "1" and op_throw == "2":
        print("Opponent throws paper = paper covers rock = Opponent win")
        sleep(1)
        hiddengem()
    elif p1_throw == "1" and op_throw == "3":
        print("Opponent throws scissors = rock crushes scissors = You win")
        sleep(1)
        hiddengem()
    elif p1_throw == "2" and op_throw == "1":
        print("Opponent throws rock= Paper covers rock = You win")
        sleep(1)
        hiddengem()
    elif p1_throw == "2" and op_throw == "3":
        print("Opponent throws scissors= scissors cut paper = Opponent win")
        sleep(1)
        hiddengem()
    elif p1_throw == "3" and op_throw == "2":
        print("Opponent throws paper = scissors cut paper = You win")
        sleep(1)
        hiddengem()
    elif p1_throw == "3" and op_throw == "1":
        print("Opponent throws rock = rock crushes scissors = Opponent win")
        sleep(1)
        hiddengem()

    else:
        hiddengem()


def rules():
    choice = input("""   the rules are plain. both you and the computer will select one of five "weapons"
                        the match is decided by the following rules: 

                        1. Scissors cuts paper, favoring scissors
                        2. Paper covers rock, favoring paper
                        3. Rock crushes lizard, favoring rock
                        4. Lizard poisons Spock, favoring lizard
                        5. Spock smashes scissors, favoring Spock
                        6. Scissors decapitates lizard, favoring scissors
                        7. Lizard eats paper, favoring lizard
                        8. Paper disproves Spock, favoring paper
                        9. Spock vaporizes rock, favoring Spock 
                        10. Rock crushes scissors, favoring rock


                        enter 'm' to return to the game:  
                    This all seems a bit overly complicated enter 'h':""")

    if choice == "m":
        menu()
    if choice != "m":
        hiddengem()
    else:
        print("You must choose a valid option.")
        print("Please try again.")
        rules()


win_condition = 3


def rematchq():
    global win_condition

    if win_condition == 3:
        choice = input(""" would you like a rematch?
                           Enter Y or N to respond:""")
        if choice == "n":
            if user_wins == 1:
                win()
                main()
            elif comp_wins == 1:
                gameover()
                print("Thank you for playing!")
                sleep(3)
                main()
        elif choice != "n":
            win_condition = input("best of 3(1) or first to 3?(2)")
        else:
            print("You must choose a valid option.")
            rematchq()

    if win_condition != 3:
        if win_condition == "1":
            if user_wins == 2:
                win()
                sleep(3)
                main()
            elif comp_wins == 2:
                gameover()
                sleep(3)
                main()
            else:
                menu()
        elif win_condition == "2":
            if user_wins == 3:
                win()
                sleep(3)
                main()
            elif comp_wins == 3:
                gameover()
                sleep(3)
                main()
            else:
                menu()

        else:
            print("You must choose a valid option.")
            print("Please try again.")
            rematchq()


def menu():
    global user_wins
    global comp_wins
    print("your wins:")
    print(user_wins)
    print("your opponent wins:")
    print(comp_wins)
    numpool = ["1","2","3","4","5"]
    comp_throw = random.choice(numpool)
    user_throw = input("""
                                 1. Rock
                                 2. Paper
                                 3. Scissors
                                 4. lizard
                                 5. Spock
                                 6. To view the rules before playing

                                 Please enter your choice: """)

    def shoot():
        if user_throw == "1":
            sleep(1)
            rock()
            shoot2()
        elif user_throw == "2":
            sleep(1)
            paper()
            shoot2()
        elif user_throw == "3":
            sleep(1)
            scissors()
            shoot2()
        elif user_throw == "4":
            sleep(1)
            lizard()
            shoot2()
        elif user_throw == "5":
            sleep(1)
            spock()
            shoot2()
        else:
            pass

    def shoot2():
        if comp_throw == "1":
            sleep(1)
            rock()
        elif comp_throw == "2":
            sleep(1)
            paper()
        elif comp_throw == "3":
            sleep(1)
            scissors()
        elif comp_throw == "4":
            sleep(1)
            lizard()
        elif comp_throw == "5":
            sleep(1)
            spock()
        else:
            pass

    if user_throw == comp_throw:
        draw()
        sleep(1)
        menu()
    elif user_throw == "1" and comp_throw == "2":
        shoot()
        print("Opponent throws paper = paper covers rock = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "1" and comp_throw == "3":
        shoot()
        print("Opponent throws scissors = rock crushes scissors = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "1" and comp_throw == "4":
        shoot()
        print("Opponent throws lizard = rock crushes lizard = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "1" and comp_throw == "5":
        shoot()
        print("Opponent throws spock = Spock vaporizes rock = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "2" and comp_throw == "3":
        shoot()
        print("Opponent throws scissors= scissors cut paper = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "2" and comp_throw == "4":
        shoot()
        print("Opponent throws lizard= lizard eats paper = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "2" and comp_throw == "5":
        shoot()
        print("Opponent throws spock = paper disproves Spock = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "2" and comp_throw == "1":
        shoot()
        print("Opponent throws rock= Paper covers rock = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "3" and comp_throw == "2":
        shoot()
        print("Opponent throws paper = scissors cut paper = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "3" and comp_throw == "1":
        shoot()
        print("Opponent throws rock = rock crushes scissors = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "3" and comp_throw == "4":
        shoot()
        print("Opponent throws lizard = scissors decapitate lizard = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "3" and comp_throw == "5":
        shoot()
        print("Opponent throws spock = Spock smashes scissors = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "4" and comp_throw == "2":
        shoot()
        print("Opponent throws paper = lizard eats paper = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "4" and comp_throw == "3":
        shoot()
        print("Opponent throws scissors = scissors decapitate lizard = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "4" and comp_throw == "1":
        shoot()
        print("Opponent throws rock = rock crushes lizard = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "4" and comp_throw == "5":
        shoot()
        print("Opponent throws Spock = lizard poisons Spock = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "5" and comp_throw == "2":
        shoot()
        print("Opponent throws paper = paper disproves Spock = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "5" and comp_throw == "3":
        shoot()
        print("Opponent throws scissors = Spock smashes scissors = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "5" and comp_throw == "4":
        shoot()
        print("Opponent throws lizard = lizard poisons Spock = Opponent win")
        comp_wins += 1
        rematchq()
        menu()
    elif user_throw == "5" and comp_throw == "1":
        shoot()
        print("Opponent throws rock = Spock vaporizes rock = You win")
        user_wins += 1
        rematchq()
        menu()
    elif user_throw == "6":
        rules()
    else:
        print("You must choose a valid option.")
        print("Please try again.")
        menu()


main()









