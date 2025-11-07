def find_king(board):
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                return r, c
    return -1, -1 

def is_valid(r, c, size):
    
    return 0 <= r < size and 0 <= c < size

def check_line_of_sight(board, king_r, king_c, dr, dc, pieces):
    
    size = len(board)
    r, c = king_r + dr, king_c + dc
    
    while is_valid(r, c, size):
        piece = board[r][c]
        if piece in pieces:
            
            return True 
        elif piece != '.': 
            
            return False 
        
        r, c = r + dr, c + dc
    
    return False

def checkmate(board_rows):
    
    
    if not board_rows:

        print("Fail")
        return

    board = [list(row) for row in board_rows]
    size = len(board)
    for row in board:
        if len(row) != size:
            
            print("Fail") 
            return 
    
    
    king_r, king_c = find_king(board)
    if king_r == -1:
        
        print("Fail")
        return

    
    pawn_r = king_r - 1 
    if is_valid(pawn_r, king_c - 1, size) and board[pawn_r][king_c - 1] == 'P':
        print("Success")
        return
    if is_valid(pawn_r, king_c + 1, size) and board[pawn_r][king_c + 1] == 'P':
        print("Success")
        return
        
    
    diagonal_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in diagonal_dirs:
        if check_line_of_sight(board, king_r, king_c, dr, dc, {'B', 'Q'}):
            print("Success")
            return

    
    straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in straight_dirs:
        if check_line_of_sight(board, king_r, king_c, dr, dc, {'R', 'Q'}):
            print("Success")
            return
    

    print("Fail")