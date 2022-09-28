#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Square each element of matrix
    Args:
        matrix - a 2d lists
    """
    if matrix is None:
        return None
    return list(
        map(
            lambda row: list(map(lambda x: x**2, row)), matrix
        )
    )


if __name__ == '__main__':
    s = square_matrix_map([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(s)
