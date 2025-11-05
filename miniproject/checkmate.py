# checkmate.py

def find_king(board):
    """
    ค้นหาตำแหน่ง (แถว, คอลัมน์) ของ King ('K') บนกระดาน
    """
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                return r, c
    return -1, -1 # ไม่พบ King

def is_valid(r, c, size):
    """
    ตรวจสอบว่าตำแหน่ง (r, c) อยู่ภายในขอบเขตของกระดานหรือไม่
    """
    return 0 <= r < size and 0 <= c < size

def check_line_of_sight(board, king_r, king_c, dr, dc, pieces):
    """
    ตรวจสอบตามแนวเส้นตรง (เส้นทแยงมุม หรือ แนวนอน/แนวตั้ง) 
    จาก King ว่ามีหมากรุกหรือไม่
    
    :param dr: ทิศทางการเปลี่ยนแถว (+1, 0, -1)
    :param dc: ทิศทางการเปลี่ยนคอลัมน์ (+1, 0, -1)
    :param pieces: ชุดของหมากรุกที่สามารถโจมตีในทิศทางนี้ได้ ('B', 'Q' หรือ 'R', 'Q')
    """
    size = len(board)
    r, c = king_r + dr, king_c + dc
    
    while is_valid(r, c, size):
        piece = board[r][c]
        if piece in pieces:
            # พบหมากรุกที่สามารถโจมตี King ได้
            return True 
        elif piece != '.': 
            # พบหมากตัวอื่นขวางทางไว้ (ถือว่าไม่ถูกรุกในทิศทางนี้)
            return False 
        
        r, c = r + dr, c + dc
    
    return False

def checkmate(board_rows):
    """
    ฟังก์ชันหลักในการตรวจสอบว่า King ถูกรุกหรือไม่
    
    :param board_rows: tuple/list ของแถวของกระดาน (string)
    """
    # 1. จัดรูปแบบกระดานให้เป็น list of list ของอักขระ
    # และตรวจสอบว่ากระดานเป็นรูปสี่เหลี่ยมจัตุรัสหรือไม่
    if not board_rows:
        # กรณีไม่มีแถวให้คืนค่าเป็น False หรือจัดการข้อผิดพลาดตามที่โจทย์ต้องการ
        # ในตัวอย่างนี้จะถือว่า Fail (ไม่ถูกรุกเพราะไม่มีกระดาน)
        print("Fail")
        return

    board = [list(row) for row in board_rows]
    size = len(board)
    for row in board:
        if len(row) != size:
            # กระดานไม่เป็นสี่เหลี่ยมจัตุรัส จัดการข้อผิดพลาด
            print("Fail") # หรือ "Error" ตามการจัดการ
            return 
    
    # 2. ค้นหาตำแหน่งของ King
    king_r, king_c = find_king(board)
    if king_r == -1:
        # ไม่พบ King ถือว่าไม่ถูกรุก
        print("Fail")
        return

    # 3. ตรวจสอบการรุกจาก Pawn ('P')
    # Pawn สามารถโจมตีแนวทแยงมุมไปข้างหน้า 1 ช่อง (สมมติ King อยู่ฝั่งที่ Pawn โจมตีมา)
    # สมมติให้ King เป็นหมากสีขาว ('K') และ Pawn เป็นหมากฝ่ายตรงข้าม ('P')
    # King อยู่แถว (king_r, king_c)
    # Pawn ต้องอยู่แถว king_r - 1 (ถ้าหมากฝ่ายตรงข้ามเคลื่อนที่ขึ้น) 
    # หรือแถว king_r + 1 (ถ้าหมากฝ่ายตรงข้ามเคลื่อนที่ลง)
    # สำหรับโจทย์นี้จะ **สมมติ** ว่า King อยู่แถวที่สูงกว่า (r น้อยกว่า) และ Pawn โจมตีลงมา
    pawn_r = king_r - 1 
    if is_valid(pawn_r, king_c - 1, size) and board[pawn_r][king_c - 1] == 'P':
        print("Success")
        return
    if is_valid(pawn_r, king_c + 1, size) and board[pawn_r][king_c + 1] == 'P':
        print("Success")
        return
        
    # 4. ตรวจสอบการรุกจาก Bishop ('B') และ Queen ('Q') (แนวทแยงมุม)
    # ทิศทางทแยงมุม: (1, 1), (1, -1), (-1, 1), (-1, -1)
    diagonal_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in diagonal_dirs:
        if check_line_of_sight(board, king_r, king_c, dr, dc, {'B', 'Q'}):
            print("Success")
            return

    # 5. ตรวจสอบการรุกจาก Rook ('R') และ Queen ('Q') (แนวตั้ง/แนวนอน)
    # ทิศทางแนวนอน/แนวตั้ง: (1, 0), (-1, 0), (0, 1), (0, -1)
    straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in straight_dirs:
        if check_line_of_sight(board, king_r, king_c, dr, dc, {'R', 'Q'}):
            print("Success")
            return
    
    # ถ้าตรวจสอบทั้งหมดแล้วไม่ถูกรุก
    print("Fail")