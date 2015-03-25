def getRatios(v1, v2):
    """Assumes v1 and v2 are lists of equal length of numbers
    Returns a list containing the meaningful values of 
    v1[i]/v2[i]"""
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))#NaN = Not a number
        except:
            raise ValueError('getRatios called with bad arg')
        return ratios