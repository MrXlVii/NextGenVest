from flask import Flask, jsonify, request
import numpy as np

scholarships = Flask(__name__)

data = [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]  # Our pseudo-database

@scholarships.route('/', methods=['GET'])
def get_data():
    return jsonify({'data': data})


def findGreatest(lists, k):

    matrix = np.array(lists)
    print matrix

    # Horizontal span
    horizontal = spanLists(lists, k)
    print horizontal

    # Vertical span
    vertMat = map(list, zip(*matrix))  # Vertical columns work as rows
    vertical = spanLists(vertMat, k)
    print vertical

    # L-diag, R-diag
    diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1, -matrix.shape[0], -1))
    diags = [n.tolist() for n in diags]

    diagnol = spanLists(diags, k)
    print diagnol

    great = 0
    for val in [horizontal, vertical, diagnol]:
        if val['total'] > great:
            great = val['total']
            correct = val
        else:
            pass

    return correct


def spanLists(lists, k):
    """Takes in matrix, finds k consecutive values that multiply to largest value"""
    sequence = []
    maxTotal = 0
    tmp = 0
    response = {}

    for seq in lists:
        if len(seq) >= k:
            for i in range(len(seq)):
                if (i+k-1) <= len(seq):
                    tmp = np.prod(seq[i:(i+k)])
                    if tmp > maxTotal:
                        maxTotal = tmp
                        del sequence[:]
                        sequence.append(seq[i:(i+k)])
                    else:
                        pass
                else:
                    tmp = 0
        else:
            pass

    print maxTotal
    response['sequence'] = sequence[0]
    response['total'] = maxTotal
    return response

if __name__ == '__main__':
    scholarships.run(debug=True)
