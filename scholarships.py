"""Rough draft brute force solutions"""

import numpy as np

def findGreatest(self, lists, k):
    matrix = np.array(lists)

    # Horizontal span O(n^2)
    horizontal = spanLists(matrix, k)

    # Vertical span O(n^2)
    vertMat = map(list, zip(*matrix)) # Vertical colums work as rows
    vertical = spanLists(vertMat, k)

    # L-diag, R-diag
    diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1, -matrix.shape[0], -1))
    diags = [n.tolist() for n in diags]

    diagnol = spanLists(diags, k)

def spanLists(self, lists, k):
    """Takes in matrix, finds k consecutive values that multiply to largest value"""

    sequence = [k]
    maxTotal = 0
    tmp = 0
    response = {}

    for seq in lists:
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
    
    response['sequence'] = sequence
    response['total'] = maxTotal

    return response
