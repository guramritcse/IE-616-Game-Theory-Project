import random

num_players = int(input("Type the number of players: ")) # Number of players
chocofrac = round(60*random.random() + 20)              # Percentage of chocolate in cake
vanillafrac = 100 - chocofrac                           # Percentage of vanilla in cake

print("The current cake has " + str(chocofrac) + " percentage of chocolate topping and " \
      + str(vanillafrac)+ " percentage of vanilla topping" )
print("Player 1 gets to cut the cake ...")

#################################### 2 PLAYER GAME ####################################
if num_players == 2:
    piece = [[0,0], [0,0]]                              # pieces' specifications

    print("Enter piece 1 details")
    piece[0][0] = float(input("Chocolate percentage of original cake: "))
    # Sanity check
    while (piece[0][0] > chocofrac):               
        print("You can not have more than what is available :) , enter again ! ")
        piece[0][0] = float(input("Chocolate percentage of original cake: "))
    piece[0][1] = float(input("Vanilla percentage of original cake: "))
    # Sanity check
    while(piece[0][1] > vanillafrac):
        print("You can not have more than what is available :) , enter again ! ")
        piece[0][1] = float(input("Vanilla percentage of original cake: "))

    # Piece 2 details
    piece[1][0] = chocofrac - piece[0][0]
    piece[1][1] = vanillafrac - piece[0][1]

    # Pieces' specifications
    print("Piece 1 conatins " + str(piece[0][0]) + "% chocolate and " + str(piece[0][1]) \
        + "% vanilla")
    print("Piece 2 contains " + str(piece[1][0]) + "% chocolate and " + str(piece[1][1]) \
        + "% vanilla")
    
    print("Player 2 choose your desired piece...")
    piece_play2 = int(input()) - 1
    piece_play1 = 1 - piece_play2

    # Overall cake division        
    print("Player 1 gets piece number " + str(piece_play1 + 1) + " which ammounts to " \
        + str(piece[piece_play1][0]) + "% chocolate and " + str(piece[piece_play1][1]) \
        + "% vanilla")
    print("Player 2 gets piece number " + str(piece_play2 + 1) + " which ammounts to " \
        + str(piece[piece_play2][0]) + "% chocolate and " + str(piece[piece_play2][1]) \
        + "% vanilla")

