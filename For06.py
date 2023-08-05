def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s = []
    sm = 0
    l = len(s)
    m = 0
    for i in range(A,B):
        s.append(i)
    while len(s)>m:
        sm += s[m]
        m += 1
    return sm
print(main(4,8))