#Name of the game: 100 game
#This game is to have fun with your friend and the person who reaches 100 first wins
#Ahmed Yasser El-Sayed
#ID:20231016
sum = 0
#Introduction to the game
print("Welcome to 100 game")
print("Every player should choose a number from 1-10 and the player who reaches 100 first wins")
#now the player should choose a number from 1-10
while sum < 100:
    # Now the first player should choose a number from 1-10
    player_1 = int(input("Player one: please choose number from 1-10: "))
    while 1 <= player_1 <= 10:
        sum = sum + player_1
        #This step is to make sure that the player will not exceed 100
        while sum > 100:
            sum -= player_1
            player_1 = int(input("Player one: please choose number from 1-10 and less than this number"))
            while player_1 == 0:
                player_1 = int(input("Player one: please choose number from 1-10: "))
                if 1 <= player_1 <= 10:
                    break
            sum += player_1
            if sum <= 100:
                break
        if sum == 100:
            print("Now the sum = 100")
            print("Player one wins")
            break
        else:
            print("Now the total number = ", sum)
            break
    # This step to make sure that the player will follow the game rules
    while player_1 > 10 or player_1 <= 0:
        print("Please try again")
        player_1 = int(input("Player one: please choose number from 1-10: "))
        if 1 <= player_1 <= 10:
            sum = player_1 + sum
            print("Now the total number = ", sum)
            break
    if sum == 100:
        break
    #The second player turn to play
    player_2 = int(input("Player two: please choose number from 1-10: "))
    while 1 <= player_2 <= 10:
        sum = sum + player_2
        # This step is to make sure that the player will not exceed 100
        while sum > 100:
            sum -= player_2
            player_2 = int(input("Player two: please choose number from 1-10 and less than this number"))
            while player_2 == 0:
                player_2 = int(input("Player two: please choose number from 1-10: "))
                if 1 <= player_2 <= 10:
                    break
            sum += player_2
            if sum <= 100:
                break
        if sum == 100:
            print("Now the sum = 100")
            print("Player two wins")
            break
        else:
            print("Now the total number = ", sum)
            break
    # This step to make sure that the player will follow the game rules
    while player_2 > 10 or player_2 <= 0:
        print("Please try again")
        player_2 = int(input("Player two: please choose number from 1-10: "))
        if 1 <= player_2 <= 10:
            sum = player_2 + sum
            print("Now the total number = ", sum)
            break
