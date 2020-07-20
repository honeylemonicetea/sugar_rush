tic_tac = [["_" for i in range(3)] for j in range(3)]
print("---------")
for i in tic_tac:
    f = " ".join(i)
    print(f"| {f} |")
print("---------")
moves = 1
while True:
    coord = input("Enter coordiantes: ").split()
    #check if entered coordinates are valid and enter x if moves is an odd number
    if moves % 2 == 1:
        if coord[0].isdigit() == True and coord[1].isdigit() == True:
            if 1 <= int(coord[0]) <= 3 and 1 <= int(coord[1]) <= 3:
                if tic_tac[-int(coord[1])][int(coord[0]) - 1] != '_':
                    print("This cell is occupied! Choose another one!")
                else:
                    tic_tac[-int(coord[1])][int(coord[0]) - 1] = 'X'
                    print("---------")
                    for i in tic_tac:
                        f = " ".join(i)
                        print(f"| {f} |")
                    print("---------")
                    moves += 1
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    #same but o if moves is an even number
    elif moves % 2 == 0:
        if coord[0].isdigit() == True and coord[1].isdigit() == True:
            if 1 <= int(coord[0]) <= 3 and 1 <= int(coord[1]) <= 3:
                if tic_tac[-int(coord[1])][int(coord[0]) - 1] != '_':
                    print("This cell is occupied! Choose another one!")
                else:
                    tic_tac[-int(coord[1])][int(coord[0]) - 1] = 'O'
                    print("---------")
                    for i in tic_tac:
                        f = " ".join(i)
                        print(f"| {f} |")
                    print("---------")
                    moves += 1
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    # Board analysis
    # checking coincidences in double array
    if tic_tac[0][0] == tic_tac[1][1] == tic_tac[2][2]:
        if tic_tac[0][0] != '_':
            print(f"{tic_tac[0][0]} wins")
            break
    elif tic_tac[0][2] == tic_tac[1][1] == tic_tac[2][0]:
        if tic_tac[0][2] != '_':
            print(f"{tic_tac[0][2]} wins")
            break
        #checking vertical coincidences
    elif tic_tac[0][0] == tic_tac[1][0] == tic_tac[2][0] or tic_tac[0][1] == tic_tac[1][1] == tic_tac[2][1] or tic_tac[0][2] == tic_tac[1][2] == tic_tac[2][2]:
        tms = 0
        ctr = 0
        crosser = 0
        ower = 0
        for j in range(3):
            for i in range(3):
                if tic_tac[i][j] == 'X':
                    crosser += 1
                elif tic_tac[i][j] == 'O':
                    ower += 1
                else:
                    continue
            if crosser == 3:
                tms += 1
            elif ower == 3:
                ctr += 1
            crosser = 0
            ower = 0
        if tms == 1 and ctr == 0:
            print("X wins")
            break
        elif tms == 0 and ctr == 1:
            print("O wins")
            break
            #change conditions
    elif tic_tac[0][0] == tic_tac[0][1] == tic_tac[0][2] or tic_tac[1][0] == tic_tac[1][1] == tic_tac[1][2] or tic_tac[2][0] == tic_tac[2][1] == tic_tac[2][2]:
        ctr = 0
        tms = 0
        crosser = 0
        ower = 0
        for i in range(3):
            for j in range(3):
                if tic_tac[i][j] == 'X':
                    crosser += 1
                elif tic_tac[i][j] == 'O':
                    ower += 1
                else:
                    continue
            if crosser == 3:
                tms += 1
            elif ower == 3:
                ctr += 1
            crosser = 0
            ower = 0
        if tms == 1 and ctr == 0:
            print("X wins")
            break
        elif tms == 0 and ctr == 1:
            print("O wins")
            break
    else:
        c = 0
        for i in tic_tac:
            al = "".join(i)
            c += al.count("_")
        if c == 0:
            print("Draw")
            break

