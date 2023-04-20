def max3(x, y, z):
    """Receives three numbers as input and returns the largest of them.

    Parameters:
        x (int): A decimal integer
        y (int): A decimal integer
        z (int): A decimal integer

    Returns:
        max_int (int): largest of three numbers

    """
    return max(x, y, z)


print(max3(22, 33, 44))
print(max3.__doc__)  # داک استرینگ این تابع رو چاپ میکنه
# print(help(max3))  # داک استرینگ این تابع رو چاپ میکنه
