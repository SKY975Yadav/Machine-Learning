# Logical AND operation
def logical_and(x, y):
    return x and y

# Logical OR operation
def logical_or(x, y):
    return x or y

# Logical NOT operation
def logical_not(x):
    return not x

# Logical XOR (exclusive OR) operation
def logical_xor(x, y):
    return (x and not y) or (not x and y)

# Logical NAND (NOT AND) operation
def logical_nand(x, y):
    return not (x and y)

# Logical NOR (NOT OR) operation
def logical_nor(x, y):
    return not (x or y)

# Logical XNOR (NOT XOR) operation
def logical_xnor(x, y):
    return not logical_xor(x, y)