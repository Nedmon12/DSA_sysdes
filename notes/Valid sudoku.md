create 3 hashsets
rows, columns and squares

iterate through the grid (nested loops)

if empty jump
if item is in the current row set or
if item is in the current column set or
if item is in the current square set 
return false

else append and move on 
finally return true

```
class Solution:

def isValidSudoku(self, board: List[List[str]]) -> bool:

cols = collections.defaultdict(set)

rows = collections.defaultdict(set)

squares = collections.defaultdict(set)

  

for r in range(9):

for c in range(9):

if board[r][c] == '.':

continue

if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3, c//3)]:

return False

cols[c].add(board[r][c])

rows[r].add(board[r][c])

squares[(r//3, c//3)].add(board[r][c])

  

return True
```