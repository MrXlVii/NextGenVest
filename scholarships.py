"""Rough draft brute force solutions"""

import numpy as np

def findGreatest(self, lists, k):
    """Takes in matrix, finds k consecutive values that multiply to largest value"""

    sequence = [k]
    maxTotal = 0
    tmp = 0

    matrix = np.array(lists)

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
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

    diags = [n.tolist() for n in diags]

    # Diag sub-array span O(n^2)
    for seq in diags:
        if len(seq) >= k:
            for i in range(len(seq)):
                if (i+k-1) <= len(seq):
                    tmp *= seq[i:(i+k)]
                else:
                    tmp = 0
            if tmp > maxTotal:
                maxTotal = tmp
                sequence = seq[i:(i+k)]
            else:
                pass
        else:
            pass
