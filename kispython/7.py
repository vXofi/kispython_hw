class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index


def main(arr):
    default = [
        Node([arr[0], 'RUBY', 2003, 1977], 0),
        Node([arr[0], 'RUBY', 1967, 1977], 1),
        Node([arr[0], 'RUBY', 1974, 1977], 2),

        Node([2007, 'RUBY', arr[2], 1989], 3),
        Node([1978, 'RUBY', arr[2], 1989], 4),
        Node([1997, 'RUBY', arr[2], 1989], 5),

        Node([arr[0], 'SASS', arr[2], arr[3]], 6),

        Node([2007, 'ALLOY', 2003, arr[3]], 7),
        Node([2007, 'ALLOY', 1967, arr[3]], 8),
        Node([2007, 'ALLOY', 1974, arr[3]], 9),

        Node([1978, 'ALLOY', arr[2], arr[3]], 10),
        Node([1997, 'ALLOY', arr[2], arr[3]], 11)
    ]

    for node in default:
        if node.data == arr:
            return node.index
