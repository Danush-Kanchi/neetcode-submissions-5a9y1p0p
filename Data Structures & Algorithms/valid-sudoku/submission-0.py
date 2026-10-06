class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        boxes=defaultdict(set)

        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value ==".":
                    continue
                if value in row[r] or value in col[c] or value in boxes[(r//3,c//3)]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                boxes[(r//3,c//3)].add(value)
        return True