from flask import Flask, jsonify, make_response
import numpy as np

scholarships = Flask(__name__)

# Our pseudo-database:
data = []  # Put lists in this list
"""
In case you're generating with np.random.randint:

data = data.tolist()
"""
max_scholarship = []


@scholarships.route('/', methods=['GET'])
def getData():
    return jsonify({'data': data})


@scholarships.route('/max_scholarship', methods=['GET'])
def getMaxScholarship():
    return jsonify(max_scholarship)


@scholarships.route('/max_scholarship', methods=['POST'])
def maxScholarship():
    ms = MaxScholarship()
    vals = ms.findGreatest(data, 11)
    max_scholarship.append(vals)
    return jsonify(max_scholarship), 201


@scholarships.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


class MaxScholarship(object):

    def findGreatest(self, lists, k):
        matrix = np.array(lists)

        # Horizontal span
        horizontal = self.spanLists(lists, k)

        # Vertical span
        vertMat = map(list, zip(*matrix))  # Vertical columns work as rows
        vertical = self.spanLists(vertMat, k)

        # L-diag, R-diag
        diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0]+1, matrix.shape[1])]
        diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1, -matrix.shape[0], -1))
        diags = [n.tolist() for n in diags]

        diagnol = self.spanLists(diags, k)

        great = 0
        for val in [horizontal, vertical, diagnol]:
            if val['total'] > great:
                great = val['total']
                correct = val
            else:
                pass
        return correct


    def spanLists(self, lists, k):
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
