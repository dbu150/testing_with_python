"""
You’re designing a gate access system. Access is granted only if:

The user is verified (verified == True)

The user has an even ID (id & 1 == 0)

The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
"""
def gate_access(verified, user_id, flags):
    """
    Access is granted only if:
    1. The user is verified (verified == True)
    2. The user has an even ID (user_id & 1 == 0)
    3. The security flag bits contain at least one 1 in the last 3 bits (flags & 0b111 != 0)
    """
    
    if verified and (user_id & 1 == 0) and (flags & 0b111 != 0):
        return "Access Granted "
    else:
        return "Access Denied "

#calling the function
print(gate_access(True, 102, 0b101))   # Granted  verified, even ID, last 3 bits have a 1
print(gate_access(True, 103, 0b101))   # Denied odd ID
print(gate_access(False, 100, 0b111))  # Denied not verified
