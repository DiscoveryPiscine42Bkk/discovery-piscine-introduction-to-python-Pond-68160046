from checkmate import checkmate

def main():
    
    board1 = (
        "...",
        ".K.",
        ".R."
    )
    print("--- Test 1 (Success) ---")
    checkmate(board1) 
    
    
    board2 = (
        "P.P",
        ".K.",
        "..."
    )
    print("--- Test 2 (Fail) ---")
    checkmate(board2) 
    board3 = (
        "B...",
        "....",
        "....",
        "...K"
    )
    print("--- Test 3 (Success) ---")
    checkmate(board3) 

if __name__ == "__main__":
    main()