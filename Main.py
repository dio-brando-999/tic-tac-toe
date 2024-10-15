def main():
    grid = [

        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    for row in grid:
        print(row)
    print("Player 1 is X, Player 2 is O")
    inGame = True
    while inGame:
        if(check(grid)!= None):
            break
        x = player1Input() 
        outputX(grid,x)
        for row in grid:
            print(row)
        if(check(grid)!= None):
            break
        o = player2Input()
        outputO(grid,o)
        for row in grid:
            print(row)
    print(check(grid)+" won!")

#prompts and returns the value of where P1 wants to place
def player1Input():
    x= 11
    while(not 0<int(x)<10):
        x = input("Player 1:")
        if(not x.isdigit()):
            print("why")
            x = 11
    return int(x)-1
#prompts and returns the value of where P2 wants to place
def player2Input():
    o= 11
    while(not 0<int(o)<10):
        o = input("Player 2:")
        if(not o.isdigit()):
            print("")
            o = 11
    return int(o)-1

#changes grid to display "X" based on P1's input
def outputX(grid,x):
    grid[x//3][x%3] = "X"

#changes grid to display "O" based on P2's input
def outputO(grid,o):
    grid[o//3][o%3] = "O"

#checks for any winning case. Returns letter of winner, indicting which player won
def check(grid):
    #check row
    for row in grid:
        if(row[0]==row[1]==row[2]):
            return row[0]
    #check columns
    for col in range(3):
        if(grid[0][col]==grid[1][col]==grid[2][col]):
            return grid[0][col]
    #check two diagonal winning case
    if(grid[0][0]==grid[1][1]==grid[2][2]):
        return grid[0][0]
    if(grid[0][2]==grid[1][1]==grid[2][0]):
        return grid[0][2]
    return None

main()

#add a check so that indicies can not be changed by retyping the grid's index
#add a check if game ends in tie