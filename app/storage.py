# Simple in-memory "DB"
USERS = {}  # key: user_id (str), value: dict
NEXT_ID = 1

def generate_id():
    global NEXT_ID
    uid = str(NEXT_ID)
    NEXT_ID += 1
    return uid
