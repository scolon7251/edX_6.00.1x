def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n % 3 == 0 or n % 20 == 0:
        return True
    else:
        return False