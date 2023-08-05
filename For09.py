def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s = []
    '''
    for int values
    # for i in range(price, price*10+1, price): 
    #     s.append(i) 
    '''
    ss = price
    for i in range(1, 11):
        s.append(ss)
        ss += price
    return s
print(main(2.25))