def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s = []
    for i in range(n):
        i = str(i)
        s.append(i)
    x =",".join(s)
    return f'"{x}"'
print(main(7))