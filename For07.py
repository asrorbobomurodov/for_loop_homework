def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    s = []
    for odd in range(1,N,2):
        s.append(odd)
    return sum(s)
print(main(8))