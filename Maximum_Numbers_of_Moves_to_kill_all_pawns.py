'''
There is a 50 x 50 chessboard with one knight and some pawns on it. You are given two integers kx and ky where (kx, ky) denotes the position of the knight, and a 2D array positions where positions[i] = [xi, yi] denotes the position of the pawns on the chessboard.

Alice and Bob play a turn-based game, where Alice goes first. In each player's turn:

The player selects a pawn that still exists on the board and captures it with the knight in the fewest possible moves. Note that the player can select any pawn, it might not be one that can be captured in the least number of moves.
In the process of capturing the selected pawn, the knight may pass other pawns without capturing them. Only the selected pawn can be captured in this turn.
Alice is trying to maximize the sum of the number of moves made by both players until there are no more pawns on the board, whereas Bob tries to minimize them.

Return the maximum total number of moves made during the game that Alice can achieve, assuming both players play optimally.

Note that in one move, a chess knight has eight possible positions it can move to, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

https://assets.leetcode.com/uploads/2024/08/01/chess_knight.jpg

Example 1:

Input: kx = 1, ky = 1, positions = [[0,0]]

Output: 4

Explanation:

https://assets.leetcode.com/uploads/2024/08/16/gif3.gif

The knight takes 4 moves to reach the pawn at (0, 0)

Example 2:

Input: kx = 0, ky = 2, positions = [[1,1],[2,2],[3,3]]

Output: 8

Explanation:

https://assets.leetcode.com/uploads/2024/08/16/gif4.gif

Alice picks the pawn at (2, 2) and captures it in two moves: (0, 2) -> (1, 4) -> (2, 2).
Bob picks the pawn at (3, 3) and captures it in two moves: (2, 2) -> (4, 1) -> (3, 3).
Alice picks the pawn at (1, 1) and captures it in four moves: (3, 3) -> (4, 1) -> (2, 2) -> (0, 3) -> (1, 1).
Example 3:

Input: kx = 0, ky = 0, positions = [[1,2],[2,4]]

Output: 3

Explanation:

Alice picks the pawn at (2, 4) and captures it in two moves: (0, 0) -> (1, 2) -> (2, 4). Note that the pawn at (1, 2) is not captured.
Bob picks the pawn at (1, 2) and captures it in one move: (2, 4) -> (1, 2).
 

Constraints:

0 <= kx, ky <= 49
1 <= positions.length <= 15
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 49
All positions[i] are unique.
The input is generated such that positions[i] != [kx, ky] for all 0 <= i < positions.length.
'''

'''Solution:'''

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        INF = float('Inf')
        @cache
        def calcMovesShortest(knx,kny):
            board = [[INF]*50 for _ in range(50)]
            moves = [(0,knx,kny)]
            board[knx][kny] = 0
            while moves:
                cost,x,y = heappop(moves)
                if cost > board[x][y]:
                    continue
                for xpos in (x-2,x+2):
                    if xpos >= 0 and xpos < 50:
                        for ypos in (y-1,y+1):
                            if ypos >= 0 and ypos < 50:
                                if board[xpos][ypos] > (cost+1):
                                    board[xpos][ypos] = cost+1
                                    heappush(moves,(cost+1,xpos,ypos))           
                for xpos in (x-1,x+1):
                    if xpos >= 0 and xpos < 50:
                        for ypos in (y-2,y+2):
                            if ypos >= 0 and ypos < 50:
                                if board[xpos][ypos] > (cost+1):
                                    board[xpos][ypos] = cost+1
                                    heappush(moves,(cost+1,xpos,ypos))
            return board  
        NSTEP = len(positions)
        pawns = positions[:] 
        @cache
        def calc(curx,cury, step, captured):
            if NSTEP == step:
                return 0
            brd = calcMovesShortest(curx,cury)
            table = []
            for i in range(NSTEP):
                if captured & (1<<i):
                    continue
                x,y = pawns[i]
                table.append( (brd[x][y],i) ) 
            ret = INF if (step&1) else 0
            for c,idx in table:
                cap2 = captured | (1<<idx)
                x,y = pawns[idx]
                calccost = c+calc(x,y, step+1,cap2)
                ret = min(ret,calccost) if (step&1) else max(ret,calccost)
            return ret
        return calc(kx,ky,0,0)

'''Intution/Approach'''
"""
Intuition:
In Alice's turn we try to capture the existing pawns one by one and maximize the moves, while in Bob's turn we minimize the moves.

Dijkstra shortest path can find the shortest path from the current knight position to every corner of the board.

And we can take dynamic programming approach to reduce the exponential way of choosing subproblems.

Approach:
We have a calc function that recursively calculates the moves of a player. Index of the captured pawns are kept as a bit-mask.

calc calculates the moves in each turn
curx,cury is the x,y position of the knight
step is the turn or recursion depth
when step == len(pawns) that ends the algorithm
captured is the bitmask of the captured pawn
Again we have calcMovesShortest which runs Dijkstra shortest path algorithm from knight position (knx,kny) to all the other positions in the board.

Complexity
Time complexity:
O(2^15)

Space complexity:
O(2^15)
"""
