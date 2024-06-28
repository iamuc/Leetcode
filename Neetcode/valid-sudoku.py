#https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def get_pos(row,col) -> (int,int,int):
            """
            Returns the row, col, sub of a position in board
            """
            row0=int(row)+1
            col0=int(col)+1
            sub0=3*((row0-1)//3) + ((col0-1)//3) + 1
            return (row0,col0,sub0)

        row={i :set([]) for i in range(1,10)}
        col={i :set([]) for i in range(1,10)}
        sub={i :set([]) for i in range(1,10)}
        dict={"row":row,"col":col,"sub":sub}

        for row,list in enumerate(board):
            for col,val in enumerate(list):
                if val==".":
                    pass
                else:
                    row0,col0,sub0 = get_pos(row,col)
                    print(val,(row0,col0,sub0))
                    if (val in dict["row"][row0]) or (val in dict["col"][col0]) or (val in dict["sub"][sub0]):
                        return False
                    else:
                        dict["row"][row0].add(val)
                        dict["col"][col0].add(val)
                        dict["sub"][sub0].add(val)
        return True
                
