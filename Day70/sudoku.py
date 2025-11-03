class Solution:
    def solveSudoku(self, board):
        """
        Solves the Sudoku puzzle in-place using backtracking and DP-style caching.
        Each '.' will be filled with a valid number (1–9) such that:
        - Each row contains digits 1–9 exactly once.
        - Each column contains digits 1–9 exactly once.
        - Each 3x3 sub-box contains digits 1–9 exactly once.
        """

       
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        
        def backtrack(k):
            
            if k == len(empty_cells):
                return True

            r, c = empty_cells[k]
            box_index = (r // 3) * 3 + (c // 3)

            
            for ch in "123456789":
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_index]:
                    
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_index].add(ch)

                    
                    if backtrack(k + 1):
                        return True

                   
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_index].remove(ch)

            
            return False

        backtrack(0)
