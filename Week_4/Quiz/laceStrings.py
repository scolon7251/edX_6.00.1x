def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
 
    
    count1 = 0
    count2 = 0
    newString = ''
    while count1 != len(s1) and count2 != len(s2):
        newString += s1[count1]
        count1 += 1
        
        newString += s2 [count2]
        count2 += 1
            
        
    if len(s1) != len(s2):
        newString += s1[count1:] or s2[count2:]
        
    return newString
  