#################################### 3 PLAYER GAME ####################################
elif num_players == 3:
    piece = [[0,0], [0,0], [0, 0]]                          # pieces' specifications
    trim = [[0,0], [0,0], [0, 0]]                           # trimming pieces' specifications

    print("Enter piece 1 details")
    piece[0][0] = float(input("Chocolate percentage of original cake: "))
    # Sanity check
    while (piece[0][0] > chocofrac):
        print("You can not have more than what is available :) , enter again ! ")
        piece[0][0] = float(input("Chocolate percentage of original cake: "))
    piece[0][1] = float(input("Vanilla percentage of original cake: "))
    # Sanity check
    while(piece[0][1] > vanillafrac):
        print("You can not have more than what is available :) , enter again ! ")
        piece[0][1] = float(input("Vanilla percentage of original cake: "))

    print("Enter piece 2 details")
    piece[1][0] = float(input("Chocolate percentage of original cake: "))
    # Sanity check
    while (piece[1][0] > chocofrac - piece[0][0]):
        print("You can not have more than what is available :) , enter again ! ")
        piece[1][0] = float(input("Chocolate percentage of original cake: "))   
    piece[1][1] = float(input("Vanilla percentage of original cake: "))
    # Sanity check
    while(piece[1][1] > vanillafrac - piece[0][1]):
        print("You can not have more than what is available :) , enter again ! ")
        piece[1][1] = float(input("Vanilla percentage of original cake: "))

    # Piece 3 details
    piece[2][0] = chocofrac - piece[0][0] - piece[1][0]
    piece[2][1] = vanillafrac - piece[0][1] - piece[1][1]
    # Pieces specifications'
    print("Piece 1 contains " + str(piece[0][0]) + "% chocolate and " + str(piece[0][1]) \
        + "% vanilla" )
    print("Piece 2 contains " + str(piece[1][0]) + "% chocolate and " + str(piece[1][1]) \
        + "% vanilla" )
    print("Piece 3 contains " + str(piece[2][0]) + "% chocolate and " + str(piece[2][1]) \
        + "% vanilla" )
    
    print("Player 2 choose your desired piece...")
    piece_play2 = int(input()) - 1
    print("Player 3 choose your desired piece...")
    piece_play3 = int(input()) - 1

    # Case 1: If both chose the same
    if(piece_play3 == piece_play2): 
        print("Player 2 please trim your chosen piece number " + str(piece_play2 + 1) \
            + " such that it matches with your second preferred piece")
        print("Beware! If Player 3 does not choose the trimmed piece, " \
            + "then you will have to take it")
        
        print("Enter trimming's details")
        trim_choco = float(input("Chocolate percentage in the trimming: "))
        while (trim_choco > piece[piece_play2][0]):
            print("You can not trim more than what is available :) , enter again !")
            trim_choco = float(input("Chocolate percentage in the trimming: "))
        trim_vanilla = float(input("Vanilla percentage in the trimming: "))
        while(trim_vanilla > piece[piece_play2][1]):
            print("You can not have more than what is available :) , enter again !")
            trim_vanilla = float(input("Vanilla percentage in the trimming: ")) 

        # Update pieces
        piece[piece_play2][0] -= trim_choco
        piece[piece_play2][1] -= trim_vanilla

        # Pieces and trimming specifications'
        print("Piece 1 has " + str(piece[0][0]) + "% chocolate and " + str(piece[0][1]) \
            + "% vanilla")
        print("Piece 2 has " + str(piece[1][0]) + "% chocolate and " + str(piece[1][1]) \
            + "% vanilla")
        print("Piece 3 has " + str(piece[2][0]) + "% chocolate and " + str(piece[2][1]) \
            + "% vanilla")
        print("Trimming has " + str(trim_choco) + "% chocolate and " + str(trim_vanilla) \
            + "% vanilla")
        
        # Player 3 to choose a piece
        print ("Player 3 choose your desired piece...") 
        piece_play3 = int(input()) - 1
        if(piece_play2 == piece_play3):
            not_trim_who = 2                                # player to cut the trimming
            print ("Player 2 choose your desired piece...") 
            piece_play2 = int(input()) - 1 
        else:
            not_trim_who = 3                                # player to cut the trimming
        piece_play1 = 3 - piece_play2 - piece_play3

        # Partial cake division       
        print("Player 1 gets piece number " + str(piece_play1 + 1) + " which ammounts to " \
            + str(piece[piece_play1][0]) + "% chocolate and " + str(piece[piece_play1][1]) \
            + "% vanilla")
        print("Player 2 gets piece number " + str(piece_play2 + 1) + " which ammounts to " \
            + str(piece[piece_play2][0]) + "% chocolate and " + str(piece[piece_play2][1]) \
            + "% vanilla")
        print("Player 3 gets piece number " + str(piece_play3 + 1) + " which ammounts to " \
            + str(piece[piece_play3][0]) + "% chocolate and " + str(piece[piece_play3][1]) \
            + "% vanilla")
        
        print("Now coming to the division of the trimming ...")
        print("Player " + str(not_trim_who) + " gets to cut the trimming into 3 parts ...")

        print("Enter trimming's piece 1 details")
        trim[0][0] = float(input("Chocolate percentage of trim cake for first piece: "))
        # Sanity check
        while (trim[0][0] > trim_choco):
            print("You can not have more than what is available :) , enter again ! ")
            trim[0][0] = float(input("Chocolate percentage of trim cake for first piece: "))
        trim[0][1] = float(input("Vanilla percentage of trim cake for first piece: "))
        # Sanity check
        while(trim[0][1] > trim_vanilla):
            print("You can not have more than what is available :) , enter again ! ")
            trim[0][1] = float(input("Vanilla percentage of trim cake for first piece: "))

        print("Enter trimming's piece 2 details")
        trim[1][0] = float(input("Chocolate percentage of trim cake for second piece: "))
        # Sanity check
        while (trim[1][0] > trim_choco - trim[0][0]):
            print("You can not have more than what is available :) , enter again ! ")
            trim[1][0] = float(input("Chocolate percentage of trim cake for second piece: "))   
        trim[1][1]= float(input("Vanilla percentage of trim cake for second piece: "))
        # Sanity check
        while(trim[1][1] > trim_vanilla-trim[0][1]):
            print("You can not have more than what is available :) , enter again ! ")
            trim[1][1]= float(input("Vanilla percentage of trim cake for second piece: "))

        # Trimming piece 3 details
        trim[2][0] = trim_choco - trim[0][0] - trim[1][0]
        trim[2][1] = trim_vanilla - trim[0][1] - trim[1][1]

        # Trimmings' specifications
        print("Trim Piece 1 has " + str(trim[0][0]) + "% chocolate and " + str(trim[0][1]) \
            + "% vanilla" )
        print("Trim Piece 2 has " + str(trim[1][0]) + "% chocolate and " + str(trim[1][1]) \
            + "% vanilla" )
        print("Trim Piece 3 has " + str(trim[2][0]) + "% chocolate and " + str(trim[2][1]) \
            + "% vanilla" )
        
        print("Player " + str(5 - not_trim_who) + " choose a piece from the above pieces...")
        trim_play_2or3 = int(input()) - 1
        print("Player 1 choose a piece from the remaining 2 pieces of trimming... ")
        trim_play_1 = int(input()) - 1
        # Sanity check
        while(trim_play_1 == trim_play_2or3):
            print("NO NO, can't take the piece that has already been taken, \
                choose some other piece number !")
            trim_play_1 = int(input()) - 1

        if not_trim_who == 2:
            trim_play_3 = trim_play_2or3                    # Player 3 got to choose first
            trim_play_2 = 3 - trim_play_1 - trim_play_3
        else:
            trim_play_2 = trim_play_2or3                    # Player 2 got to choose first
            trim_play_3 = 3 - trim_play_1 - trim_play_2

        # Overall cake division        
        print("Player 1 gets piece number " + str(piece_play1 + 1) + " and trimming piece" \
            + " number " + str(trim_play_1 + 1) + " which ammounts to " \
            + str(piece[piece_play1][0] + trim[trim_play_1][0]) + "% chocolate and " \
            + str(piece[piece_play1][1] + trim[trim_play_1][1]) + "% vanilla")
        print("Player 2 gets piece number " + str(piece_play2 + 1) + " and trimming piece" \
            + " number " + str(trim_play_2 + 1) + " which ammounts to " \
            + str(piece[piece_play2][0] + trim[trim_play_2][0]) + "% chocolate and " \
            + str(piece[piece_play2][1] + trim[trim_play_2][1]) + "% vanilla")
        print("Player 3 gets piece number " + str(piece_play3 + 1) + " and trimming piece" \
            + " number " + str(trim_play_3 + 1) + " which ammounts to " \
            + str(piece[piece_play3][0] + trim[trim_play_3][0]) + "% chocolate and " \
            + str(piece[piece_play3][1] + trim[trim_play_3][1]) + "% vanilla")

    # Case 2: If both chose different, then we are done. Allot them their chosen pieces
    else:
        piece_play1 = 3 - piece_play2 - piece_play3 
        # Overall cake division        
        print("Player 1 gets piece number " + str(piece_play1 + 1) + " which ammounts to " \
            + str(piece[piece_play1][0]) + "% chocolate and " + str(piece[piece_play1][1]) \
            + "% vanilla")
        print("Player 2 gets piece number " + str(piece_play2 + 1) + " which ammounts to " \
            + str(piece[piece_play2][0]) + "% chocolate and " + str(piece[piece_play2][1]) \
            + "% vanilla")
        print("Player 3 gets piece number " + str(piece_play3 + 1) + " which ammounts to " \
            + str(piece[piece_play3][0]) + "% chocolate and " + str(piece[piece_play3][1]) \
            + "% vanilla")
else:
    print("Number of players can be either 2 or 3 !")
    exit()
print("Enjoy !")