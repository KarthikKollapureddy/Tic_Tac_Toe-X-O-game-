Board={
       'T1':' ','T2':' ','T3':' ',
       'M1':' ','M2':' ','M3':' ',
       'D1':' ','D2':' ','D3':' ',
       }
Player= 1  #initialise 1st player
total_moves = 0 #to count
end_check = 0
def check():        # checking t end 
# horizntal
    if  Board["T1"]=="X" and  Board["T2"]=="X" and  Board["T3"]=="X":
        print("player One Wins!")
        return 1
    if  Board["M1"]=="X" and  Board["M2"]=="X" and  Board["M3"]=="X":
        print("player One Wins!")
        return 1
    if  Board["D1"]=="X" and  Board["D2"]=="X" and  Board["D3"]=="X":
        print("player One Wins!")
        return 1
# vertival
    if  Board["T1"]=="X" and  Board["M1"]=="X" and  Board["D1"]=="X":
        print("player One Wins!")
        return 1
    if  Board["T2"]=="X" and  Board["M2"]=="X" and  Board["D2"]=="X":
        print("player One Wins!")
        return 1
    if  Board["T3"]=="X" and  Board["M3"]=="X" and  Board["D3"]=="X":
        print("player One Wins!")
        return 1
#diagonal       
    if  Board["T1"]=="X" and  Board["M2"]=="X" and  Board["D3"]=="X":
        print("player One Wins!")
        return 1
# for player 2    
    # horizntal
    if  Board["T1"]=="O" and  Board["T2"]=="O" and  Board["T3"]=="O":
        print("player Two Wins!")
        return 1
    if  Board["M1"]=="O" and  Board["M2"]=="O" and  Board["M3"]=="O":
        print("player Two Wins!")
        return 1
    if  Board["D1"]=="O" and  Board["D2"]=="O" and  Board["D3"]=="O":
        print("player Two Wins!")
        return 1
# vertival
    if  Board["T1"]=="O" and  Board["M1"]=="O" and  Board["D1"]=="O":
        print("player Two Wins!")
        return 1
    if  Board["T2"]=="O" and  Board["M2"]=="O" and  Board["D2"]=="O":
        print("player Two Wins!")
        return 1
    if  Board["T3"]=="O" and  Board["M3"]=="O" and  Board["D3"]=="O":
        print("player Two Wins!")
        return 1
#diagonal       
    if  Board["T1"]=="X" and  Board["M2"]=="O" and  Board["D3"]=="O":
        print("player Two Wins!")
        return 1
    return 0
print('T1|T2|T3'.center(20))
print('--+--+--'.center(20))
print('M1|M2|M3'.center(20))
print('--+--+--'.center(20))
print('D1|D2|D3'.center(20))
print('*'*25)

while True:
    print((Board['T1']+'|'+Board['T2']+' |'+Board['T3']).center(20))
    print('--+--+--'.center(20))
    print((Board['M1']+'|'+Board['M2']+' |'+Board['M3']).center(20))
    print('--+--+--'.center(20))
    print((Board['D1']+'|'+Board['D2']+' |'+Board['D3']).center(20))
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if Player == 1:
            P1_input = input('Player One: ')
            if P1_input.upper() in Board and Board[P1_input.upper()] == " ":
                Board[P1_input.upper()] = "X"
                Player = 2
                break
            else:       # on wrong input
                print("Invalid Input, Please try again")
                continue
        else:
            P2_input = input('Player Two: ')
            if P2_input.upper() in Board and Board[P2_input.upper()] == " ":
                Board[P2_input.upper()] = "O"  
                Player = 1 
                break
            else:        # on wrong input
                print("Invalid Input, Please try again")
                continue
    total_moves += 1
    print('*'*25)        