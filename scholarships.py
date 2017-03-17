"""Rough draft brute force solutions"""


def findGreatest(self, matrix, k):
    """Takes in matrix, finds k consecutive values that multiply to largest value"""

    sequence = [k]
    maxTotal = 0
    tmp = 0

    # Horizontal span O(n^2)
    for row in matrix:
        for i in range(len(row)):
            if (i+k-1) <= len(row):
                tmp *= row[i:(i+k)]
            else:
                tmp = 0

        if tmp > maxTotal:
            maxTotal = tmp
            sequence = row[i:(i+k)]
        else:
            pass

    # Vertical span O(n^2)
    vertMat = map(list, zip(*matrix)) # Vertical colums work as rows

    for column in vertMat:
        for i in range(len(column)):
            if (i+k-1) <= len(column):
                tmp *= column[i:(i+k)]
            else:
                tmp = 0

        if tmp > maxTotal:
            maxTotal = tmp
            sequence = column[i:(i+k)]
        else:
            pass

    # L-diag, R-diag


def zip_uneven():
    """ Recursive function to map diagnols"""
    pass
