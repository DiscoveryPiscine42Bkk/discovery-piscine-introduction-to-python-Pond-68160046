# main.py

from checkmate import checkmate

def main():
    # ตัวอย่าง 1: King ถูกรุกโดย Rook (R) (สมมติว่า R สามารถรุก K ได้ตามตัวอย่าง)
    # กระดาน 3x3:
    # . . .
    # . K .
    # . R .
    board1 = (
        "...",
        ".K.",
        ".R."
    )
    print("--- Test 1 (Success) ---")
    checkmate(board1) # คาดหวัง "Success"
    
    # ตัวอย่าง 2: King ไม่ถูกรุก
    # กระดาน 3x3:
    # . . .
    # . K .
    # P . . 
    board2 = (
        "P.P",
        ".K.",
        "..."
    )
    print("--- Test 2 (Fail) ---")
    checkmate(board2) # คาดหวัง "Fail"
    
    # ตัวอย่าง 3: King ถูกรุกโดย Bishop (B)
    # กระดาน 4x4:
    # B . . .
    # . . . .
    # . . . .
    # . . . K
    board3 = (
        "B...",
        "....",
        "....",
        "...K"
    )
    print("--- Test 3 (Success) ---")
    checkmate(board3) # คาดหวัง "Success"

if __name__ == "__main__":
    main()