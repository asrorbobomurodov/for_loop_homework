def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    s = []
    ss = 0
    for i in range(1,N+1):
        s.append(1/i)
        ss += s[i-1]
    return ss
print(main(5))